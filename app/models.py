
class Customer:
    
    def __init__(self, name, phone, id):
        self.name = name
        self.phone = phone
        self.id = id
        
    def __str__(self):
        return f'Customer name: {self.name} | phone: {self.phone} | id: {self.id}'

class Professional:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.avaliable_times = []

    def book_time(self, time):
        if time not in self.avaliable_times:
            print(f'Novo horario cadastrado: {time}hrs')
            self.avaliable_times.append(time)
        else:
            print(f'O horário {time} já está disponível.')
        
    def __str__(self):
        return f'Professional: {self.name} | specialty: {self.specialty} | times: {self.avaliable_times}'

class Schedule:

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
                print(f"Agendamento para {customer_name} com {professional_name} às {time} foi cancelado.")
                return

        print('Erro: agendamento nao encontrado')


nome_cliente = input('nome do cliente: ')
tel_cliente = input('telefone do cliente: ')


marcar_horario_nome = input('Marcar horario\n Nome: ')
marcar_horario_profissional = input('Profissional: ')
# marcar_horario_hora = input('Hora: ')

cliente = Customer(nome_cliente, tel_cliente, 1)
barbeiro = Professional('matheus', 'cortes')
hor = Schedule()

hor.add_customer(cliente)
barbeiro.book_time('18')
barbeiro.book_time('19')
hor.add_professinal(barbeiro)

hor.book_appointment(marcar_horario_nome, marcar_horario_profissional, 17)

hor.check_availability()

hor.cancel_appointment(marcar_horario_nome, marcar_horario_profissional, 17)

hor.check_availability()

