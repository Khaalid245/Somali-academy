from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home/home.html')

@main.route('/dashboard')
def dashboard():
    return render_template('student/dashboard.html')

@main.route('/admin')
def admin():
    return render_template('admin_center/admin.html')
