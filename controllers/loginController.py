from controllers import registerController

def login(email, password):
    users = registerController.users
    for user in users:
        if user['email'] == username and user['password'] == password:
            return 'Logged in successfully'
    return 'Invalid username or password'