class Appointment:

    #✅ 4. create relationship: appointment belongs to a pet
    #✅ 4a. use chatGPT to create instances
    def __init__(self, staff, pet, request):
        self.staff = staff 
        self.pet = pet 
        self.request = request

    #✅ 7. Create a function that prints details for the appointment 
        
    #✅ 8. Create a class method for all unique clients of the clinic

    def __repr__(self):
        return f'''<Appointment request={self.request} >'''
    