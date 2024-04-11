# ✅ 9. Import all helper functions and necessary models
from helpers import (
    exit_program,
    print_owner,
    print_pet,
    helper_1,
    print_all_owners,
    print_all_pets_for_owner,
    print_all_apps_for_owner,
    print_apps_for_one_pet
)
from models.owner import Owner 
from models.pet import Pet

#enter full name 
#see my pets
#see all my appointments
#see appointments for one pet
#update user 
#make an appointment for a pet 

# ✅ 14. Create a global `owner` and `pet` value
cur_owner = None
cur_pet = None 

# ✅ 10. Create a function `main()` that will wait for a user's input 
# ✅ 15. Add the decision tree to `main`
def main():
    while True:
        choice = input(">Press enter to continue")
        menu()
        choice = input("> ")
        print(f"\n")
        if choice == "0": #exit program
            exit_program() 
        elif choice == "1": #set current owner
            print_all_owners()
            set_cur_owner()
        elif choice == "2": #see all current owner's pets
            print_all_pets_for_owner(cur_owner)
        elif choice == "3": #see all owner's appointments 
            print_all_apps_for_owner(cur_owner)
        elif choice == "4": #Select a pet
            print_all_pets_for_owner(cur_owner)
            set_cur_pet()
        elif choice == "5": #See current pet
            print_pet(cur_pet)
        elif choice == "6": #See current pet's appointments
            print_apps_for_one_pet(cur_pet)
        else:
            print("Invalid choice")
        print(f"\n")


def set_cur_owner():
    global cur_owner
    print('Enter the id of the current owner')
    cur_owner = input("> ")
    print_owner(cur_owner)
def set_cur_pet():
    global cur_pet 
    print('Enter the id of the pet')
    cur_pet = input("> ")

# ✅ 13. Create a `menu` function that displays actions a user can take
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Set the current owner")
    if(cur_owner):
        print("2. See all my pets")
        print("3. See all my appointments")
        print("4. Select a pet")
        if(cur_pet):
            print("5. See current pet")
            print("6. See current pet's appointments")

# ✅ 11. Create a function `greeting()` and `get_name()` that welcomes the user to the program and asks for their name 

# ✅ 12. Use `greeting` and `main` to start the program
def greeting():
    print("*******************")
    print("WECLOME TO THE VET")
    print("*******************")

def get_name():
    print("Enter your full name (case-sensitive): ")

    

if __name__ == "__main__":
    greeting()
    main()