from controllers import registerController

users = registerController.users

def login(email, password):
    for user in users:
        if user['email'] == email and user['password'] == password:
            return {'confirm': True, 'message': 'Logged in successfully'}
    return {'confirm': False, 'message': 'Invalid username or password'}