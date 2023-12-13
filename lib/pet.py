#!/usr/bin/env python3
# Class Attributes and Methods 
import ipdb
#✅ 5. Import the pet and cat class to use in debug.py
class Pet:
    #✅ 6. Keep track of the total number of Pets created
    #✅ 6a. Create a class attribute

    total_pets = 0

    def __init__(self, name, age, breed, temperament, image_url):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        #✅ 6b. Update class attribute whenever an instance is initialized
        #Pet.total_pets += 1

        #✅ 6c. Create a class method increase_pets that will increment total_pets
        Pet.increase_pets()
    
    #🛑 using property for name 
    # def get_name(self):
    #     return self._name 
    # def set_name(self, name):
    #     if(isinstance(name, str)):
    #         self._name = name 
    #     else: 
    #         raise ValueError("name must be a string")
    # name = property(get_name, set_name) 

    #🛑using decorator for name 
    @property
    def name(self):
        return self._name 
    @name.setter 
    def name(self, name):
        if(isinstance(name, str)):
            self._name = name 
        else: 
            raise ValueError("name must be a string")



    #🛑 decorator for class methods
    @classmethod 
    #🛑 cls refers to Pet class, analogous to 'self' but for the whole class
    def increase_pets(cls):
        cls.total_pets += 1

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
        ''')


