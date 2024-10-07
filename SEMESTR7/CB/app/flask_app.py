from flask import Flask, request, jsonify, render_template, redirect, url_for
from functools import wraps
import json
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Load users from JSON database
def load_users():
    with open('database.json', 'r') as f:
        return json.load(f)

# Save users to JSON database
def save_users(users):
    with open('database.json', 'w') as f:
        json.dump(users, f, indent=4)

# JWT decorator for protected routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-tokens')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = next((user for user in load_users() if user['ID'] == data['ID']), None)
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Validate password strength
def validate_password(password):
    if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"[@$!%*?&#]", password):
        return False
    return True

# Check password expiration
def check_password_expiration(last_change, days_valid=90):
    last_change_date = datetime.datetime.strptime(last_change, '%Y-%m-%d')
    if (datetime.datetime.utcnow() - last_change_date).days > days_valid:
        return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        user_id = request.form['ID']
        password = request.form['password']
        user = next((user for user in users if user['ID'] == user_id), None)

        if user and check_password_hash(user['passwords'][-1], password):
            if user['new_user'] or check_password_expiration(user['last_password_change']):
                return redirect(url_for('change_password', user_id=user_id))
            
            token = jwt.encode({'ID': user['ID'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
                               app.config['SECRET_KEY'], algorithm="HS256")
            return jsonify({'token': token})
        return 'Invalid credentials', 401
    return render_template('login.html')

@app.route('/change_password/<user_id>', methods=['GET', 'POST'])
def change_password(user_id):
    if request.method == 'POST':
        new_password = request.form['new_password']
        if not validate_password(new_password):
            return 'Password must be at least 8 characters long, contain one capital letter, and one special character', 400
        
        users = load_users()
        for user in users:
            if user['ID'] == user_id:
                hashed_password = generate_password_hash(new_password)
                # Check if the new password is different from the last 12
                if any(check_password_hash(old_password, new_password) for old_password in user['passwords'][-12:]):
                    return 'New password must be different from the last 12 passwords.', 400
                user['passwords'].append(hashed_password)
                if len(user['passwords']) > 12:
                    user['passwords'] = user['passwords'][-12:]
                user['new_user'] = False
                user['last_password_change'] = datetime.datetime.utcnow().strftime('%Y-%m-%d')
        save_users(users)
        return redirect(url_for('login'))
    return render_template('change_password.html')

@app.route('/admin/users', methods=['GET', 'POST'])
@token_required
def admin_dashboard(current_user):
    if current_user['role'] != 'admin':
        return 'Access denied', 403

    if request.method == 'POST':
        new_user = {
            'ID': request.form['ID'],
            'passwords': [generate_password_hash(request.form['password'])],
            'role': request.form['role'],
            'new_user': True,
            'last_password_change': datetime.datetime.utcnow().strftime('%Y-%m-%d')
        }
        users = load_users()
        users.append(new_user)
        save_users(users)
    users = load_users()
    return render_template('dashboard.html', users=users)

@app.route('/admin/users/<user_id>', methods=['PUT', 'DELETE'])
@token_required
def manage_user(current_user, user_id):
    if current_user['role'] != 'admin':
        return 'Access denied', 403

    users = load_users()
    user = next((u for u in users if u['ID'] == user_id), None)
    if not user:
        return 'User not found', 404

    if request.method == 'PUT':
        user['role'] = request.form['role']
        save_users(users)
        return 'User updated', 200

    if request.method == 'DELETE':
        users.remove(user)
        save_users(users)
        return 'User deleted', 200

if __name__ == '__main__':
    app.run(debug=True)
