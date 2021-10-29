from app import app
from app.controlers.public import index, about, register
from app.controlers.admin import admin_dashboard

app.config['SECRET_KEY'] = 'tI8vJbbVoLMorhI9x3xIRQ'


app.add_url_rule('/', view_func=index, methods=['GET'])
app.add_url_rule('/about', view_func=about, methods=['GET'])
app.add_url_rule('/admin/dashboard', view_func=admin_dashboard, methods=['GET'])
app.add_url_rule('/register', view_func=register, methods=['POST', 'GET'])
# app.add_url_rule('/test', view_func=test, methods=['POST', 'GET'])

