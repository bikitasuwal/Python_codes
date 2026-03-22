#raising exception
#user defined exception to handle the error and provide more usability and flexibilty

def withdraw(balance, amount):
    if amount > balance:
        raise Exception("you cannot withdraw more than you have")
    return balance - amount

print(withdraw(100, 1000))
