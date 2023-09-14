#!/usr/bin/env python3
# Class Attributes and Methods 
import ipdb
from appointments import Appointment
class Pet:

    all = []
    #✅ 1. create relationship: pet belongs to an owner
    #✅ 2. use chatGPT to create owners and pets in debug.py
    #✅ 2a. create __repr__ function to more easily read output
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner 
        Pet.all.append(self)

    #✅ 5. create relationship: pet has many appointments
    def appointments(self):
        # return [appointment.request for appointment in Appointment.all if appointment.pet == self ]
        return [appointment for appointment in Appointment.all if appointment.pet == self]
    
    #✅ 6. create relationship: pet has many procedures (but make it unique)
    #🛑 can't do vice versa in Procedure because we imported Procedure in appointments and we would get a circular import
    def procedures(self):
        return list(set([app.procedure.name for app in self.appointments()]))

    def print_pet_details(self):
        return(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
        ''')

    def __repr__(self):
        return f'''<Pet {self.name}'s owner is {self.owner.name}>'''