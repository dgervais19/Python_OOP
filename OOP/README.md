# This class will cover OOP in python

### Step 1
* create an Animal class as our Parent
```
# Creating an Animal class as PARENT/BASE/SUPER class

class Animal:

    def __init__(self):  # initialising the Animal class
        self.alive = True  # creating an attribute/variable
        self.spine = True
        self.lungs = True
        self.eyes = True


    # create behaviours as functions/methods
    def breathe(self):
        return  "Keep breathing to stay alive "

    def move(self):
        return "left to right and up and down...."

    def eat(self):
        return "Nom Nom Nom"

    def procreate(self):
        return "find partner"

# instantiate our class/ create and object

cat = Animal() # creaeting an object of Animal class

# cat as child has inherited everything from animal
print(cat.eat())
```

### Step 2
* create Reptile class as the child class
* Why? so we can Inherit from our parent
* Abstract

```
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

# Lets also see if we can still print the inherited attributes from the parent class
print(reptile_object.eat())
print(reptile_object.breathe())
print(reptile_object.procreate())

# Now lets look at the attributes from the current class
print(reptile_object.seek_heat())
print(reptile_object.hunt())
print(reptile_object.use_venom())
```


### Step 3
* create Snake class as child of reptile directly
```
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
```

### Step 4
* create a Python class

```
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
```


###  Using ``__name__`` and ``__main__``

``__name__`` and ``__main__`` are used to check if the code is run from the current file/directly or from a different file thats imported
* we will create 2 files and use ``__name__`` and ``__main__`` in both files and the outcome will show the difference.

