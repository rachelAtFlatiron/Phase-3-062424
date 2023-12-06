#!/usr/bin/env python3

from models.owner import Owner, CONN, CURSOR
from models.pet import Pet, CONN, CURSOR
from models.procedure import Procedure, CONN, CURSOR
from models.appointment import Appointment, CONN, CURSOR

Owner.drop_table()
Pet.drop_table()
Procedure.drop_table()
Appointment.drop_table()

Owner.create_table()
Pet.create_table()
Appointment.create_table()
Procedure.create_table()

owner1 = Owner.create("John Doe", "john@example.com")
owner2 = Owner.create("Alice Smith", "alice@example.com")
owner3 = Owner.create("Bob Johnson", "bob@example.com")
owner4 = Owner.create("Eva Williams", "eva@example.com")
owner5 = Owner.create("Charlie Brown", "charlie@example.com")

pet1 = Pet.create("Buddy", 3, "Golden Retriever", owner2.id)
pet2 = Pet.create("Max", 2, "German Shepherd", owner2.id)
pet3 = Pet.create("Luna", 5, "Labrador", owner3.id)
pet4 = Pet.create("Milo", 1, "Poodle", owner4.id)
pet5 = Pet.create("Coco", 4, "Bulldog", owner5.id)
pet6 = Pet.create("Bailey", 2, "Beagle", owner5.id)
pet7 = Pet.create("Rocky", 6, "Rottweiler", owner2.id)
pet8 = Pet.create("Charlie", 3, "Husky", owner3.id)
pet9 = Pet.create("Daisy", 7, "Yorkshire Terrier", owner4.id)
pet10 = Pet.create("Lucy", 2, "Dachshund", owner5.id)

proc1 = Procedure.create("Checkup", 30)
proc2 = Procedure.create("Vaccination", 0)
proc3 = Procedure.create("Surgery", 100)
proc4 = Procedure.create("Dental Cleaning", 40)

appointment1 = Appointment.create(pet2.id, proc1.id)
appointment2 = Appointment.create(pet2.id, proc2.id)
appointment3 = Appointment.create(pet3.id, proc3.id)
appointment4 = Appointment.create(pet4.id, proc1.id)
appointment5 = Appointment.create(pet5.id, proc4.id)
appointment6 = Appointment.create(pet6.id, proc2.id)
appointment7 = Appointment.create(pet7.id, proc1.id)
appointment8 = Appointment.create(pet8.id, proc1.id)
appointment9 = Appointment.create(pet9.id, proc3.id)
appointment10 = Appointment.create(pet10.id, proc1.id)
appointment11 = Appointment.create(pet10.id, proc2.id)
appointment12 = Appointment.create(pet2.id, proc1.id)
appointment13 = Appointment.create(pet3.id, proc4.id)
appointment14 = Appointment.create(pet4.id, proc1.id)
appointment15 = Appointment.create(pet5.id, proc3.id)
appointment16 = Appointment.create(pet6.id, proc1.id)
appointment17 = Appointment.create(pet7.id, proc2.id)
appointment18 = Appointment.create(pet8.id, proc1.id)
appointment19 = Appointment.create(pet9.id, proc4.id)
appointment20 = Appointment.create(pet10.id, proc1.id)

import ipdb; ipdb.set_trace()
