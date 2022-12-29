# Descrição: controladora de login, responsável por fazer o login de usuários.
# Importando o módulo de registro
from controllers import registerController

# Usando a variável users do módulo de registro
users = registerController.users

# Função de login
def login(email, password):
    # Percorre a lista de usuários
    for user in users:
        # Verifica se os dados da requisição são iguais aos dados do usuário na lista de usuários
        if user['email'] == email and user['password'] == password:
            # Caso sejam iguais, retorna uma mensagem de sucesso
            return {'confirm': True, 'message': 'Logged in successfully'}
    # Caso não sejam iguais, retorna uma mensagem de erro
    return {'confirm': False, 'message': 'Invalid username or password'}