import json
import os
import bcrypt
import re
import datetime
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, set_access_cookies, unset_jwt_cookies
import requests
import math
import random
import time


app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure your app
app.config['secret'] = 'SECRET KEY'
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret-key')
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/' 
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh' 
app.config['JWT_COOKIE_CSRF_PROTECT'] = False 
app.config['JWT_COOKIE_SECURE'] = False 

jwt = JWTManager(app)

failed_attempts = {}

def log_entry(user, action, description):
    settings = get_settings()
    if settings['logging_enabled']:
        log_data = {
            "user": user,
            "action": action,
            "description": description,
            "timestamp": str(datetime.datetime.now())
        }
        with open('logs.json', 'a') as f:
            json.dump(log_data, f)
            f.write("\n")

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
            "last_password_change": "2024-11-01",
            "force_password_change": False,
            "single_use_password": False
        },
        {
            "ID": "user",
            "passwords": [bcrypt.hashpw(b"user", bcrypt.gensalt()).decode('utf-8')],
            "role": "user",
            "new_user": True,
            "last_password_change": "2023-07-01",
            "force_password_change": False,
            "single_use_password": False
        },
        {
            "ID": "user_manager",
            "passwords": [],
            "role": "user_manager",
            "new_user": True,
            "last_password_change": "2023-07-01",
            "force_password_change": False,
            "single_use_password": True
        },
        {
            "ID": "session_manager",
            "passwords": [],
            "role": "session_manager",
            "new_user": True,
            "last_password_change": "2023-07-01",
            "force_password_change": False,
            "single_use_password": True
        },
        {
            "ID": "debugger",
            "passwords": [],
            "role": "debugger",
            "new_user": True,
            "last_password_change": "2023-07-01",
            "force_password_change": False,
            "single_use_password": True
        }
    ]
    settings = {
        "password_criteria_enabled": True,
        "expiry_months": 3,
        "expiry_days": 0,
        "logging_enabled": True,
        "session_timeout": 1
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

def get_user(user_id):
    users = get_users()
    for user in users:
        if user["ID"] == user_id:
            return user
    return {}

# Get only settings
def get_settings():
    data = get_data()
    return data.get('settings', {})

# Save both users and settings
def save_users_and_settings(users, settings):
    save_data({"users": users, "settings": settings})


@app.before_request
def enforce_session_timeout():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=get_settings().get('session_timeout', 10))
    session.modified = True


@app.route('/get_user_role', methods=['GET'])
@jwt_required()
def get_user_role():
    user_id = get_jwt_identity()
    users = get_users()
    user = next((u for u in users if u['ID'] == user_id), None)

    if user:
        return jsonify({"role": user['role']}), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/admin/toggle_logging', methods=['POST'])
@jwt_required()
def toggle_logging():
    current_user = get_jwt_identity()

    if current_user['role'] != 'admin' and current_user['role'] != 'session_manager':
        log_entry('Unknown', "toggle_logging", f"Unauthorized user tried to change toggle logging rule")
        return {"error": "Unauthorized access"}, 403
    
    settings = get_settings()
    users = get_users()
    toggle_logging_form = request.form.get('enable_logging') == 'on'
    settings['logging_enabled'] = toggle_logging_form
    log_entry(current_user['ID'], "toggle_logging", f"Logging set to {settings['logging_enabled']}")
    save_users_and_settings(users, settings)

    return redirect(url_for('admin_dashboard'))


@app.route('/admin/view_logs', methods=['GET'])
@jwt_required()
def view_logs():
    current_user = get_jwt_identity()

    if current_user['role'] != 'admin' and current_user['role'] != 'debugger':
        log_entry('Unknown', "view_logs", f"Unauthorized user tried to see logs")
        return {"error": "Unauthorized access"}, 403

    user = get_user(current_user['ID'])
    if user['force_password_change'] or user['new_user']:
        return render_template('change_password.html', user_id=current_user['ID'])

    logs = []
    with open('logs.json', 'r') as f:
        for line in f:
            logs.append(json.loads(line.strip()))  # Load each line as a JSON object

    return render_template('view_logs.html', logs=logs)


