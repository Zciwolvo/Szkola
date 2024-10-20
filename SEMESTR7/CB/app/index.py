import json
import os
import bcrypt
import re
import datetime
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, set_access_cookies, unset_jwt_cookies

app = Flask(__name__)

# Configure your app
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret-key')
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/' 
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh' 
app.config['JWT_COOKIE_CSRF_PROTECT'] = False 
app.config['JWT_COOKIE_SECURE'] = False 

jwt = JWTManager(app)

# Password validation function
def validate_password(password):
    settings = get_settings()
    
    if not settings.get('password_criteria_enabled', True):
        return True 
    
    if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"[@$!%*?&#]", password):
        return False
    
    return True


# Load or reset the users database on startup
def load_users():
    # Reset the database
    users = [
        {
            "ID": "admin",
            "passwords": [bcrypt.hashpw(b"admin", bcrypt.gensalt()).decode('utf-8')],
            "role": "admin",
            "new_user": False,
            "last_password_change": "2023-07-01",
            "force_password_change": False  # New flag to force admin password change
        },
        {
            "ID": "user",
            "passwords": [bcrypt.hashpw(b"user", bcrypt.gensalt()).decode('utf-8')],
            "role": "user",
            "new_user": True,
            "last_password_change": "2023-07-01"
        }
    ]
    settings = {
        "password_criteria_enabled": True,
        "expiry_months": 3,
        "expiry_days": 0
    }

    with open('users.json', 'w') as f:
        json.dump({"users": users, "settings": settings}, f)
    return users


# Utility to read the user database and settings
def get_data():
    with open('users.json', 'r') as f:
        return json.load(f)

# Utility to save the user database and settings
def save_data(data):
    with open('users.json', 'w') as f:
        json.dump(data, f, indent=4)

# Get only users
def get_users():
    data = get_data()
    return data.get('users', [])

# Get only settings
def get_settings():
    data = get_data()
    return data.get('settings', {})

# Save both users and settings
def save_users_and_settings(users, settings):
    save_data({"users": users, "settings": settings})

# Create user
# Create user
@app.route('/admin/create_user', methods=['POST'])
@jwt_required()
def create_user():
    data = request.form  # Get the form data
    user_id = data.get('ID')  # Extract user ID from form
    password = data.get('password')  # Extract password from form
    role = data.get('role', 'user')  # Extract role, default to 'user'

    users = get_users()

    # Check if user already exists
    if any(u['ID'] == user_id for u in users):
        return {"error": "User already exists"}, 400

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Create new user
    new_user = {
        "ID": user_id,
        "passwords": [hashed_password],
        "role": role,
        "new_user": True,
        "last_password_change": None
    }

    # Add new user to the list
    users.append(new_user)
    settings = get_settings()

    # Save back to the JSON file
    save_users_and_settings(users,settings)

    return redirect(url_for('admin_dashboard'))


# Update user
@app.route('/admin/update_user/<user_id>', methods=['POST'])
@jwt_required()
def update_user(user_id):
    current_user = get_jwt_identity()

    if current_user['role'] != 'admin':
        return {"error": "Unauthorized access"}, 403

    users = get_users()
    user = next((u for u in users if u['ID'] == user_id), None)

    if not user:
        return {"error": "User not found"}, 404

    new_role = request.form.get('role')
    if new_role:
        user['role'] = new_role
    settings = get_settings()

    # Save back to the JSON file
    save_users_and_settings(users,settings)
    return redirect(url_for('admin_dashboard'))


# Delete user
@app.route('/admin/delete_user/<user_id>', methods=['POST'])
@jwt_required()
def delete_user(user_id):
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin':
        return {"error": "Unauthorized access"}, 403

    users = get_users()
    new_users = [u for u in users if u['ID'] != user_id]

    if len(users) == len(new_users):
        return {"error": "User not found"}, 404
    settings = get_settings()

    # Save back to the JSON file
    save_users_and_settings(users,settings)
    return redirect(url_for('admin_dashboard'))


