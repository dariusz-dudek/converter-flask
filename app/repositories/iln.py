from app.repositories.db import get_connection
from psycopg2 import extras

class IlnRepository:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(cursor_factory = extras.RealDictCursor)

    def get_by_nip(self, nip: str):
        self.cursor.execute(
            'SELECT iln FROM company WHERE nip=%s', (nip,)
        )
        answer = self.cursor.fetchone()
        return answer['iln'] if answer is not None else ''


    def add(self, nip: str, name: str, iln: str):
        self.cursor.execute(
            'INSERT INTO company (nip, name, iln) VALUES (%s, %s, %s)',
            (nip, name, iln)
        )
        company_id = self.cursor.fetchone()
        self.connection.commit()
        return company_id['id']

    def delete(self, nip: str):
        self.cursor.execute(
            'DELETE FROM company WHERE nip=%s', (nip,)
        )
        self.connection.commit()

