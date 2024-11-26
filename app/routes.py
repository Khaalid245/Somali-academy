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

@main.route('/about')
def about():
    return render_template('home/about.html')
@main.route('/courses')
def courses():
    return render_template('home/courses.html')

@main.route('/services')
def services():
    return render_template('home/services.html')




