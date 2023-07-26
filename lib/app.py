#!/usr/bin/env python3
#🛑 Review With Students:
    # Python environment set up: pipenv install, pipenv shell
    # Make sure the versions are aligned (with Pipfile)
    #🛑 Python => ipdb.set_trace(), JS => debugger
    # Pipfile.lock => package.lock.json
	# Python debugging tools (inside terminal as opposed to browser)
	# Python datatypes 

#🛑 To enable ipdb debugging, first import "ipdb" (included in pipfile)
#🛑 can override previously set values / test different outcomes
import ipdb #🛑 hit c to continue

#🛑 Python => snake_case, JS => camelCase
#🛑 Python => cannot declare vars without assignment, JS => can declare vars without assignment (test in python shell)
#🛑 Python => True, JS => true
#🛑 Python => ==, JS => === (compares data types), note: isInstance
#🛑 check type of string: type("Hungry!"), etc. to see its an INSTANCE of CLASS str
#🛑 check difference between 2.0, 2
pet_mood = "Hungry!"
pet_name = "Rose"

#✅ 1. Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

#🛑 have them write it in javascript first?
if pet_mood == "Hungry!":
    print(f"{pet_name} needs to be fed.")
elif pet_mood == "Rowdy!":
    print(f"{pet_name} needs a walk.")
#elif: ...
#elif: ...
#elif: ...
else:
    print(f"{pet_name} is all good.")

#✅ 2. Create a ternary operator using "pet_mood" as a condition:
#🛑 JS => condition ? "If true" : "If false"
#🛑 Python => "If true" if "Condition" else "Default"
#🛑 JS => `${interpolate}`, Python => f"{interpolate}"
print(f"{pet_name} needs to be fed.") if pet_mood == "Hungry!" else print(f"{pet_name} is all good.")

#✅ 3. Create a function (say_hello) that returns the string "Hello, world!"
#🛑 JS => function, Python => def
def say_hello():
    return "Hello, world!"

#🛑 JS => can invoke fxns with params without args, Python => cannot invoke fxns with params w/o args (unless there's a default)
def say_hello_param(param):
    return "Hello, world!"
say_hello_param() #throws error on python app.py

#🛑 note default param
def say_hello_param_def(param = "Default"):
    return "Hello, world" 
say_hello_param_def()
say_hello_param_def("Rachel")


#✅ 4. Create a function (pet_greeting) that will return a string with interpolated pet's name
#💡 Will this affect pet_name in pet_greeting?
pet_name = "Bud" #🛑 no - this is global scope
def pet_greeting(pet_name): #🛑 pet_name is in function scope
    #global pet_name #🛑 this will override the previous declaration of pet_name
    return f"{pet_name} says hello!" 
pet_greeting("Momo")
#🛑 try and come up with some other errors

#✅ 5. Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
def pet_status(pet_name, pet_mood):
    if pet_mood == "Hungry!":
        return f"{pet_name} needs to be fed."
    elif pet_mood == "Rowdy!":
        return f"{pet_name} needs a walk."
    else:
        return f"{pet_name} is all good."
#pet_status("Rose", "Hungry!")
#pet_status("Rose", "Rowdy!")
#pet_status("Rose", "Sleepy!")

#✅ 6. Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"
#🛑 show python exceptions documentation
def pet_birthday(age):
    #🛑 view error received with this first
    #f"Happy Birthday! Your pet is now {age + 1}"
    try:
        new_age = age + 1
        return f"Happy Birthday! Your pet is now {new_age}"
    except TypeError: 
        print("Type Error Occurred")
    except NameError: #example of multiple excepts
        print("Name Error Occurred")
pet_birthday("10") #type error

#🛑 To create an ipdb breakpoint, comment / uncomment line below:
ipdb.set_trace()


