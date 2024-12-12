
import json

from packages.customers import Customer
from packages.professionals import Professional
from packages.database_manager import DatabaseManager

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