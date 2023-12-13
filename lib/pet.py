#!/usr/bin/env python3

import ipdb; 
#✅ 1. Create a Pet class
class Pet:

    #✅ 2. Instantiate a few pet instances in ipdb 
    #✅ 2a. Compare the pet instances to demonstrate they are not the same object
    #pet_one = Pet()
    #<__main__.Pet object at 0x104cd4820>

    #✅ 3. Demonstrate __init__ 
    def __init__(self, name, age, breed, owner=None):
    #✅ 3a. Add parameters for attributes 
        #✅ 3b. use dot notation to access their attributes 
        #✅ 3c. update attributes with new values 
        self.name = name 
        self.age = age 
        self.breed = breed
        self.owner = owner 
        #update attributes: pet_one.age = 1
        #momo.owner.print_owner()

        #✅ 3d. add owner attribute with default value
    
    #✅ 4. Demonstrate INSTANCE methods
    #✅ 4a. Create a hello method that will print "Hello!"
    #✅ 4b. Create a print_pet_details function that will print the pet attributes
    def print_pet(self):
        print(f''' 
            <Pet 
                name: {self.name}
                age: {self.age}
                breed: {self.breed}
                owner: {self.owner}
            />
        ''')


#✅ 5. Set constraints for updating properties (attributes that are controlled by methods)
class Owner:
    def __init__(self, name, age):
        print("instantiating...")
        self.name = name  #_ says please don't directly update this attribute (even though technically you can)
        self.age = age 
    #✅ 5d.  Add parameter to pass in name property value on instantiation

    @property 
    def name(self):
        print("getting name with decorator...")
        return self._name 
    
    @name.setter 
    def name(self, name):
        print("setting name with decorator...")
        if isinstance(name, str):
            self._name = name 
        else: 
            print("Name must be a string")
    
    # #✅ 5a. Create get/set instance methods for name property 
    # def get_name(self):
    #     print("getting...")
    #     return self._name 
    # def set_name(self, name):
    #     print("setting...")
    #     #✅ 5b. Create constraint to make sure the name is of type string
    #     if isinstance(name, str):
    #         self._name = name 
    #     else:
    #         print("Name must be a string")

    # def print_owner(self):
    #     print(f'''
    #             <Owner 
    #                 name: {self.name}
    #                 age: {self.age}
    #             />
    #           ''')
    
    # #✅ 5c. Compile get_name, set_name under the same property name
    # name = property(get_name, set_name)

ipdb.set_trace()