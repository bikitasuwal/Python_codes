class Restaurant:
    #class variable
    menu = {
        "pizza": 500,
        "burger": 600,
        "pasta": 400,
        "salad": 300,
    }
    def __init__(self, customer_name):
        #object attributes
        self.customer_name = customer_name
        self.order = [] #k order garyo
        self.order_summary = {} #kati ota garyo
        self.discount = 0
    #order process for customer
    def place_order(self, item, quantity):
        if item in Restaurant.menu:
            price = Restaurant.menu[item] * quantity
            order = (item, quantity, price)
            self.order.append(order)
            #update dictionary
            self.order_summary[item] = order = self.order_summary.get(item, 0)+quantity
            print(f"{self.customer_name} ordered{quantity} X {item}")
            print("order placed successfully")
        else:
            print(f"sorry {item} is not available in the menu")

    #apply discount
    def apply_discount(self, percent):
        self.discount = percent
        print(f"A discount of {percent}% has been applied for {self.customer_name}")

    #calculate the bill
    def calculate_total(self):
        total_func =  lambda order : order [2] #lambda func to get price
        total = sum(total_func(order) for order in self.order)
        if self.discount>0:
            total = total - (total * self.discount/100)
        return total

    #unique items ordered using set
    def unique_items_ordered(self):
        return set(item[0] for item in self.order)

    #show order summary
    def show_summary(self):
        print("\n------ Order Summary for", self.customer_name, "------")
        print("Item-wise quantity (dictionary):", self.order_summary)
        print("Unique items ordered (set):", self.unique_items_ordered())
        print("Discount applied:", self.discount, "%")
        print("Total bill after discount:", self.calculate_total(), "INR")
        print("--------------------------------------\n")

# Create customers
customer1 = Restaurant("Bikita")
customer2 = Restaurant("biki")

# Place orders
customer1.place_order("pizza", 2)
customer1.place_order("salad", 4)
customer1.apply_discount(10)  # Apply 10% discount

customer2.place_order("burger", 2)
customer2.place_order("pasta", 1)
customer2.apply_discount(5)   # Apply 5% discount

# Show summaries
customer1.show_summary()
customer2.show_summary()

