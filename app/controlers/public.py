from flask import render_template, request, redirect, flash, abort, url_for, send_from_directory
from app.converter.containers.xml_template_classes_full_classes import DocumentInvoice
from app.converter.add_function import AddFunction

from app.converter.converter_method.excel_mag_krak import MagKrak
from app.converter.converter_method.raw_pol import Rawpol
from app.converter.converter_method.sewera_csv import Sewera

from app.repositories.forms import RegisterForm, LoginForm
from app.repositories.users import UserRepository
from hashlib import pbkdf2_hmac
from flask_login import login_user, logout_user, login_required
from os.path import splitext, join
from app import app


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


@login_required
def converter():
    option = request.form.get('option')

    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['file']
            if uploaded_file.filename == '':
                flash('The filename is empty', 'warning')
                return redirect(url_for('converter'))
            file_ext = splitext(uploaded_file.filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                flash('Unsupported file type', 'warning')
                return redirect(url_for('converter'))
            uploaded_file.save(join(app.config['UPLOAD_PATH'], f'input{file_ext}'))
            converter_method(option, file_ext)
            upload(f'{option}.xml')
            flash('Conversion created', 'success')

    return render_template('public/converter.html.jinja2')

@login_required
def upload(filename):
    return send_from_directory(app.config['RESULT'], filename, as_attachment=True)


def converter_method(method, ext):
    xml_document = DocumentInvoice()
    match method:

        case 'mag_krak_xls':
            mag_krak = MagKrak()
            AddFunction.load_file(mag_krak, xml_document, method, ext)

        case 'raw_pol_csv':
            raw_pol = Rawpol()
            AddFunction.load_file(raw_pol, xml_document, method, ext)

        case 'sewera_csv':
            sewera = Sewera()
            AddFunction.load_file(sewera, xml_document, method, ext)
