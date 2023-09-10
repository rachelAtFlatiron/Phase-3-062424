#!/usr/bin/env python3

#🛑 conn, cursor defined individually in both owner and pet
#🛑 one connection per table?
from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

# Pet.create_table()
# spot = Pet("spot", "dog", "chihuahua", "feisty", 1)
# spot.save()

import ipdb; ipdb.set_trace()
