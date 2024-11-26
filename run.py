from app import create_app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
app = create_app()


from app.models import db, Role, User



def seed_roles():
    roles = ['student', 'instructor']
    for role_name in roles:
        if not Role.query.filter_by(name=role_name).first():
            db.session.add(Role(name=role_name))
    db.session.commit()
    print("Roles seeded successfully!")


admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')


with app.app_context():
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Role, db.session))



if __name__ == '__main__':

    with app.app_context():
        db.create_all()
        seed_roles()
    app.run(debug=True)
