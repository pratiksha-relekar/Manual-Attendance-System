from flask import Flask, render_template, redirect, url_for, request
import re  # Import regex module for password validation

app = Flask(__name__)

# Route for landing page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Function to validate password
def is_valid_password(password):
    # Password must contain at least one uppercase letter, one lowercase letter,
    # one number, one special character, and be at least 8 characters long.
    if (len(password) >= 8 and
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return True
    return False

# Route for user login (login.html)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Check if the email is a valid Gmail address
        if email.endswith('@gmail.com') and is_valid_password(password):
            return redirect(url_for('user_dashboard'))  # Redirect to user dashboard
        else:
            # If login fails, redirect back to the login
            return redirect(url_for('login'))  # Stay on user login page if invalid credentials
    return render_template('login.html')

# Route for admin login (admin_login.html)
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Check if the email is a valid Gmail address and password is valid
        if email.endswith('@gmail.com') and is_valid_password(password):
            return redirect(url_for('admin_dashboard'))  # Redirect to admin dashboard
        elif email == "admin@example.com" and password == "Admin@123":
            return redirect(url_for('admin_dashboard'))  # Redirect to admin dashboard if admin credentials are correct
        else:
            # If login fails, redirect back to the admin login
            return redirect(url_for('admin_login'))  # Stay on admin login page if invalid credentials
    return render_template('admin_login.html')

# Route for user dashboard
@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')

# Route for admin dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Route for register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle user registration logic here
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
