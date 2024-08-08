#!/usr/bin/env python3
#✅ import owner, pet, and appointments
from owner import Owner 
from pet import Pet 
from procedure import Procedure
from appointments import Appointment

#owner has many appointments
#owner has many pets

#pet belongs to owner
#pet belongs to appointment

#appointment belongs to pet
#appointment belongs to owner through pet (can't import owner due to circular import)

#✅ 2. use chatGPT to create owners and pets

owner1 = Owner("Alice Smith", "555-1234", "alice@example.com")
owner2 = Owner("Bob Johnson", "555-5678", "bob@example.com")
owner3 = Owner("Charlie Brown", "555-8765", "charlie@example.com")
owner4 = Owner("Diana Prince", "555-4321", "diana@example.com")
owner5 = Owner("Edward Norton", "555-6789", "edward@example.com")
owner6 = Owner("Fiona Gallagher", "555-2345", "fiona@example.com")
owner7 = Owner("George Martin", "555-3456", "george@example.com")
owner8 = Owner("Hannah Davis", "555-4567", "hannah@example.com")
owner9 = Owner("Ian Curtis", "555-5679", "ian@example.com")
owner10 = Owner("Jill Valentine", "555-6780", "jill@example.com")
owner11 = Owner("Rick", "999-9999", "rick@example.com")

pet1 = Pet("Fluffy", 3, "Labrador", owner=owner10)
pet2 = Pet("Max", 2, "Beagle", owner=owner1)
pet3 = Pet("Bella", 4, "Poodle", owner=owner2)
pet4 = Pet("Daisy", 1, "Bulldog", owner=owner3)
pet5 = Pet("Charlie", 5, "Golden Retriever", owner=owner4)
pet6 = Pet("Milo", 6, "Siamese", owner=owner5)
pet7 = Pet("Lucy", 3, "Rottweiler", owner=owner6)
pet8 = Pet("Oliver", 2, "Shih Tzu", owner=owner2)
pet9 = Pet("Sophie", 4, "Dachshund", owner=owner8)
pet10 = Pet("Buddy", 5, "Chihuahua", owner=owner9)
pet11 = Pet("Luna", 1, "Sphynx", owner=owner10)
pet12 = Pet("Coco", 2, "Maine Coon", owner=owner8)
pet13 = Pet("Teddy", 3, "Bichon Frise", owner=owner2)
pet14 = Pet("Sadie", 4, "Pug", owner=owner3)
pet15 = Pet("Chester", 5, "Cocker Spaniel", owner=owner4)
pet16 = Pet("Ruby", 6, "Great Dane", owner=owner8)
pet17 = Pet("Jack", 1, "Pomeranian", owner=owner6)
pet18 = Pet("Maggie", 2, "Yorkshire Terrier", owner=owner7)
pet19 = Pet("Rex", 3, "Boxer", owner=owner8)
pet20 = Pet("Lola", 4, "Australian Shepherd", owner=owner9)
stray = Pet("Tramp", 2, "Mutt")

procedure1 = Procedure("Vaccination", 75.50)
procedure2 = Procedure("Dental Cleaning", 120.00)
procedure3 = Procedure("Spay/Neuter", 250.00)
procedure4 = Procedure("Wellness Exam", 45.00)
procedure5 = Procedure("Surgery", 350.00)


# Create 40 instances of Appointment class, each assigned to its own variable
appointment1 = Appointment("Staff1", pet20, procedure2)
appointment2 = Appointment("Staff2", pet1, procedure3)
appointment3 = Appointment("Staff3", pet2, procedure4)
appointment4 = Appointment("Staff4", pet3, procedure5)
appointment5 = Appointment("Staff5", pet4, procedure1)
appointment6 = Appointment("Staff6", pet5, procedure4)
appointment7 = Appointment("Staff7", pet6, procedure2)
appointment8 = Appointment("Staff8", pet7, procedure3)
appointment9 = Appointment("Staff9", pet8, procedure4)
appointment10 = Appointment("Staff10", pet9, procedure1)
appointment11 = Appointment("Staff1", pet10, procedure2)
appointment12 = Appointment("Staff2", pet11, procedure3)
appointment13 = Appointment("Staff3", pet12, procedure4)
appointment14 = Appointment("Staff4", pet13, procedure5)
appointment15 = Appointment("Staff5", pet14, procedure1)
appointment16 = Appointment("Staff6", pet15, procedure4)
appointment17 = Appointment("Staff7", pet16, procedure2)
appointment18 = Appointment("Staff8", pet17, procedure3)
appointment19 = Appointment("Staff9", pet18, procedure4)
appointment20 = Appointment("Staff10", pet19, procedure3)
appointment21 = Appointment("Staff1", pet20, procedure2)
appointment22 = Appointment("Staff2", pet1, procedure3)
appointment23 = Appointment("Staff3", pet2, procedure4)
appointment24 = Appointment("Staff4", pet3, procedure5)
appointment25 = Appointment("Staff5", pet4, procedure1)
appointment26 = Appointment("Staff6", pet5, procedure4)
appointment27 = Appointment("Staff7", pet6, procedure2)
appointment28 = Appointment("Staff8", pet7, procedure3)
appointment29 = Appointment("Staff9", pet8, procedure4)
appointment30 = Appointment("Staff10", pet9, procedure3)
appointment31 = Appointment("Staff1", pet10, procedure2)
appointment32 = Appointment("Staff2", pet11, procedure3)
appointment33 = Appointment("Staff3", pet12, procedure4)
appointment34 = Appointment("Staff4", pet13, procedure5)
appointment35 = Appointment("Staff5", pet14, procedure1)
appointment36 = Appointment("Staff6", pet15, procedure4)
appointment37 = Appointment("Staff7", pet16, procedure2)
appointment38 = Appointment("Staff8", pet17, procedure3)
appointment39 = Appointment("Staff9", pet18, procedure4)
appointment40 = Appointment("Staff10", pet19, procedure3)


import ipdb; ipdb.set_trace()
