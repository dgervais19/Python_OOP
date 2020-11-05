# Creating a python class as child class of our Snake class

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    # creating functions for our python class

    def digest_large_prey(self):
        return "Yum Yummy..."

    def climb(self):
        return "Up We Go"

    def shed_skin(self):
        return "Your skin is getting old. Time to shed"


python_object = Python()

# creating an object of our python class

print(python_object.breathe()) # getting an attribute from the animal class
print(python_object.hunt()) # getting an attribute from the reptile class
print(python_object.use_venom()) # getting an attribute from the snake class
print(python_object.digest_large_prey()) # getting an attribute from the python class