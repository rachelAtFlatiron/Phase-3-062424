#!/usr/bin/env python3

import ipdb; 
import datetime;
#✅ 1. Create a Pet class/blueprint
class Pet:

    #all classes have a built-in __init__ method that is super barebones
    #here we are overwriting the built in __init__ method to include additional attributes including name, age, breed
    def __init__(self, new_name, new_age, new_breed):
        # to update: instance.name = "example"
        self.name = new_name 
        self.age = new_age 
        self.breed = new_breed 
    
    #✅ 4. Demonstrate INSTANCE methods
    def say_hello(self, weekday):
        print(f"Hi! My name is {self.name}.  Today is {weekday}")

    def __repr__(self):
        return (f"<Pet name={self.name} age={self.age} breed={self.breed} />")

class Owner:
   
    def __init__(self, name, age):
       self.name = name 
       #calling the setter property method to invoke set_age()
       self.age = age 

    def say_hello(self):
        print(f'Hi my name is {self.name} I am {self.age} yrs old')

    #constraints for our attributes 
    #we will be creating properties
    #property has a set and get method
    
    #def get_age
    # def get_age(self):
    #     print('...getting age')
    #     return self._age 
    
    # #def set_age
    # def set_age(self, new_age):
    #     print('...setting age')
    #     if(new_age >= 16):
    #         #this is setting/creating the private attribute
    #         self._age = new_age
    #     else:
    #         print("you must be over 16")

    # age = property(get_age, set_age)

    #@property 
    #def age
    #@age.getter 
    #@age.setter 
    #def age 
    @property 
    def age(self):
        return self._age 
    @age.getter 
    def age(self):
        print('...getting')
        return self._age 
    @age.setter 
    def age(self, new_age):
        print('...setting age')
        if(new_age >= 16):
            #this is setting/creating the private attribute
            self._age = new_age
        else:
            raise ValueError('age must be 16 or over')
        
class Appointment:
    def __init__(self, new_time, new_pet, new_service):
        self.time = new_time 
        self.pet = new_pet 
        self.service = new_service 

    def print_receipt(self):
        self.pet.say_hello("Tuesday")
        return f'{self.pet.name} has an appointment at {self.time} for a {self.service}'
    
    @property 
    def pet(self):
        return self._pet 
    @pet.setter 
    def pet(self, new_pet):
        if(type(new_pet) == Pet):
            self._pet = new_pet
        else:
            raise ValueError('pet needs to be an instance of class Pet')

    def __repr__(self):
        return f'<Appointment time={self.time} pet={self.pet} service={self.service} />'
    


#creating instances
lassie = Pet(new_breed="collie", new_age=2, new_name="lassie")
lady = Pet(new_breed="domestic", new_age=1, new_name="lady")
courage = Pet(new_age=1000, new_breed="cowardly", new_name="courage")

guy = Owner(age=50, name="guy")
penelope = Owner(age=16, name="penelope")
jessie = Owner(age=20, name="jessie")

app_one = Appointment(new_time="3pm", new_service="dental", new_pet=lassie)

pets = [
    Pet("Buddy", 2, "Golden Retriever"),
    Pet("Mittens", 3, "Siamese"),
    Pet("Rex", 5, "German Shepherd"),
    Pet("Whiskers", 1, "Maine Coon"),
    Pet("Charlie", 4, "Beagle"),
    Pet("Bella", 6, "Poodle"),
    Pet("Lucy", 2, "Bulldog"),
    Pet("Max", 7, "Rottweiler"),
    Pet("Oliver", 8, "Sphynx"),
    Pet("Daisy", 3, "Dachshund"),
    Pet("Luna", 4, "Australian Shepherd"),
    Pet("Rocky", 5, "Boxer"),
    Pet("Chloe", 2, "Cocker Spaniel"),
    Pet("Milo", 1, "Pug"),
    Pet("Zoe", 6, "Shih Tzu"),
    Pet("Toby", 3, "Schnauzer"),
    Pet("Sophie", 8, "Bichon Frise"),
    Pet("Ginger", 4, "Scottish Terrier"),
    Pet("Jack", 7, "Pomeranian"),
    Pet("Maggie", 2, "French Bulldog"),
    Pet("Sammy", 5, "Shetland Sheepdog")
]

for pet in pets:
    print(pet.name)
ipdb.set_trace()