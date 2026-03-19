class FoodOrder:
    def __init__(self, name, item, price):
        self.name = name
        self.price = price
        self.item = item

        order1 = FoodOrder("biki", "pizza", 500)
        order2 = FoodOrder("bikiii", "pizza", 400)