@app.route('/')
def homepage():
    return render_template("login.html")

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    # Handle login via POST request
    data = request.get_json()  # Fetch JSON data from the request
    user_id = data.get('ID')
    password = data.get('password')

    users = get_users()
    user = next((u for u in users if u['ID'] == user_id), None)

    settings = get_settings()
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user['passwords'][-1].encode('utf-8')):
        # If the user is admin and the password is incorrect, force a password change on the next successful login
        if user and user['ID'] == 'admin':
            user['force_password_change'] = True
            save_users_and_settings(users, settings)
        
        return jsonify({"error": "Invalid credentials"}), 401

    # If login is successful, check if the admin account has the force_password_change flag set
    if user['ID'] == 'admin' and user.get('force_password_change', False):
        user['force_password_change'] = False  # Reset the flag after forcing a password change
        user['new_user'] = True  # Force password change
        save_users_and_settings(users, settings)

    # Create JWT token
    token = create_access_token(identity={'ID': user['ID'], 'role': user['role']})

    # Check if the user needs to change their password
    change_password_required = user['new_user'] or password_change_needed(user)
    response = jsonify({"token": token, "change_password": change_password_required, "role": user['role']})
    set_access_cookies(response, token)

    return response


# Admin dashboard (only admins can access)
@app.route('/admin/dashboard', methods=['GET'])
@jwt_required()
def admin_dashboard():
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin':
        return redirect(url_for('error_page', error='Unauthorized Access'))
    
    users = get_users() 
    settings = get_settings()

    return render_template('admin_dashboard.html', current_user=current_user, users=users, 
                           password_criteria_enabled=settings.get('password_criteria_enabled', True),
                           expiry_months=settings.get('expiry_months', 0),
                           expiry_days=settings.get('expiry_days', 0))

@app.route('/admin/update_password_policy', methods=['POST'])
@jwt_required()
def update_password_policy():
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin':
        return {"error": "Unauthorized access"}, 403
    
    # Get form data
    password_criteria_enabled = request.form.get('enable_password_criteria') == 'on'
    expiry_months = int(request.form.get('expiry_months', 0))
    expiry_days = int(request.form.get('expiry_days', 0))
    
    # Get current users and settings
    users = get_users()
    settings = get_settings()

    # Update the settings
    settings['password_criteria_enabled'] = password_criteria_enabled
    settings['expiry_months'] = expiry_months
    settings['expiry_days'] = expiry_days

    # Save updated settings
    save_users_and_settings(users, settings)

    return redirect(url_for('admin_dashboard'))


# Add an error handler for missing/invalid JWT
@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return redirect(url_for('error_page', error="Unauthorized access - Missing or invalid token"))

# User dashboard (for users)
@app.route('/user/dashboard', methods=['GET'])
@jwt_required()
def user_dashboard():
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'user':
        return redirect(url_for('error_page', error='Unauthorized Access'))
    
    # Pass the current_user information to the template
    return render_template('user_dashboard.html', current_user=current_user)

# Change password route
@app.route('/change_password/<user_id>', methods=['GET', 'POST'])
@jwt_required()
def change_password(user_id):
    error_message = None  # To store the error message

    if request.method == 'GET':
        return render_template("change_password.html", user_id=user_id)

    new_password = request.form.get('new_password')
    users = get_users()
    user = next((u for u in users if u['ID'] == user_id), None)

    if not validate_password(new_password):
        error_message = "Password doesn't meet the security criteria."
    else:
        # Check if new password is one of the last 12
        for old_password in user['passwords'][-12:]:
            if bcrypt.checkpw(new_password.encode('utf-8'), old_password.encode('utf-8')):
                error_message = "New password can't be one of the last 12 passwords."
                break

    if error_message:
        return render_template("change_password.html", user_id=user_id, error_message=error_message)

    # Add the new password (hashed) to the passwords list
    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user['passwords'].append(hashed_password)

    # Update the user to no longer be a new user, and update password change date
    user['new_user'] = False
    user['last_password_change'] = str(datetime.date.today())

    settings = get_settings()

    # Save back to the JSON file
    save_users_and_settings(users,settings)

    return redirect(url_for('user_dashboard' if user['role'] == 'user' else 'admin_dashboard'))


# Check if password change is needed
def password_change_needed(user):
    settings = get_settings()

    last_change = datetime.datetime.strptime(user['last_password_change'], '%Y-%m-%d')
    
    # Calculate the expiry time based on settings
    expiry_time = datetime.timedelta(days=settings['expiry_days'] + settings['expiry_months'] * 30)
    
    return (datetime.datetime.now() - last_change) > expiry_time


# Error page route
@app.route('/error')
def error_page():
    error = request.args.get('error')
    return render_template('error.html', error=error)

@app.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)
    return response

if __name__ == '__main__':
    load_users()  # Initialize/reset the database
    app.run(debug=True)