# Create user
@app.route('/admin/create_user', methods=['POST'])
@jwt_required()
def create_user():
    current_user = get_jwt_identity()
    data = request.form  # Get the form data
    user_id = data.get('ID')  # Extract user ID from form
    password = data.get('password')  # Extract password from form
    role = data.get('role', 'user')  # Extract role, default to 'user'
    single_use_password = 'single_use_password' in data  # Check if checkbox is checked

    users = get_users()
    
    if current_user['role'] != 'admin' and current_user['role'] != 'user_manager':
        return {"error": "Unauthorized access"}, 403

    # Check if user already exists
    if any(u['ID'] == user_id for u in users):
        log_entry(f'{current_user["ID"]}', "create_user", "Creating user failed because such user already exists")
        return {"error": "User already exists"}, 400

    # Hash the password only if it's not a single-use password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') if not single_use_password else None

    # Create new user
    new_user = {
        "ID": user_id,
        "passwords": [hashed_password] if hashed_password else [],  # Only include passwords if it's not single-use
        "role": role,
        "new_user": True,
        "last_password_change": None,
        "single_use_password": single_use_password,
    }

    # Add new user to the list
    users.append(new_user)
    settings = get_settings()

    # Save back to the JSON file
    save_users_and_settings(users, settings)
    log_entry(current_user["ID"], "create_user", f"{current_user['ID']} has created user {user_id}")
    return redirect(url_for('admin_dashboard'))


# Update user
@app.route('/admin/update_user/<user_id>', methods=['POST'])
@jwt_required()
def update_user(user_id):
    current_user = get_jwt_identity()

    if current_user['role'] != 'admin' and current_user['role'] != 'user_manager':
        return {"error": "Unauthorized access"}, 403

    users = get_users()
    user = next((u for u in users if u['ID'] == user_id), None)

    if not user:
        log_entry(f'{current_user['ID']}', "update_user", f"User to be updated not found")
        return {"error": "User not found"}, 404

    new_role = request.form.get('role')
    if new_role:
        user['role'] = new_role
    settings = get_settings()

    # Save back to the JSON file
    save_users_and_settings(users,settings)
    log_entry(current_user['ID'], "update_user", f"{current_user['ID']} has updated user {user_id} role")
    return redirect(url_for('admin_dashboard'))


# Delete user
@app.route('/admin/delete_user/<user_id>', methods=['POST'])
@jwt_required()
def delete_user(user_id):
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin' and current_user['role'] != 'user_manager':
        log_entry(f'Unknown', "delete_user", f"Unauthorized access attept to user deletion")
        return {"error": "Unauthorized access"}, 403

    users = get_users()
    new_users = [u for u in users if u['ID'] != user_id]

    if len(users) == len(new_users):
        log_entry(f'{current_user['ID']}', "delete_user", f"User to be deleted not found")
        return {"error": "User not found"}, 404

    users = new_users
    settings = get_settings()

    save_users_and_settings(users, settings)
    log_entry(current_user['ID'], "delete_user", f"{current_user['ID']} has deleted user {user_id}")
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/modify_user/<user_id>', methods=['POST'])
@jwt_required()
def modify_user(user_id):
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin' and current_user['role'] != 'user_manager':
        log_entry(f'Unknown', "modify_user", f"Unauthorized access attept to user modify user")
        return {"error": "Unauthorized access"}, 403

    users = get_users()

    # Find the user to modify
    user_to_modify = next((u for u in users if u['ID'] == user_id), None)
    if not user_to_modify:
        log_entry(f'{current_user['ID']}', "modify_user", f"User to be modified not found")
        return {"error": "User not found"}, 404

    # Get the new data from the form
    new_id = request.form.get('new_id')
    new_password = request.form.get('new_password')

    # Update the user's information
    if new_id:
        user_to_modify['ID'] = new_id
    if new_password:
        new_password = new_password.encode(encoding="utf-8")  
        user_to_modify['password'] = bcrypt.hashpw(new_password, bcrypt.gensalt()).decode('utf-8')

    # Save the updated user data
    settings = get_settings()
    save_users_and_settings(users, settings)
    log_entry(current_user['ID'], "modify_user", f"{current_user['ID']} has modified user {user_id}")

    return redirect(url_for('admin_dashboard'))



