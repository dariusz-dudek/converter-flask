from app import app
from flask import render_template

@app.errorhandler(413)
def too_large(e):
    return render_template('public/response_codes/413.html.jinja2')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('public/response_codes/404.html.jinja2')\

@app.errorhandler(500)
def server_error(e):
    return render_template('public/response_codes/500.html.jinja2')