from app.repositories.db import get_connection
from psycopg2 import extras
from app.repositories.auth import User


class UserRepository:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(cursor_factory=extras.RealDictCursor)

    def map_row_to_user(self, row):
        user = User()
        user.id = row['id']
        user.username = row['username']
        user.password = row['password']
        user.name = row['name']
        user.admin = row['admin']

    def get_by_username(self, username):
        self.cursor.execute(
            'SELECT id, username, password, name, admin FROM users WHERE username=%s', (username,)
        )
        return self.map_row_to_user(self.cursor.fetchone())

    def get_by_id(self, user_id):
        self.cursor.execute(
            'SELECT id, username, password, name, admin FROM users WHERE id=%s', (user_id,)
        )
        return self.map_row_to_user(self.cursor.fetchone())

    def get_all_usernames(self):
        self.cursor.execute(
            'SELECT username FROM users'
        )
        return [user['username'] for user in self.cursor.fetchall()]

    def add(self, username, password, name, admin=0):
        self.cursor.execute(
            'INSERT INTO users (username, password, name, admin) VALUES (%s, %s, %s, %s) RETURNING id',
            (username, password, name, admin)
        )
        user_id = self.cursor.fetchone()
        self.connection.commit()
        return user_id['id']
