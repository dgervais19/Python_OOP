# Creating a snake class as child class of Reptile

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    def use_tongue_to_smell(self):
        return "I use tongue to taste"


snake_object = Snake()

print(snake_object.limbs)
print(snake_object.breathe())

# We have double inheritance