@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        a = round(random.uniform(0.1, 2.0), 2)
        x = round(random.uniform(0.1, 2.0), 2)
        single_use_password = round(math.exp(-a * x), 2) 
        session['single_use_password'] = single_use_password  
        session['a'] = a
        session['x'] = x
        return render_template("login.html", a=a, x=x) 

    data = request.get_json()
    user_id = data.get('ID')
    password = data.get('password')

    users = get_users()
    user = next((u for u in users if u['ID'] == user_id), None)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if failed_attempts.get(user_id, {'count': 0, 'timestamp': 0})['count'] >= 5:
        if time.time() - failed_attempts[user_id]['timestamp'] < 15 * 60:
            return jsonify({"error": "Account is locked. Try again later."}), 403
        else:
            failed_attempts[user_id] = {'count': 0, 'timestamp': 0}

    if user.get('single_use_password'):
        try:
            single_use_password_correct = math.isclose(float(password), session['single_use_password'], rel_tol=1e-9)
        except:
            return jsonify({"error": "New user needs to solve equation!"}), 401
        if not single_use_password_correct:
            failed_attempts[user_id] = {
                'count': failed_attempts.get(user_id, {'count': 0})['count'] + 1,
                'timestamp': time.time()
            }
            return jsonify({"error": "Invalid credentials"}), 401
    else:
        correct_password = bcrypt.checkpw(password.encode('utf-8'), user['passwords'][-1].encode('utf-8'))
        if not correct_password:
            failed_attempts[user_id] = {
                'count': failed_attempts.get(user_id, {'count': 0})['count'] + 1,
                'timestamp': time.time()
            }
            return jsonify({"error": "Invalid credentials"}), 401

    # Determine if password change is needed
    current_date = datetime.date.today()
    
    password_change_needed = (user['new_user'] or 
                              (current_date - datetime.datetime.strptime(user['last_password_change'], "%Y-%m-%d").date()).days > 90 or 
                              user.get('force_password_change'))

    failed_attempts[user_id] = {'count': 0, 'timestamp': 0}
    
    token = create_access_token(identity={'ID': user['ID'], 'role': user['role']})
    
    if password_change_needed:
        response = jsonify({"token": token, "change_password": True, "role": user['role']})
    else:
        response = jsonify({"token": token, "change_password": False, "role": user['role']})

    set_access_cookies(response, token)

    return response




# Admin dashboard (only admins can access)
@app.route('/admin/dashboard', methods=['GET', 'POST'])
@jwt_required()
def admin_dashboard():
    current_user = get_jwt_identity()
    print(current_user['role'])
    allowed = ['admin', 'user_manager', 'session_manager', 'debugger']
    if current_user['role'] not in allowed:
        return {"error": "Unauthorized access"}, 403
    ''
    user = get_user(current_user['ID'])
    if user['force_password_change'] or user['new_user']:
        return render_template('change_password.html', user_id=current_user['ID'])
    users = get_users()
    settings = get_settings()
    if request.method == 'POST':
        # Update session timeout setting
        session_timeout = int(request.form.get('session_timeout', 10))
        settings['session_timeout'] = session_timeout
        save_users_and_settings(users, settings)
        log_entry(current_user['ID'], "update_session_timeout", f"Session timeout updated to {session_timeout} minutes")

    return render_template('admin_dashboard.html', users=users, settings=settings, current_user=current_user)


