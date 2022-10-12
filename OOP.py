# OOP exercises

# Define basic class with two functions.

class Car:
    # This the function constructor.
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

        # These are clas functions

    def description(self):
        return f"The {self.name} has a mileage of {self.mileage}km/l."

    def car_speed(self, speed):
        return f"The {self.name} has a maximum speed of {speed}km/h."


# This is the class object.
car1 = Car("Honda", 8)

# Here I call the object functions that it inherited from its class.

print(car1.description())
print(car1.car_speed(120))

# Parent and child classes


class AnotherCar:       # A parent class

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f"A {self.name} car has a mileage of {self.mileage}km/l."


class BMW(AnotherCar):
    def bmw_description(self):
        return f"A BMW class description."

aCar = Car("Honda", 8)
bmw = BMW("BMW 7-Series", 14)

print(aCar.description())
print(bmw.description())
print(bmw.bmw_description())