def greet():
  print("hello biki")
greet()

def greetwithparam(name):
  print("hello"+name)
greetwithparam("bikita")

def sub(a,b):
  return a-b
res = sub(5,2)
print("subtraction is ", res)

#file handling in python
#file = open("example.txt", "w")  # opening a file in write mode
#file.write("Hello, this is an example of file handling in Python.")  # writing to the file
#file.close()  # closing the file
'''
w write mode - if the file does not exist, it will be created. If it already exists, it will be overwritten.
r read mode - if the file does not exist, it will raise an error. If it exists, it will be opened for reading.
a append mode - if the file does not exist, it will be created. If it already exists, new data will be added to the end of the file without overwriting the existing content.
'''


#save data to a file
def saveData():
  file=open("userdata.txt","a")
  for i in range(3):
    name= input("enter your name")
    age= input("enter your age")
    file.write(f"Name:{name}, Age:{age}\n")
  file.close()

saveData()

def readData():
  file = open("userdata.txt","r")
  data = file.read()
  print("user data\n", data)
  file.close()

readData()
