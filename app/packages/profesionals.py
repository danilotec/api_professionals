from packages.database_manager import DatabaseManager

class Professional(DatabaseManager):
    def __init__(self, name, specialty, db_path):
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
                specialty TEXT NOT NULL
            )
        '''
        self.execute_query(query)

    def add_professional(self):
        query = "INSERT INTO professionals (name, specialty) VALUES (?,?)"
        self.execute_query(query, (self.name, self.specialty))

    def get_professionals(self):
        return self.execute_query("SELECT * FROM professionals")
