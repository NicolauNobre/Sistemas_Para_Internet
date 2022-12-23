users = []

def register(username, email, password):
    if (email in [user['email'] for user in users]):
        return {'confirm': False, 'error': 'Email already exists'}
    else:
        users.append({
            'username': username,
            'email': email,
            'password': password
            })
        return {'confirg': True, 'message': 'Registered successfully'}

def update(username, email, password):
    for user in users:
        if user['email'] == email:
            user['username'] = username
            user['password'] = password
            return {'confirm': True, 'message': 'Updated successfully'}
    return {'confirm': False, 'error': 'User not found'}

def delete(email):
    for user in users:
        if user['email'] == email:
            users.remove(user)
            return {'confirm': True, 'message': 'Deleted successfully'}
    return {'confirm': False, 'error': 'User not found'}