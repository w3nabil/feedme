from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__, template_folder='public')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    page_title = "Login"

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        fa2 = request.form.get('2fa') 
        from .db_custom import User

        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                if user.fa2 == fa2.lower():
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    message = "Invalid Login, Try Again!"
                    return render_template('login.html', page_title=page_title, message=message)
            else:
                message = "Invalid Login, Try Again!"
                return render_template('login.html', page_title=page_title, message=message)
        else:
            message = "Invalid Login, Try Again!"
            return render_template('login.html', page_title=page_title, message=message)

    return render_template('login.html', page_title=page_title)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    page_title = "Sign Up"
    from .models import pwdchecker, emailchecker, userchecker
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        fa2 = request.form.get('2fa')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        message = emailchecker(email)
        if message is not None:
            return render_template('register.html', page_title=page_title, message=message)
        else:
            message = userchecker(username)
            if message is not None:
                try:
                    return render_template('register.html', page_title=page_title, message=message)
                except:
                    message = "Username already exists. Try another one!"
            else:
                if password == password2:
                    message = pwdchecker(password)
                    if message is not None:
                        return render_template('register.html', page_title=page_title, message=message)
                    else:
                        page_title = "Login"
                        from .db_custom import User 
                        new_user = User(email=email, username=username, password=generate_password_hash(password), fa2=fa2.lower())
                        from . import db 
                        db.session.add(new_user)
                        db.session.commit()
                        message = "Account created successfully. Try accessing!"
                        return redirect(url_for('auth.login'))

    else:
        return render_template('register.html', page_title=page_title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))