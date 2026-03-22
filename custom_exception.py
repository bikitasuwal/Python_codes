#custom  exception
#user defined exception to handle the error and provide more usability and flexibilty

def withdraw(balance, amount):
    return balance - amount
class InsufficientBalanceErr(Exception):
    pass
def withdraw(balance, amount):
    if balance < amount:
        raise InsufficientBalanceErr("insufficient balance")
    return balance - amount

print(withdraw(100,10))