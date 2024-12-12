# API de Gestão de Clientes e Profissionais

Essa é uma API RESTful self-hosted para gerenciamento de serviços.

A ideia é facilitar a criação de um app de barbearia, manicure, salao de beleza ou qualquer outro tipo de serviço que nescessite de agendamento.

## Funcionalidades

- **/ (GET)** - Endpoint de boas-vindas.
- **/add_customer (POST)** - Adicionar um novo cliente.
- **/get_customers (GET)** - Obter todos os clientes cadastrados.
- **/add_professional (POST)** - Adicionar um novo profissional.
- **/add_times_professional (POST)** - Adicionar horários para um profissional específico.
- **/get_professionals (GET)** - Obter todos os profissionais cadastrados.

## Endpoints

### 1. `/` - Boas-vindas

- **Método**: `GET`
- **Descrição**: Endpoint de teste para verificar se a API está funcionando corretamente.
- **Resposta**: 
  ```json
  {
    "Access successful": "Wellcome!"
  }
  ```

### 2. `/add_customer` - Adicionar Cliente

- **Método**: `POST`
- **Descrição**: Adiciona um novo cliente com nome e telefone.
- **Requisição**: 
  ```json
  {
    "name": "Nome do Cliente",
    "phone": "Telefone do Cliente"
  }
  ```
- **Resposta**:
  - Se os dados forem válidos:
    ```json
    {
      "message": "Customer added successfully"
    }
    ```
  - Se algum valor for `None`:
    ```json
    {
      "error": "value cannot be none"
    }
    ```
- **Status Code**: `400` em caso de erro.

### 3. `/get_customers` - Obter Clientes

- **Método**: `GET`
- **Descrição**: Retorna todos os clientes cadastrados.
- **Resposta**:
  ```json
  [
    {
      "name": "Nome do Cliente",
      "phone": "Telefone do Cliente"
    },
  ]
  ```
- **Status Code**: `200`

### 4. `/add_professional` - Adicionar Profissional

- **Método**: `POST`
- **Descrição**: Adiciona um novo profissional com nome e especialidade.
- **Requisição**:
  ```json
  {
    "name": "Nome do Profissional",
    "specialty": "Especialidade"
  }
  ```
- **Resposta**:
  - Se os dados forem válidos:
    ```json
    {
      "message": "Professional added successfully"
    }
    ```
  - Se algum valor for `None`:
    ```json
    {
      "error": "value cannot be none"
    }
    ```
- **Status Code**: `400` em caso de erro.

### 5. `/add_times_professional` - Adicionar Horários para Profissional

- **Método**: `POST`
- **Descrição**: Adiciona os horários disponíveis para um profissional.
- **Requisição**:
  ```json
  {
    "id": 1,
    "times": ["09:00", "14:00", "16:00"]
  }
  ```
- **Resposta**:
  - Se os dados forem válidos:
    ```json
    {
      "message": "Times added successfully"
    }
    ```
    Se os valores não forem `int` e `list` :
    ```json
    {
      "error": "check if values are 'int' and 'list' types"
    }
    ```
  - Se algum valor for `None`:
    ```json
    {
      "error": "value cannot be none"
    }
    ```
- **Status Code**: `400` em caso de erro.

### 6. `/get_professionals` - Obter Profissionais

- **Método**: `GET`
- **Descrição**: Retorna todos os profissionais cadastrados.
- **Resposta**:
  ```json
  [
    {
      "name": "Nome do Profissional",
      "specialty": "Especialidade"
    },
  ]
  ```
- **Status Code**: `200`

## Requisitos

- Python 3.x
- Flask
- Banco de Dados SQLite (por padrão, `database/persons.db`)

## Como rodar

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o aplicativo:
   ```bash
   python run.py
   ```
4. A API estará disponível em `http://localhost:5000`.

## Autenticação

A API requer uma chave de API para acesso. A chave de API deve ser passada em cada requisição através do cabeçalho `API-Key`.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Crie um fork do repositório, faça suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
