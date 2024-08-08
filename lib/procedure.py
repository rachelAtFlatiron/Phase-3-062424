from appointments import Appointment
# ✅ 5. Use procedure 
# ✅ 5a. Use chatGPT to create some procedures
# ✅ 5b. Update appointments.py to use procedures
class Procedure:

    def __init__(self, name, price):
        self.name = name 
        self.price = price

    # all the pets that have current procedure
    def pets(self):
        # this_procs_pets = []
        # #loop through all appointments
        # for app in Appointment.all:
        #     #filter out appointments with current procedure
        #     if(app.procedure == self):

        #         #further filter out the pets name
        #         this_procs_pets.append(app.pet)
        #     #[<Pet Max>, <Pet Rocco>, <Pet Timmy>]
        
        # return this_procs_pets
        return [app.pet for app in Appointment.all if(app.procedure == self)]



    def __repr__(self):
        return f'''<Procedure {self.name} is ${self.price} />'''

