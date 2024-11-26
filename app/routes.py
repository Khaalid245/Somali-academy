from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, User, Role
from app.forms import RegistrationForm, LoginForm


main = Blueprint('main', __name__)


@main.route('/signup', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        role = Role.query.filter_by(name=form.role.data).first()
        if not role:
            flash('Selected role is invalid. Please contact support.', 'danger')
            return redirect(url_for('main.register'))

        user = User(
            username=form.username.data,
            email=form.email.data,
            role_id=role.id
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('main.login'))

    return render_template('home/signup.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # Redirect based on the role
        return redirect_role_dashboard()

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            # Redirect based on the role
            return redirect_role_dashboard()
        flash('Invalid email or password.', 'danger')
    return render_template('home/login.html', form=form)


# Utility function for role-based redirection
def redirect_role_dashboard():
    """Redirect users based on their roles."""
    if current_user.is_admin:
        return redirect(url_for('main.admin'))
    
    elif current_user.role.name == 'instructor':
        return redirect(url_for('main.instructors'))
    else:
        
        return redirect(url_for('main.dashboard'))
    


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))

@main.route('/')
def home():
    return render_template('home/home.html')


@main.route('/dashboard')
def dashboard():
    return render_template('student/dashboard.html')

@main.route('/admin_user')
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



@main.route('/intructors')
def instructors():
    return render_template('instructors/instructors.html')

