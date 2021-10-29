import psycopg2
from flask import g
from dotenv import load_dotenv
from os import getenv

load_dotenv()


def init_app(app):
    app.teardown_appcontext(close_connection)

def get_connection():
    if 'connection' not in g:
        if getenv('DATABASE_URL', None) is not None:
            g.connection = psycopg2.connect(
                getenv('DATABASE_URL'),
                sslmode='require'
            )
        else:
            g.connection = psycopg2.connect(
                dbname=getenv('DB_NAME', 'app'),
                user=getenv('DB_USER', 'app'),
                password=getenv('DB_PASSWORD', 'admin123'),
                host=getenv('DB_HOST', 'db')
            )
    return g.connection


def close_connection():
    connection = g.pop('connection', None)

    if connection is not None:
        connection.close()
