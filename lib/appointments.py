#🛑 will cause a circular import since Appointment has been imported in owner
#from owner import Owner 
from procedure import Procedure
#join table between pets and procedures
class Appointment:
    all = []
    #✅ 4. create relationship: appointment belongs to a pet
    #✅ 4a. use chatGPT to create instances
    #💡 Do you see any redundant info that can be factored out into a single source of truth? - request
    # def __init__(self, staff, pet, request):
    def __init__(self, staff, pet, procedure):
        self.staff = staff 
        self.pet = pet 
        # self.request = request 
        self.procedure = procedure
        Appointment.all.append(self)

    #✅ 7. Create a function that prints details for the appointment 
    def print_diagnostics(self):
        print(f'''
                {self.pet.print_pet_details()} has an appointment with {self.staff} for a {self.procedure.name}
                ''')
        
    #✅ 8. Create a class method for all unique clients of the clinic
    @classmethod
    def clients(cls):
        all_clients = []
        for app in Appointment.all: 
            all_clients.append(app.pet.owner.name)
        return list(set(all_clients))
    
    def __repr__(self):
        return f'''<Appointment for {self.pet.name}: {self.procedure.name}>'''
    