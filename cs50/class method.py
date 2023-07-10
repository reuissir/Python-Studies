# class method
# implement sorting hat that tells you what house you should be in
import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)

# instantiating object of class
Hat.sort("Harry")