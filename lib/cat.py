#✅ 5. Import the pet and cat class to use in debug.py
#✅ 6. See pet.py



#✅ 7. Create a subclass of Pet called Cat
#✅ 7a. Import Pet from lib.pet
import ipdb
from lib.pet import Pet 

class Cat(Pet):
    #✅ 7b. Create an __init__ method that has all parameters of Pet including an additional parameter: indoor
    def __init__(self, name, age, breed, temperament, image_url, indoor):
        # self.name = name 
        # self.age = age 
        # self.breed = breed
        # self.temperament = temperament
        # self.image_url = image_url

        #✅ 7c. Use super to pass Pet parameters to super class
        super().__init__(name, age, breed, temperament, image_url)
        self.indoor = indoor

        #✅ 7d. Update the instance in debug.py to rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)


    #✅ 8. Create a method unique to the Cat subclass called talk which returns the string "Meowwwwwww"
    def say_meow(self):
        print("Meow!")
        #🛑 show how say_meow only works for Cats and not for Pets

    #✅ 9. Create a method called print_pet_details, to match the print_pet_details in Pet    
    def print_pet_details(self):
        super().print_pet_details()
        #✅ 9a. Print the indoor attribute
        print(f'''
            indoor: {self.indoor}
        ''')

#🛑 decorators: application value is reducing redundancy within classes
#🛑 inheritance: application value is reducing redundancy across classes
