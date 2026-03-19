class Ride:
    def __init__(self, user, distance):
        self.user = user
        self.__distance = distance #private used for encapsulation
    def get_distance(self):
        return self.__distance
    def set_distance(self, distance):
        if distance > 0:
            self.__distance = distance

r= Ride("bikii", 4)
print(f"the distance for {r.user} is {r.get_distance()}")

