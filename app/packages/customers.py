from packages.database_manager import DatabaseManager

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
    