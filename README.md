Essa é uma API para gerenciamento de serviços.

A ideia é facilitar a criação de um app de barbearia, manicure, salao de beleza ou qualquer outro tipo de serviço que nescessite de agendamento.

Em 'app/models.py' teremos a logica de negócio e o controle dos agendamentos.

    A classe Customer trata de criar os clientes
        posteriomente será adcionado os methods para o gerenciamento do banco de dados dos clientes.

    A classe Professional serve para criar o profissioal no sistema e informar qual a atribuição que lhe pertence e os horarios disponiveis.
        posteriormente tambem será adcionado a integração com o banco de dados.

    A classe Schedule cuida de todo o agendamento do sistema.