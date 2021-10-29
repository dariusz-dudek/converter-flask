from flask import render_template


def admin_dashboard():
    return render_template('admin/dashboard.html.jinja2')
