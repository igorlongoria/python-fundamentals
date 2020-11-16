'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''
class Movie:
    def __init__(self, year, title):
        self.year = year
        self.title = title

    def __str__(self):
        return f"The release year of {self.title} was {self.year}"

class RomCom(Movie):
    def sport(self):
        if self.title == "Fever Pitch":
            print(f"{self.title} is romantic comedy about baseball")
        else:
            print(f"I have not wathced {self.title}")

class ActionMovie(Movie):
    def __init__(self, year, title, pg = 13, actor = ""):
        super().__init__(year, title)
        self.pg = pg
        self.actor = actor
    def jackie(self):
        if self.actor == "Jackie Chan":
            print(f"{self.actor} made pg {self.pg} action movies such as {self.title}. ")


godfather = Movie(1970, "The Godfather")
fp = RomCom(2005, "Fever Pitch")
kd = ActionMovie(2010, "Karate Kid", 13, "Jackie Chan")
print(godfather)
fp.sport()
print(fp)
kd.jackie()
print(kd)