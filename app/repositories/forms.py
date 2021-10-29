from wtforms import Form, StringField, PasswordField, validators


class RegisterForm(Form):
    username = StringField('User name: ', [validators.Length(min=5)])
    name = StringField('Name: ')
    password = PasswordField('Password: ', [
        validators.Length(min=8),
        validators.EqualTo('password_repeat')
    ])
    password_repeat = PasswordField('Repeat password: ')


class LoginForm(Form):
    username = StringField('User name: ', [validators.Length(min=5)])
    password = PasswordField('Password: ', [validators.Length(min=8)])
