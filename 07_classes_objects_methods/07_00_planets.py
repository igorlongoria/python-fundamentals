'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet:

    def __init__(self, name, color, place_in_solar_sys):
        self.name = name
        self.color = color
        self.place_in_solar_sys = place_in_solar_sys

    def __str__(self):
        return f"{self.name} is a {self.color} planet and it's the {self.place_in_solar_sys} planet in the solar system."

planet_1 = Planet('Mercury', 'Red', 'first')
planet_2 = Planet('Venus', 'Blue', 'second')
planet_3 = Planet('Earth', 'Blue', 'third')

print(planet_1)
print(planet_2)
print(planet_3)



