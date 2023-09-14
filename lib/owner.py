# Stretch Goal: Build Out Corresponding Owner Class Methods

from pet import Pet 
from appointments import Appointment
class Owner:
    all = []
    def __init__(self, name, phone, email):
        self.name = name 
        self.phone = phone 
        self.email = email 
        Owner.all.append(self)

    #✅ 3. create relationship: owner has many pets
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def __repr__(self):
        return f'''<Owner {self.name} >'''
    
    #✅ 9. create a function for the total bill of the owner
    #✅ 9a. create helper method for all appointments of owner (owner has many appointments through pets)
    def owner_appointments(self):
        owner_apps = []
        for pet in self.pets():
            for app in Appointment.all:
                if pet == app.pet:
                    owner_apps.append(app)
        return owner_apps
    
    def total_bill(self):
        bill = 0
        for app in self.owner_appointments(): 
            bill += app.procedure.price 
        return bill


    



    def appointments(self):
        apps = []
        for i in self.pets():
            for app in Appointment.all:
                if(app.pet == i):
                    apps.append(i.name)
        return apps 


    