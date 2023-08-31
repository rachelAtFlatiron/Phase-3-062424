#!/usr/bin/env python3

#✅ 5. Import the pet and cat class to use in debug.py
from lib.pet import *
from lib.cat import *

#🛑 if there is an ipdb.set_trace() in pet.py or cat.py we will not get to the below code 


# Instances of the pet classes
rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)
cookie = Pet('cookie', 1, 'Dachshund', 'hyper', 'cookie.jpg')
princess_grace = Pet('princess grace', 7, 'domestic longhair', 'affectionate', 'gracy.png')



import ipdb; ipdb.set_trace()