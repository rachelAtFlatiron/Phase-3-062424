# ✅ 5. Use procedure 
# ✅ 5a. Use chatGPT to create some procedures
# ✅ 5b. Update appointments.py to use procedures
class Procedure:
    def __init__(self, name, price):
        self.name = name 
        self.price = price

    def __repr__(self):
        return f'''<Procedure {self.name} is ${self.price}'''