@app.route('/admin/update_password_policy', methods=['POST'])
@jwt_required()
def update_password_policy():
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin' and current_user['role'] != 'session_manager':
        log_entry(f'Unknown', "update_password_policy", f"Unauthorized access attempt to change password policy")
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
    log_entry(current_user['ID'], "create_user", f"{current_user['ID']} has toggled password policy")

    return redirect(url_for('admin_dashboard'))


# Add an error handler for missing/invalid JWT
@jwt.unauthorized_loader
def unauthorized_callback(callback):
    print("Unauthorized access attempt detected")
    print("Callback details:", callback)
    return redirect(url_for('error_page', error="Unauthorized access - Missing or invalid token"))


# User dashboard (for users)
@app.route('/user/dashboard', methods=['GET'])
@jwt_required()
def user_dashboard():
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'user':
        log_entry(f'Unknown', "user/dashboard", f"Unauthorized access attept to user dashboard")
        return redirect(url_for('error_page', error='Unauthorized Access'))
    user = get_user(current_user['ID'])
    if user['force_password_change'] or user['new_user']:
        return render_template('change_password.html', user_id=current_user['ID'])
    # Pass the current_user information to the template
    return render_template('user_dashboard.html', current_user=current_user)

@app.route('/change_password/<user_id>', methods=['GET', 'POST'])
@jwt_required()
def change_password(user_id):
    current_user = get_jwt_identity()
    error_message = None  # To store the error message

    users = get_users()
    user = next((u for u in users if u['ID'] == user_id), None)

    if not user:
        log_entry(f'{current_user["ID"]}', "change_password", "User not found")
        return {"error": "User not found"}, 404

    # Check if the user is new and does not have a password set
    is_new_user = user['new_user'] and not user['passwords']

    if request.method == 'GET':
        return render_template("change_password.html", user_id=user_id, is_new_user=is_new_user)

    # If POST request, handle password change logic
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    recaptcha_response = request.form.get('g-recaptcha-response')  # Get reCAPTCHA response

    # Verify reCAPTCHA response with Google API
    secret_key = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
    recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': secret_key,
        'response': recaptcha_response
    }
    recaptcha_verification = requests.post(recaptcha_url, data=payload)
    recaptcha_result = recaptcha_verification.json()

    if not recaptcha_result.get('success'):
        error_message = "reCAPTCHA verification failed. Please try again."

    # Verify old password if the user is not new
    if not error_message and not is_new_user:
        if user['passwords'] and not bcrypt.checkpw(old_password.encode('utf-8'), user['passwords'][-1].encode('utf-8')):
            error_message = "Old password is incorrect."

    # Validate new password criteria if no error so far
    if not error_message and not validate_password(new_password):
        error_message = "New password doesn't meet the security criteria."
    
    # Check if new password was used in the last 12 passwords
    if not error_message:
        for old_password in user['passwords'][-12:]:
            if bcrypt.checkpw(new_password.encode('utf-8'), old_password.encode('utf-8')):
                error_message = "New password can't be one of the last 12 passwords."
                break

    # If there's an error, re-render the form with the error message
    if error_message:
        return render_template("change_password.html", user_id=user_id, error_message=error_message, is_new_user=is_new_user)

    # Add the new password (hashed) to the passwords list
    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user['passwords'].append(hashed_password)

    # Update the user to no longer be a new user, and update password change date
    user['new_user'] = False
    user['last_password_change'] = str(datetime.date.today())

    # Save back to the JSON file
    settings = get_settings()
    save_users_and_settings(users, settings)
    log_entry(current_user['ID'], "change_password", f"{current_user['ID']} has changed password")

    # Redirect based on user role
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
@jwt_required()
def logout():
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)  # Clear JWT token cookies
    return response

if __name__ == '__main__':
    load_users()  # Initialize/reset the database
    app.run(debug=True)
