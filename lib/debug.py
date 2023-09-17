#!/usr/bin/env python3

# 🛑 YOU HAVE TO CLOSE IPDB WITH 'QUIT' TO NOT KEEP SQL THREADS OPEN
# or ctrl D
# 🛑 conn, cursor defined individually in both owner and pet
# 🛑 one connection per table?
from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

pet1 = Pet("Fluffy", 2, "Labrador")
pet2 = Pet("Whiskers", 1, "Siamese")
pet3 = Pet("Buddy", 3, "Golden Retriever")
pet4 = Pet("Mittens", 2, "Persian")
pet5 = Pet("Rocky", 4, "Bulldog")
pet6 = Pet("Luna", 1, "Husky")
pet7 = Pet("Oliver", 5, "Maine Coon")
pet8 = Pet("Charlie", 2, "Poodle")
pet9 = Pet("Daisy", 3, "Beagle")
pet10 = Pet("Max", 4, "German Shepherd")

pet1.save()
pet2.save()
pet3.save()
pet4.save()

import ipdb; ipdb.set_trace()
