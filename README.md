Essa é uma API para gerenciamento de serviços.

A ideia é facilitar a criação de um app de barbearia, manicure, salao de beleza ou qualquer outro tipo de serviço que nescessite de agendamento.

*Ate o momento, temos 5 endpoints:

    '/' -> Da as boas vindas a API.

    '/add_customer' -> serve para adicionar um novo cliente.
        como faço isso: 
            Com um json da seguinte forma: {"name": "nome do cliente", "phone": "(99) 9 9999-9999"}
            no momento a API não faz tratamento desses dados, o usuario da api deve valida-los antes de usar a API.

    '/get_customers' -> retorna uma lista de listas contendo os dados dos clientes.

    '/add_professional' -> Serve para adcionar um novo profissional.
        como faço isso: 
            Com um json da seguinte forma: {"name": "nome do profissional", "specialty": "Manicure"}
            no momento a API não faz tratamento desses dados, o usuario da api deve valida-los antes de usar a API.

    '/get_professionals' -> retorna uma lista de listas contendo os dados dos profissionais.