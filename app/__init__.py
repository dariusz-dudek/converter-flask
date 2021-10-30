from flask import Flask

app = Flask(__name__)

from app import views
from app import admin_views

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.csv', '.xls', '.xml', '.xlsx']
app.config['UPLOAD_PATH'] = 'app/static/uploaded_files'

