# get access to Pet.all
from pet import Pet 

# make the assumption that no all Owners are clients
class Owner:

    def __init__(self, name, phone, email):
        self.name = name 
        self.phone = phone 
        self.email = email 

    #✅ 3. create relationship: owner has many pets
    def pets(self):
        # list comprehension to collect all the pets who's owner is self
        # if(pet.owner == self)
            #if so, we will leave pet in the list

        #create empty list for pets that belong to current owner
        # this_owners_pets = []
        #loop through all existing pets and find one's that belong to self (current owner)
        #see import at top of file for access to Pet.all
        # for cur_pet in Pet.all:
        #     #if current pet's owner is self
        #     if(cur_pet.owner == self):
        #         #add cur_pet to list of pets
        #         this_owners_pets.append(cur_pet)
        # return this_owners_pets
        return [pet for pet in Pet.all if pet.owner == self]
        
    # owner has many appointments
    def appointments(self):
        owners_appointments = []
        #loop through all ofthe owners pets
        for pet in self.pets(): 
            #for each pet save their appointments somewhere
            owners_appointments.extend(pet.appointments())
        return owners_appointments
    
    def print_appointments(self):
        # printing some details for each appointment current user has
        for app in self.appointments():
            print(f'{self.name} has a {app.procedure.name} for {app.pet.name}')

    def total_bill(self):
        total = 0
        #return the sum of all prices for all appointments 
        # owner's appointments
        for app in self.appointments():
            # appointment's procedure's price 
            total += app.procedure.price 
        return f'${total}'
    
    def __repr__(self):
        return f'''<Owner name={self.name} />'''
    
    

    