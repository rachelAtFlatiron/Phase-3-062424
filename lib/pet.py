#!/usr/bin/env python3

#attribute - stuff in the __init__
#properties - attributes that have extra logic and use the @property decorator
# you have complete control over its getter and setter methods
# methods - functions you define within a class that operate within the values available in that instance

import ipdb; 
#✅ 1. Create a Pet class
#🛑 class is the blueprint (cookie cutter), the instances are the cookies
class Pet:
    # pass

    #✅ 2. Instantiate a few pet instances in ipdb 
    #✅ 2a. Compare the pet instances to demonstrate they are not the same object
    #🛑 different objects in memory all created from the same source (the class 'blueprint')

    #✅ 3. Demonstrate __init__ 
    #🛑 self => current instance that is being created
    #🛑 dunder (double underscore) method - builtin "magic method"
    #see all dunder methods for class with dir(int)
    #✅ 3a. Add parameters for attributes (NO OWNER YET, SEE 3D) 

    # attributes - data members of objects
    # properties - like attributes but also perform some computation
    def __init__(self, name, age, breed, temperament, image_url, owner="No Owner"):
        #✅ 3b. use dot notation to access their attributes 
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        self.owner = owner
        #✅ 3c. update attributes with new values 
        #in ipdb: fido.age = 6, fido.age = "6" 
        #🛑 need a way to do some checking when updating attributes
        #✅ 3d. add owner attribute with default value
    
    #✅ 4. Demonstrate INSTANCE methods

    #✅ 4a. Create a hello method that will print "Hello!"
    def hello(self):
        print("Hello!")

    #✅ 4b. Create a print_pet_details function that will print the pet attributes
    def print_pet_details(self):
        #💡 How do we pull out the current instance's attributes?
        #🛑 self is representative of whichever instance we are currently working with
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
        ''')


#✅ 5. Set constraints for updating properties (attributes that are controlled by methods)
class Owner:
    #✅ 5d.  Add parameter to pass in name property value on instantiation
    #🛑 init is inherent, when we write one we are overwriting the default
    def __init__(self, age, name):
        self.age = age 
        #🛑 because self.name compiled the set/get methods, it will use the set_name()
        self._name = name #imply that _name should be a private attribute


    #✅ 5a. Create get/set instance methods for name property 
    def get_name(self):
        print("Getting name...")
        return self._name 

    def set_name(self, name):
        #✅ 5b. Create constraint to make sure the name is of type string
        print("Setting name...")
        if isinstance(name, str):
            self._name = name 
            return self._name 
        else:
            print("Name must be a string")
    name = property(get_name, set_name)
    #✅ 5c. Compile get_name, set_name under the same property name
    #🛑 using the @ decorator for properties is just syntactic sugar
            
    # @property 
    # def name(self):
    #     print("getting name with decorator...")
    #     return self._name 
    # @name.getter #mostly in case you need to do other logic
    # @name.setter 
    # def name(self, name):
    #     print("setting name with decorator...")
    #     if isinstance(name, str):
    #         self._name = name 
    #     else: 
    #         print("Name must be a string")
    

    

ipdb.set_trace()