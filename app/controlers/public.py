from flask import render_template, request, redirect, flash
from app.repositories.forms import RegisterForm
from app.repositories.users import UserRepository
from hashlib import pbkdf2_hmac


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
        cryptded_password = crypt_password(request.form.get('password'))
        print(f'Username: {username}\nName: {name}\nPassword: {cryptded_password}')
        repository = UserRepository()

        if username in repository.get_all_usernames():
            flash(f'The username {username} already exist. Choice another one.', 'warning')
            print('Already exists')
            return redirect(request.url)

        flash('Account created!', 'success')
        return redirect(request.url)
        # try:
        #     repository.add(username, password, name)
        #     return redirect(request.url)
        # except errors.lookup(UNIQUE_VIOLATION) as e:
        #     print(e)
    return render_template('public/register.html.jinja2', form=form)


def crypt_password(password):
    salt = 'abcdef1234!@#$%'
    password = pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        999
    )
    return password.hex()

