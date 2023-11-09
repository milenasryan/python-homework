import vehicle

class Car(vehicle.Vehicle):
    def __init__(self, weight, speed):
        super().__init__(weight)
        self.speed = speed

    def move(self):
        print("A car is in motion.")

class Plane(vehicle.Vehicle):
    def __init__(self, weight, speed, engineCount):
        super().__init__(weight)
        self.speed = speed
        self.engineCount = engineCount

    def move(self):
        print("A plane is flying.")

class Boat(vehicle.Vehicle):
    def __init__(self, weight, speed, maxLoad):
        super().__init__(weight)
        self.speed = speed
        self.maxLoad = maxLoad

    def move(self):
        print("A boat is sailing.")

class RaceCar(Car):
    def __init__(self, weight, speed, horsePower):
        super().__init__(weight, speed)
        self.horsePower = horsePower

    def move(self):
        print("A race car is accelerating.")

    def __str__(self):
        return f"A high-performance racecar with weight - {self.weight}, speed - {self.speed}, and horsepower - {self.horsePower} is tearing up the track!"

myRaceCar = RaceCar(200, 300, 600)
print(myRaceCar)