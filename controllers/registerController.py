# Descrição: controladora de cadastro, responsável por cadastrar, editar e excluir usuários.
# Lista de usuários
users = []

# Funções de cadastro
def register(username, email, password):
    # Verifica se o email já existe na lista de usuários
    if (email in [user['email'] for user in users]):
        # Caso exista, retorna uma mensagem de erro
        return {'confirm': False, 'error': 'Email already exists'}
    # Caso não exista, adiciona o usuário na lista de usuários
    else:
        users.append({
            'username': username,
            'email': email,
            'password': password
            })
        # Retorna uma mensagem de sucesso
        return {'confirm': True, 'message': 'Registered successfully'}

# Funções de edição de cadastro
def update(username, email, password):
    # Percorre a lista de usuários
    for user in users:
        # Verifica se o email da requisição é igual ao email do usuário na lista de usuários
        if user['email'] == email:
            # Caso sejam iguais, atualiza os dados do usuário
            user['username'] = username
            user['password'] = password
            # Retorna uma mensagem de sucesso
            return {'confirm': True, 'message': 'Updated successfully'}
    # Caso não sejam iguais, retorna uma mensagem de erro
    return {'confirm': False, 'error': 'User not found'}

# Funções de exclusão de cadastro
def delete(email, password):
    # Percorre a lista de usuários
    for user in users:
        # Verifica se o email e a senha da requisição são iguais 
        # aos dados do usuário na lista de usuários
        if user['email'] == email and user['password'] == password:
            # Caso sejam iguais, remove o usuário da lista de usuários
            users.remove(user)
            # Retorna uma mensagem de sucesso
            return {'confirm': True, 'message': 'Deleted successfully'}
    # Caso não sejam iguais, retorna uma mensagem de erro
    return {'confirm': False, 'error': 'User not found or password is incorrect'}