from app import app
from app.controlers.public import index, about, register, login, logout, converter, upload
from app.controlers.admin import admin_dashboard
from flask_login import LoginManager
from app.repositories.users import UserRepository

app.config['SECRET_KEY'] = 'tI8vJbbVoLMorhI9x3xIRQ'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    repo = UserRepository()
    return repo.get_by_id(user_id)


app.add_url_rule('/', view_func=index, methods=['GET'])
app.add_url_rule('/about', view_func=about, methods=['GET'])
app.add_url_rule('/admin/dashboard', view_func=admin_dashboard, methods=['GET'])
app.add_url_rule('/register', view_func=register, methods=['POST', 'GET'])
app.add_url_rule('/login', view_func=login, methods=['POST', 'GET'])
app.add_url_rule('/logout', view_func=logout, methods=['GET'])
app.add_url_rule('/converter', view_func=converter, methods=['POST', 'GET'])
app.add_url_rule('/upload/<filename>', view_func=upload, methods=['POST', 'GET'])

