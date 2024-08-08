class Appointment:
    #class attribute to have all instances of appointment
    all = []

    def __init__(self, staff, pet, procedure):
        self.staff = staff 
        self.pet = pet #appointment belongs to pet
        self.procedure = procedure
        Appointment.all.append(self)

    #✅ 7. Create a function that prints details for the appointment 
    def print_details(self):
        return f'''
            {self.pet.name} has an appointment with {self.staff} for a {self.procedure.name}.  The final price of ${self.procedure.price} will be billed to {self.pet.owner.name}.  We will reach {self.pet.owner.name} at {self.pet.owner.email} and {self.pet.owner.phone}.
        '''
    
    @classmethod 
    #unique clients are not specific to an appointment, so it makes more sense as a class method
    #access using Appointment.unique_clients()
    def unique_clients(cls):
        # loop through all the pet's and save their owners
        clients = [app.pet.owner for app in cls.all]
        # convert clients list to set (to remove duplicates) and back into a list (because I want to return a list data type, not a set)
        return list(set(clients))


    def __repr__(self):
        return f'''<Appointment for {self.pet.name} by {self.staff}>'''
    