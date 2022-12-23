users = []

def register(username, email, password):
    users.append({
        'username': username,
        'email': email,
        'password': password
        })
    return {'users': users}