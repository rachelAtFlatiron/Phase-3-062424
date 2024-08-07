#!/usr/bin/env python3
# Class Attributes and Methods 
import ipdb

class Pet:
    #class attribute - create outside of init 
    #Class.attribute
    #instance.attribute
    #can still access class attributes via instances, however the class attribute values will remain the same across all instances
    total_pets = 0
    # class attribute, to store all instances of pets
    pets = []

    def __init__(self, name, age=1, breed='animal', temperament='', image_url=''):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        #update class attributes whenever a new instance is created
        Pet.increase_pets()
        #Pet.total_pets += 1
        Pet.pets.append(self)
        
    #use decorator for class methods
    @classmethod 
    def increase_pets(cls):
        cls.total_pets += 1

    def __repr__(self):
        return f'<Pet name={self.name} age={self.age} />'

    # no decorator, so its an instance method
    # instance method will give results specific to instance we are calling it on
    # class methods/attributes can be accessed by instances but the values will remain the same across all instances 
    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
            the total number of pets is currently {Pet.total_pets}
        ''')


lassie = Pet(name="lassie", age=6)
courage = Pet(name="courage", age=10000)
scooby = Pet(name="scooby", age=2)


