from packages.database_manager import DatabaseManager
import json

class Professional(DatabaseManager):
    def __init__(self, db_path, name=None, specialty=None ):
        self.name = name
        self.specialty = specialty
        self.avaliable_times = []
        super().__init__(db_path)

    def book_time(self, time):
        if time not in self.avaliable_times:
            print(f'Novo horario cadastrado: {time}hrs')
            self.avaliable_times.append(time)
        else:
            print(f'O horário {time} já está disponível.')
        
    def create_professional_table(self):
        super().connect_db()
        query = '''
            CREATE TABLE IF NOT EXISTS professionals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                specialty TEXT NOT NULL,
                times TEXT
            )
        '''
        self.execute_query(query)

    
    def add_professional(self):
        verify = self.verify_in_database(value=self.name, value2=self.specialty,table='professionals', column='name', column2='specialty')
        if not verify:
            query = "INSERT INTO professionals (name, specialty) VALUES (?,?)"
            self.execute_query(query, (self.name, self.specialty))
            super().close_db()
            return json.dumps({'status': 'success professional cadaster'}), 201
        return json.dumps({'status': 'professional allredy exits'}), 409
    
    
    def add_times_professionals(self, id_professional, times: list):
        verify = self.verify_for_id(id_professional)
        if verify:
            times_json = json.dumps(times)
            query = "UPDATE professionals SET times = ? WHERE id = ?"
            try:
                self.execute_query(query, (times_json, id_professional))
                return json.dumps({'status': 'success update'}), 200
            except Exception as e:
                return json.dumps({'status': 'error', 'message': str(e)}), 500
            finally:
                super().close_db()
        return json.dumps({'status': 'id not found'}), 409
    
    def get_professionals(self):
        return self.execute_query("SELECT * FROM professionals")


