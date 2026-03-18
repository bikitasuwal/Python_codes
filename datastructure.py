#data struccture in python

#list
mylist = [1,2.98,3,"biki",True]
#accessing list
print(mylist[0])
#insert element in data 
mylist.append("added element")
print(mylist)
#insert element in list 
mylist.insert(2,"programming")
print(mylist)
#remove element from list
mylist.remove(2.98)
print(mylist)

#loop through list
for item in mylist:
    print(item)

#tuple immutable list
gpsValues = (27.1212, 85.3232)
print(gpsValues[0])

#dictionary
intro = {"name":"biki", "age": 21, "city": "bhaktapur"}
print(intro["name"])
#add element in dictionary
intro["profession"] = "student"
print(intro.get("profession"))
intro["age"] = 23
print(intro.get("age"))
#remove element from dictionary
del intro["city"]
print(intro)
intro.pop("profession")
print(intro)
#loop through dictionary
for key in intro:
    print(key, intro[key])

for key, value in intro.items():
    print(key, value)


student = {"name": "biki", "age": 21, "city": "bhaktapur"}

# .keys()  → returns all keys
print(student.keys())           # dict_keys(['name', 'age', 'city', 'grade'])

# .values()  → returns all values
print(student.values())         # dict_values(['biki', 21, 'bhaktapur', 'A'])                 

# .items()  → returns (key, value) pairs
print(student.items())
for key, value in student.items():
    print(f"{key} : {value}") 

# .get()  → safely fetch a value (no KeyError if key missing)
print(student.get("name"))      # biki
print(student.get("phone"))     # None  (key doesn't exist)
print(student.get("phone", "N/A"))  # N/A  (custom default)

# .update()  → merge / overwrite keys from another dict
student.update({"age": 22, "phone": "9800000000"})
print(student)   # age updated to 22, phone added

# .clear()  → removes all items from the dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print(temp)      

#set only unique values
print("######################### sets ")
myset = {1,2,3,4,5}
print(myset)
myset.add(6)
print(myset)
myset.remove(3)
print(myset)    

list1 = [6,7,8,9,9]
print(list1)
myset_from_list = set(list1) 
print(myset_from_list)

#list, dictionary, tuple, set
#duplicate values in list. eg - shopping list 
#indexing in list and tuple
#key value pair in dictionary , example - student data in college 
#immutable in tuple , example - gps coordinates of a place
#unique values in set example - guest list in events
