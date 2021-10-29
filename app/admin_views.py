from app import app
from app.controlers.admin import admin_dashboard

app.add_url_rule('/admin/dashboard', view_func=admin_dashboard, methods=['GET'])
