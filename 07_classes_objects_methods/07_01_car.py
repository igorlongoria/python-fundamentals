'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase(self, increase_speed):
        "Increases the maximum speed."
        self.max_speed += increase_speed

    def __str__(self):
        return f"This is a {self.year}, {self.model} and it goes up to {self.max_speed} mph. "

car_1 = car('Toyota Tundra', 2013, 160)

print(car_1)
car_1.increase(5) # once called it changes the input
print(car_1.max_speed)
car_2 = car('Ford Mustang', 2020, 200)
print(car_2.model)
car_2.increase(50)
print(car_2.max_speed)