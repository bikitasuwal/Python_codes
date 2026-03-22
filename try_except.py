#exception handling in python
#sytax error -wrong code
#runtime error - during program executon
#basic try except
#only test during development not during production
#during production the value must be analysed at initial point

try:
    num = int(input("Please enter a number: "))
    print(10/num)
except:
    print("invalid input")


try:
    num1 = int(input("Please enter a number1: "))
    print(10/num1)
except ZeroDivisionError:
    print("you cant divide by zero")
except ValueError:
    print("invalid input")