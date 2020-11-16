'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_rectangle(self):
        self.area = self.length * self.width
        return f"The area of the rectangle is {self.area}"

    def perimeter_rectangle(self):
        self.perimeter = 2 * self.length + 2 * self.width
        return f"The perimeter of the rectangle is {self.perimeter}"

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 0
        self.circumference = 0
    def area_circle(self):
        self.area = 3.14 * (self.radius * self.radius)

    def circumference_circle(self):
        self.circumference = 2 * 3.14 * self.radius


my_rectangle = Rectangle(20, 40)
my_rectangle.area_rectangle()
my_rectangle.perimeter_rectangle()
print(my_rectangle.area)
print(my_rectangle.area_rectangle())
print(my_rectangle.perimeter)
print(my_rectangle.perimeter_rectangle())

my_circle = Circle(5)

my_circle.area_circle()
print(my_circle.area)
my_circle.circumference_circle()
print(my_circle.area)
print(my_circle.circumference)