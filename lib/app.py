#!/usr/bin/env python3q
import ipdb 

# NOTE: snake_case instead of camelCase
pet_name = "Merv"
pet_mood = "Bagagwa"

# if(pet_mood === "Sad"){ }


# condition ? trueVal : falseVal
# trueVal if condition else falseVal
print(f"{pet_name} is vroom") if pet_mood=="Bagagwa" else print(f"{pet_name} is fine")

def say_hello():
    print("Hello world")

def pet_status(name, mood):
    ipdb.set_trace()
    if mood == "Sad":
        print(f"{name} is big sad")
    elif mood == "Bagagwa":
        print(f"{name} go vroom")
    else:
        print(f"{name} is {mood}")
# pet_status("merv", "bagagwa")
# pet_status("momo", "annoyed")

#✅ 6. Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"
def pet_bday(age):
    if type(age) is str:
        raise TypeError("age cannot be str")
    elif type(age) is float:
        raise TypeError("age cannot be float")
    else:
        new_age = age + 1
        print(f"momo is {new_age}")

    #try adding one and returning 
    # try:
    #     age = age + 1
    #     print(f"momo is {age}")
    # #two incompatible data types
    # except TypeError:
    #     print("age must be integer")
    # #a variable name was not recognized 
    # except NameError:
    #     print("name error occured")
    
ipdb.set_trace()