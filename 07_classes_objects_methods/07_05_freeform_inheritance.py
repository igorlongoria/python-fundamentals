'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

# class IgorMexicanFood:
#     def __init__(self, name, cook_time):
#         self.name = name
#         self.cook_time = cook_time
#
#     def __str__ (self):
#         return f'Cooking {self.name} will take you approximately {self.cook_time}.'
#
# class Ingredients:
#     def __init__(self, ing_1 = "", ing_2 = "", ing_3 = "", ing_4 = "", ing_5 = "", ing_6 = "", total):
#         self.ing_1 = ing_1
#         self.ing_2 = ing_2
#         self.ing_2 = ing_4
#         self.ing_3 = ing_3
#         self.ing_4 = ing_4
#         self.ing_5 = ing_5
#         self.ing_6 = ing_6
#         self.total =
#         print(f"The ingredients for {self.name} are {self.total}")
#
#     def plate(self):
#         if self.name == 'arroz rojo':
#             print(f"To make {self.name}, you only need ")
#
# arroz_rojo = IgorMexicanFood("arroz rojo", "30 minutes")
# pollo_mole = IgorMexicanFood("pollo con mole", "40 minutes")
# ar = Ingredients("rice", "onion")
# print(arroz_rojo)
# print(pollo_mole)
# print(ar)

class MexicanFood:
    def __init__(self, name, cooking_time):
        self.name = name
        self.cooking_time = cooking_time

    def __str__(self):
        return f"Cooking {self.name} takes approximately {self.cooking_time}."

    def notmexican(self):
        """"Explains the plate is not Mexican Food"""
        print(f"{self.name.capitalize()} is not a typical Mexican dish. It's not in the menu.")

class Beef(MexicanFood):
    def __init__(self, name, cooking_time, ingredients = []):
        super().__init__(name, cooking_time)
        self.ingredients = ingredients
        for i in self.ingredients:
            self.ingredients = i
            if self.name == "fajita tacos":
                print(f"You need {self.ingredients} to cook {self.name}.")
            if self.name == "picadillo":
                print(f"You need {self.ingredients}, to cook {self.name}")

fajita_tacos = Beef("fajita tacos", "45 minutes", "beef, ", "salt, ", "pepper, ", "bacon, ", "tortillas ")
picadillo = Beef("picadillo", "30 minutes", "ground beef, ", "tomato, ", "onion, ", "garlic, ", "salt, ", "pepper")
hot_dog = MexicanFood("hot dog", "5 minutes")

print(fajita_tacos)
print(picadillo)
print(hot_dog)
hot_dog.notmexican()