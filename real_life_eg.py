print("Real life Example")
def login(username, password):
    if username != 'admin':
        raise NameError('user not found')
    if password != '123':
        raise NameError('password not found')
    return "login successful"

try:
    print(login('admin', '123'))
except NameError as up:
    print(up)