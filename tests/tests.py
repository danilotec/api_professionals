from app.models import *

nome_cliente = 'Danilo'
tel_cliente = '79 9999999999'



marcar_horario_profissional = 'matheus'


cliente = Customer(nome_cliente, tel_cliente)
barbeiro = Professional('matheus', 'cortes')
hor = Schedule()

hor.add_customer(cliente)
barbeiro.book_time('18')
barbeiro.book_time('19')
hor.add_professinal(barbeiro)

hor.book_appointment(nome_cliente, marcar_horario_profissional, '18')

hor.check_availability()

print(hor.cancel_appointment('jose', marcar_horario_profissional, 17))

hor.check_availability()