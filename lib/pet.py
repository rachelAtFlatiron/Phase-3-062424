#!/usr/bin/env python3
# Class Attributes and Methods 
import ipdb
from appointments import Appointment
class Pet:

    #class attribute for all pets
    #when the class first loads, no instances have been created yet, therefore all is empty
    all = []
    def __init__(self, name, age, breed, owner=None):
        self.name = name
        self.age = age
        self.breed = breed
        # this creates our pet belongs to owner relationship
        self.owner = owner 
        # list of all existing pets 
        Pet.all.append(self)

    #✅ 5. create relationship: pet has many appointments

    def appointments(self):
        #import Appointment 
        #all appointments
        # this_pets_apps = []
        # for app in Appointment.all:
        #     #if appointment.pet == self
        #     if(app.pet == self):
        #         this_pets_apps.append(app)
        # return this_pets_apps
        return [app for app in Appointment.all if(app.pet == self)]


    #✅ 6. create relationship: pet has many procedures (but make it unique)
    # [<Procedure Check-up>, <Procedure Dental>, <Procedure Flea>]
    # Pet.appointment.procedure
    def procedures(self):
        # procs = []
        # for app in self.appointments():
        #     procs.append(app.procedure)
        # return list(set(procs))
        return [app.procedure for app in self.appointments()]

    def print_pet_details(self):
        return(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
        ''')
    
    def message(self):
        if(self.owner):
            return(f'Dear {self.owner.name}, your pet {self.name} is ready for pickup.  Please confirm the correct phone number {self.owner.phone}.')
        else: 
            return(f'Put {self.name} up for adoption.')


    def __repr__(self):
        return f'''<Pet {self.name} >'''