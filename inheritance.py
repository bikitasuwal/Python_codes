class Ride:
    def __init__(self, user, distance):
        self.user = user
        self.distance = distance
    def fare(self):
        print(f"{self.user} fare is {self.distance}")

class BikeRide(Ride):
    def __init__(self, user, distance):
        super().__init__(user, distance)
    def fare(self):
        print("this is bike fare", self.distance*50)

class CarRide(Ride):
    def __init__(self, user, distance):
        super().__init__(user, distance)
    def fare(self):
        print("this is car fare", self.distance*100)

r1 = BikeRide("bikita", 10)
r1.fare()
r2= CarRide("biki", 20)
r2.fare()