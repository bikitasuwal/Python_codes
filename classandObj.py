class FoodOrder:
    def __init__(self, name, item, price):
        self.name = name
        self.price = price
        self.item = item
    def show_order(self):
        print("Name:{}".format(self.name))
        print("Price:{}".format(self.price))

order1 = FoodOrder("biki", "pizza", 500)
order2 = FoodOrder("bikiii", "pizza", 400)
print(order1.name,order2.price)
order1.show_order()

'''inside class : only define methods and attributes
outside class : call methods, define and use objects'''

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def show_details(self):
        print("Brand:{}".format(self.brand))
        print("Price:{}".format(self.price))

laptop1 = Laptop("dell", 50000)
laptop2 = Laptop("lenovo", 50000)
laptop1.show_details()
laptop2.show_details()