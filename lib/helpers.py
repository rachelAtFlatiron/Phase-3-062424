from models.owner import Owner 
from models.pet import Pet
from models.appointment import Appointment
from models.procedure import Procedure
def helper_1():
    print("Performing useful function#1.")

def print_owner(id):
    owner = Owner.find_by_id(id)
    print(f'Owner #{owner.id}. {owner.name}')
def print_pet(id):
    pet = Pet.find_by_id(id)
    print(f'Pet #{pet.id}. {pet.name}')
def print_all_owners():
    for owner in Owner.get_all():
        print(f'{owner.id}. {owner.name}')

def print_all_pets_for_owner(id):
    if(id):
        for pet in Pet.get_owner_pets(id):
            print(f'{pet.id}. {pet.name}')

    else:
        print('no user selected')


def print_all_apps_for_owner(id):
    if(id):
        for app in Appointment.get_owner_apps(id):
            proc = Procedure.find_by_id(app.procedure_id)
            pet= Pet.find_by_id(app.pet_id)
            print(f'{pet.name} has a {proc.name} appointment for ${proc.price}')

    else:
        print('no user selected')


def print_apps_for_one_pet(id):
    if(id):
        pet = Pet.find_by_id(id)
        print(f'{pet.name} has the following appointments...')
        for app in Appointment.get_pet_apps(id):
            proc = Procedure.find_by_id(app.procedure_id)
            print(f'A {proc.name} for ${proc.price}')

    else:
        print('no pet selected')

def exit_program():
    print("Goodbye!")
    exit()