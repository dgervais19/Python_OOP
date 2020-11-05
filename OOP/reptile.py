# creating a reptile class as a child class of our Animal class

from animal import Animal

class Reptile(Animal):
    def __init__(self):


        super().__init__()  # Super is a keyword is used to inherit everything from a Parent Class
        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chamber = [3, 4]

    # creating function for our Reptile class
    def seek_heat(self):
        return "it's freezing, look for some warmth"

    def hunt(self):
        return "Work hard to catch a meal or go home hungry"

    def use_venom(self):
        return "Use it only when you need to"


# lets create an object of our Reptile class to utilise the amazing functionalities of OOP
reptile_object = Reptile()

# # Lets also see if we can still print the inherited attributes from the parent class
# print(reptile_object.eat())
# print(reptile_object.breathe())
# print(reptile_object.procreate())
#
# # Now lets look at the attributes from the current class
# print(reptile_object.seek_heat())
# print(reptile_object.hunt())
# print(reptile_object.use_venom())

