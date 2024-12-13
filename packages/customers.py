from packages.database_manager import DatabaseManager
import json

class Customer(DatabaseManager):
    
    def __init__(self, db_path, name=None, phone=None):
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
        verify = self.verify_in_database(value=self.name, value2=self.phone, table='customers', column='name', column2='phone')
        if not verify: 
            query = "INSERT INTO customers (name, phone) VALUES (?,?)"
            self.execute_query(query, (self.name, self.phone))
            super().close_db()
            return json.dumps({'message': 'Customer added successfully'}), 201
        return json.dumps({'message': 'customer allredy exits'}), 409
    
    def get_customers(self):
        return self.execute_query("SELECT * FROM customers")
    