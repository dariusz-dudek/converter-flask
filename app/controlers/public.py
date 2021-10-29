from flask import render_template, request, redirect, flash, abort
from app.repositories.forms import RegisterForm, LoginForm
from app.repositories.users import UserRepository
from hashlib import pbkdf2_hmac
from flask_login import login_user, logout_user, login_required


@login_required
def index():
    return render_template('public/index.html.jinja2')


def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """


def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = request.form.get('username')
        name = request.form.get('name')
        crypted_password = crypt_password(request.form.get('password'))
        repository = UserRepository()

        if username in repository.get_all_usernames():
            flash(f'The username {username} already exist.\nChoice another one.', 'warning')
            return redirect(request.url)

        flash('Account created!', 'success')
        repository.add(username, crypted_password, name)
        return redirect('/login')

    return render_template('public/register.html.jinja2', form=form)


def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        crypted_password = crypt_password(form.password.data)

        repository = UserRepository()
        user = repository.get_by_username(username)

        if user.password == crypted_password:
            login_user(user)
            return redirect('/')
        else:
            abort(400)

    return render_template('public/login.html.jinja2', form=form)


def logout():
    logout_user()
    return redirect('/login')


def crypt_password(password):
    salt = 'abcdef1234!@#$%'
    password = pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        999
    )
    return password.hex()

