import sqlite3

class DatabaseManager:

    def __init__(self, db_path):
        self.__db_path = db_path
        self.connection = None

    def connect_db(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.__db_path)
    
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

    def close_db(self):
        if self.connection:
            self.connection.close()
            self.connection = None