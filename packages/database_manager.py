import sqlite3
from functools import wraps

class DatabaseManager:

    def __init__(self, db_path):
        self.__db_path = db_path
        self.connection = None

    def connect_db(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.__db_path)
    
    def close_db(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, params=None):
        self.connect_db()
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Erro ao executar a consulta {e}')
            return None

    def verify_in_database(self, value, value2, table, column, column2):
        self.connect_db()
        cursor = self.connection.cursor()   
        try:
            cursor.execute(f'SELECT 1 FROM {table} WHERE {column} = ? AND {column2} = ?', (value,value2))
            if cursor.fetchone():
                return False
            else:
                return True
        except sqlite3.Error as e:
            print(f'Erro ao executar a consulta {e}')
            return None

