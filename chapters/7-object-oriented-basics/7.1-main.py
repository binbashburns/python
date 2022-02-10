#!/usr/bin/env python3.7

### --- Object-Oriented Programming Basics --- ###

# Classes

class Car:
    # First we start with what's called a docstring. This just tells the reader about the class
    """                          
    Docstring describing the method
    """
    
    def __init__(self): # We define methods in here. Methods are functions that are inside of classes. This takes an argument that is always called self
        """
        Docstring describing the method
        """
        pass            # This is another keyword that allows us to simply say that we're not going to implement it right now
    
    
    
# Step back to __init__. This is the thing that happens when we create a new instance of something that we're working with
# __init__ and similar methods are called "Dunder" methods, or "double-under methods"
# You can automatically load the classes by going to the command line and typing:
# python3.7 -i program_name.py
# Now you can go to your REPL and type:
# my_car = Car()
# And then if we go to the REPL and type:
# my_car
# You'll see that the object has been defined and that it has a location in memory.

class Car:
    """                          
    Car models a car w/ tires and an engine
    """
    
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
        
    # Go to your REPL and type:
    # civic = Car('4-cylinder', ['front-driver','front-passenger','rear-driver','rear-passenger'])
    # And then if go to the REPL and type:
    # civic
    # You'll see that the object has been defined and that it has a location in memory. Same as before.
    # Now try "civic.engine". You should see the value stored in the engine variable
    # You can think of attributes as being variables that are localized to an individual instance of an object or class
    # You can also add more attributes like this:
    # civic.license_plate = 'something'
    # Now when you run "civic.license_plate", you'll see 'something'

    def description(self):
        print(f"A car with an {self.engine} engine, and {self.tires} tires")
        
    # Let's initialize this once more with:
    # python3.7 -i 7.1-main.py 
    # civic = Car('4-cylinder', ['front-driver','front-passenger','rear-driver','rear-passenger'])
    # civic.tires
    # civic.engine
    # Now let's try "civic.description". You should get something like this:
    # <bound method Car.description of <__main__.Car object at 0x7f9067adad68>>
    # This tells us "it's a method!" so we slap some parentheses on it, and should get a better result
    # civic.description()
    # A car with an 4-cylinder engine, and ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'] tires
    
    # Composition
    
    