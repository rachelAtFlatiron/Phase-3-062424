#!/usr/bin/env python3
# Class Attributes and Methods 
import ipdb
class Pet:

    #✅ 1. create relationship: pet belongs to an owner
    #✅ 2. use chatGPT to create owners and pets in debug.py
    #✅ 2a. create __repr__ function to more easily read output
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner 

    #✅ 5. create relationship: pet has many appointments

    #✅ 6. create relationship: pet has many procedures (but make it unique)

    def print_pet_details(self):
        return(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
        ''')

    def __repr__(self):
        return f'''<Pet {self.name}'s owner is {self.owner.name}>'''