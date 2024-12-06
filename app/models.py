import json,sqlite3


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


class Customer(DatabaseManager):
    
    def __init__(self, name, phone, db_path):
        self.name = name
        self.phone = phone
        super().__init__(db_path)

    
    def create_customer_table(self):
        super().connect_db()
        query = '''
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL    
                )
        '''
        self.execute_query(query)

    def add_customer(self):
        query = "INSERT INTO customers (name, phone) VALUES (?,?)"
        self.execute_query(query, (self.name, self.phone))
    
    def get_customers(self):
        return self.execute_query("SELECT * FROM customers")
    

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

    
class Schedule(Customer, Professional):

    def __init__(self):
        self.customers = []
        self.professionals = []
        self.appointments = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f'{customer} adcionado.')

    def add_professinal(self, professional):
        self.professionals.append(professional)
        print(f'{professional} adcionado.')

    def book_appointment(self, customer_name, professinal_name, time):
        for customer in self.customers:
            if customer_name == customer.name:
                for professional in self.professionals:
                    if professinal_name == professional.name:
                        if time in professional.avaliable_times:
                            print(
                                f'Horário agendado: \n'
                                f'{customer_name} agendado para as {time}hrs, com {professinal_name}'
                                )
                            professional.avaliable_times.remove(time)

                            self.appointments.append({
                                "customer": customer_name,
                                "professional": professinal_name,
                                "time": time
                            })
                            return
        print('Erro: verifique as informações de entrada!')

    def check_availability(self):
        print("Horários disponíveis:")
        for professional in self.professionals:
            print(f"Profissional: {professional.name} | Especialidade: {professional.specialty}")
            if professional.avaliable_times:
                print("Horários disponíveis:", ", ".join(map(str, professional.avaliable_times)))
            else:
                print("Sem horários disponíveis no momento.")
                
    def cancel_appointment(self, customer_name, professional_name, time):
        for appointment in self.appointments:
            if (
                appointment['customer'] == customer_name and
                appointment['professional'] == professional_name and
                appointment['time'] == time
            ):
                self.appointments.remove(appointment)

        for professional in self.professionals:
            if professional.name == professional_name:
                professional.avaliable_times.append(time)
                response = json.dumps({'status': 'cancel',
                                        'appointment':  { 
                                            'customer': customer_name,
                                            'professional': professional_name,
                                            'time': time
                                            }
                                          })
                return response

        return json.dumps({'error': 'agendamento nao encontrado'})

cl = Customer('Danilo', '(79) 9 9999-9999', db_path='database/customs.db')

cl.create_customer_table()
cl.add_customer()
print(cl.get_customers())
cl.close_db()

pf = Professional('Matheus', 'Barbeiro', db_path='database/professionals.db')

pf.create_professional_table()
pf.add_professional()
print(pf.get_professionals())
pf.close_db