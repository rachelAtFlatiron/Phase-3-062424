# ORM (models) -> helpers.py (useful for creating relationships, managing the belongs to/has many) -> cli.py (main menu, infinite loop, if statements, what to do when a user inputs a specific number)


# ✅ 9. Import all helper functions and necessary models
from helpers import (
    print_all_owners,
    print_all_pets_for_owner
)
from models.owner import Owner 
from models.pet import Pet

global cur_owner 
cur_owner = None 
cur_pet = None 

#the main loop that constantly asks what the user wants to do next (including exiting the program)
# exit()
def main():
    menu()
    while(True):
        choice = input("Enter something")
        if(int(choice) == 0):
            exit()
        elif(int(choice) == 1):
            #each if statement will probably execute a helper function
            print_all_owners() 
        elif(int(choice) == 2):
            print_all_owners()
            set_cur_owner()
            print(f'Owner is currently: {cur_owner}')
        elif(int(choice) == 3):
            # get all pets where id equals owner
            if(not cur_owner):
                print("please select owner first")
            else:
                print_all_pets_for_owner(cur_owner.id)
            # print out all those pets 
        #if the user types something invalid
        elif(int(choice) == 4):
            #add new pet
            pass 
        elif(int(choice) == 5):
            #delete pet
            pass 
        elif(int(choice) == 6):
            #make appointment
            pass 
        else:
            menu()


def set_cur_owner():
    global cur_owner 
    choice = input("Enter number of owner: ")
    cur_owner = Owner.find_by_id(int(choice))

def menu():
    print (f"""  
        Current owner is {cur_owner}
        Enter 0 to exit \n 
        Enter 1 to see all owners \n
        Enter 2 to select new owner \n
        Enter 3 to see selected owners pets \n
    """)


if __name__ == "__main__":
    main()