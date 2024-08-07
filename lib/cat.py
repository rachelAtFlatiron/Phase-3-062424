#✅ 7. Create a subclass of Pet called Cat
#✅ 7a. Import Pet from lib.pet
import ipdb
from pet import Pet

class Cat(Pet):
    def __init__(self, name, age=1, breed='cat', temperament='', image_url='', indoor=True):
        #invoking the super/parent class' init method
        super().__init__(name, age, breed, temperament, image_url)
        #and doing some additional stuff specific to this subclass 
        self.indoor = indoor 

    #✅ 8. Create a method unique to the Cat subclass called talk which returns the string "Meowwwwwww"
    def say_meow(self):
        return f'hiiii meow {self.name}'

    #✅ 9. Create a method called print_pet_details, to match the print_pet_details in Pet    
    def print_pet_details(self):
        print(super().print_pet_details())
        return f'indoor: {self.indoor}'
    
    def __repr__(self):
        return f'<Cat name={self.name} />'

alex = Pet(name="Alex", breed="bird")
garfield = Cat(name="Garfield")
ipdb.set_trace()

# parent class: Error, subclasses: ValueError, NameError