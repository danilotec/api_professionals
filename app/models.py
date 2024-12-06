from packages import Customer, Professional

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