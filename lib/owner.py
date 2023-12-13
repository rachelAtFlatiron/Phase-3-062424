# Stretch Goal: Build Out Corresponding Owner Class Methods

class Owner:
    all = []
    def __init__(self, name, phone, email):
        self.name = name 
        self.phone = phone 
        self.email = email 

    #✅ 3. create relationship: owner has many pets

    def __repr__(self):
        return f'''<Owner {self.name} >'''
    
    #✅ 9. create a function for the total bill of the owner
    #✅ 9a. create helper method for all appointments of owner (owner has many appointments through pets)
    

    