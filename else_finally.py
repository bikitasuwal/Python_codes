#else and finally
#what is finaaly
#what is try and except
#how else is used in exception handling

try:
    num = int(input("Enter a number: "))
    print(10/num)
except ValueError:
    print("invalid number")
else:
    print("ok",num)
finally:
    print("this always runs")
