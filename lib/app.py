# 🛑 use the simplicity of this lesson as an opportunity to look up documentation

# Sequence Types

# Creating Lists
#✅ 1. Create a list of 10 pet names
#🛑 we call arrays 'lists' in python
#🛑🛑 Mutable: can change values (tuples are immutable)
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

#------------------------ Reading Information from Lists
#✅ 1a. Return the first pet name 
print(pet_names[0]) # -> 'Rose' 

#✅ 1b. Return the last value
#🛑 can keep going backwards
print(pet_names[-1]) # -> 'Paul'

#✅ 1c. Return all pet names beginning from the 3rd index
#💡 Is this inclusive or exclusive? (inclusive)
print(pet_names[3:]) # -> ['Luke', 'Lea', 'Princess Grace', ...]

#✅ 1d. Return all pet names before the 3rd index
#💡 Is this inclusive or exclusive? (exclusive)
print(pet_names[:3]) # -> ['Rose', 'Meow Meow Beans', 'Mr.Legumes']

#✅ 1e. Return all pet names beginning from the 3rd index and up to (exclusive of) the 7th
print(pet_names[3:7]) # -> ['Luke', 'Lea', 'Princess Grace', 'Spot']

#✅ 1f. Find the index of a given element
print(pet_names.index('Tom')) # -> 7

#✅ 1g. Reverse the original list
pet_names.reverse() #🐛 try printing pet_names.reverse() to see None
#🛑 Note that .reverse does not return anything, it is DESTRUCTIVE
print(pet_names)

#✅ 1h. Return the frequency of a given element 
print(pet_names.count('Rose')) # -> 1
print(['a', 'b', 'c', 'a', 'd', 'a'].count('a')) # -> 3

#---------------------------------- Updating Lists
#✅ 1i. Change the first element to all uppercase
#🛑 REASSIGNMENT 
pet_names[0] = pet_names[0].upper()
print(pet_names) # -> ['ROSE', 'Meow Meow Beans', ...]

#---------------------------------- Adding items to list
#✅ 1j. Append a new name to the list
pet_names.append('Blue') #🛑 MUTATES list
print(pet_names) # -> ['Rose', ..., 'Paul', 'Blue']

#✅ 1k. Add a new name at a specific index
pet_names.insert(0, "Bud") #beginning
pet_names.insert(3,'Red') #index 3
pet_names.insert(-1, "Sam") #second to list index (use append for end)

#✅ 1l. Add two lists together 
new_list = pet_names + ['Yellow', 'Green']
print(new_list) # -> ['Rose', ..., 'Yellow', 'Green']
new_list_2 = [1,2,3] + [4,5,6]
print(new_list_2) # -> [1, 2, 3, 4, 5, 6]

#---------------------------------- Removing 
#✅ 1m. Remove the final element from the list
print(pet_names.pop()) # -> Paul
print(pet_names) # -> ['Rose', ..., 'Mini']

#✅ 1n. Remove element by specific index
pet_names.pop(3)
print(pet_names)

#✅ 1o. Remove a specific element 
pet_names.remove('Paul') #🛑 finds first matching case, google for all cases
print(pet_names)

#✅ 1p. Remove all pet names from the list
pet_names.clear()
print(pet_names)  # -> []

#---------------------------------- Tuple 
# 🛑 Immutable - useful for when pulling in data and perserving said data (to keep it from being changed/altered)

#✅ 2. Create a Tuple of pet 10 ages 
pet_ages = (3, 5, 6, 2, 7, 10, 2, 11, 7, 2)
print(pet_ages) # -> (3, 5, 6, 2, 7, 10, 2, 11, 7, 2)

#✅ 2a. Print the first pet age
print(pet_ages[0]) # -> 3

#---------------------------------- Testing Changeability 
#✅ 2b. Attempt to remove an element with .pop (should error)
pet_ages.pop() # -> AttributeError: 'tuple' object has no attribute 'pop' 

#✅ 2c. Attempt to change the first element (should error)
pet_ages[0] = 'rose' # -> TypeError: 'tuple' object does not support item assignment
print(pet_ages)

#---------------------------------- Tuple Methods
#✅ 2d. Return the frequency of a given element
print(pet_ages.count(2)) # -> 3
#✅ 2e. Return the index of first matching element 
print(pet_ages.index(10)) # -> 5

#✅ 2f. Create a range 
#🛑 Ranges are primarily used in loops
range_1 = range(10)
print(range_1) # -> range_1(0, 10) 
range_2 = range(90, 100, 2) # -> range(90, 100, 2)


#---------------------------------- Demo Sets
#✅ 3. Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}
# print(pet_fav_food)
# -> {'bacon', 'fish', 'house plants'}
# 🛑 duplicate items not allowed
letters = set('banana') # => { 'b', 'a', 'n'}


# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 4. Create a dictionary of pet information with the keys name, age and breed
#🛑 like JSON where the keys are strings
#🛑 faster than using dict() since it doesn't require method call
pet_info_rose = {'name':'rose','age':11,'breed':'domestic long '}
# print(pet_info_rose)
# -> {'name': 'Rose', 'age': 11, 'breed': 'domestic long '}

#✅ 4a.  Use dict to create a dictionary of pet information with the keys name, age and breed
#🛑 useful for ensuring keys are valid identifiers {'1+1=':2}
pet_info_spot = dict(name='Spot', age=25, breed='boxer')
print(pet_info_spot) # -> {'name': 'Spot', 'age': 25, 'breed': 'boxer'}

#---------------------------------- Reading
#✅ 4b. Print the pet attribute of name using bracket notation
#🛑 gives error if key/value does not exist 
print(pet_info_rose['name']) # -> Rose 

#✅ 4c. Print the pet attribute of age using .get
#🛑 returns None if key/value does not exist
print(pet_info_rose.get('age')) # -> 11
#🛑 optional second param to specify error statement
print(pet_info_rose.get('temperament', 'Attribute Not Found!'))
#🛑 Note: get is preferred over bracket notation in most cases because it will return none instead of an error if the item does not exist

#---------------------------------- Updating 
#✅ 4d. Update the pets age to 12
pet_info_rose['age'] = 12
print(pet_info_rose) # -> {'name': 'rose', 'age': 12, 'breed': 'domestic long '}

#✅ 4e. Update the other pets age to 26
#🛑 useful for updating multiple key/value pairs
pet_info_spot.update({'age':26})
print(pet_info_spot) # -> {'name': 'Spot', 'age': 26, 'breed': 'boxer'}

#---------------------------------- Deleting
#✅ 4f. Delete a pets age using the del keyword 
#🛑 del can be used on other things besides key/value pairs (i.e. variables), removes it from the global/local scope
del pet_info_spot['age']
print(pet_info_spot) # -> {'name': 'Spot', 'breed': 'boxer'}

#✅ 4g. Delete the other pets age using the .pop, returns removed value
pet_info_rose.pop('age')
print(pet_info_rose) # -> {'name': 'rose', 'breed': 'domestic long '}

#✅ 4h. Delete the last item in the pet dictionary using popitem()
pet_info_rose.popitem()
print(pet_info_rose) # ->{'name': 'rose', 'age': 11}


#---------------------------------- Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]
#✅ 5. loop through a range of 10 and print every number within the range
for num in range(10):
    print(num)

#✅ 5a. loop through a range between 50 and 60 that iterates by 2 and print every number
for num in range(50, 60, 2):
    print(num)

#✅ 5b. Loop through the pet_info list and print every dictionary  
for pet in pet_info:
    print(pet)

#✅ 6. Create a function that takes a list as an argument. 
    # The function should use a for loop to loop through the list and print every item in the list 
    # Invoke the function and pass it pet_names as an argument
def print_info(lst):
    for item in lst:
        print(item)

print_info(pet_names)

#✅ 7. Create a function that takes a list as an argument.(simple example) 
    # The function should define a counter and set it to 0
    # Create a while loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # return the counter 
def count(info):
    counter = 0
    while(counter < len(info)-1):
        counter += 1
    return counter
count(pet_info)

#✅ 8. Create a function that updates the age of a given pet
        # The function should take a list of dicts, name and age as parameters 
        # Create a index variable and set it to 0
        # Create a while loop. 
            # The loop will continue so long as the list does not contain a name matching the name param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found update the items age with the new age 
        # else return 'pet not found'

def update_age(info, name, age):
    index = 0
    while(info[index].get('name') != name and index < len(info)-1):
        index += 1

    if info[index].get('name') == name:
        info[index]['age'] = age
        return info[index]
    else:
        return 'pet not found' 

print(update_age(pet_info,'spot',2))


# map like 
#✅ 9. Use list comprehension to return a list containing every pet name from pet_info changed to uppercase
pet_names_upper = [pet.get('name').upper() for pet in pet_info] 
print(pet_names_upper)

# find like
#✅ 9a. Use list comprehension to find a pet named spot
find_pet = [ pet for pet in pet_info if pet.get('name') == 'spot']
print(find_pet)

# filter like
#✅ 9b. Use list comprehension to find all of the pets under 3 years old
young_pets = [pet for pet in pet_info if pet.get('age') < 3]
print(young_pets)

#✅ 9c. Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
young_pets_generator = (pet for pet in pet_info if pet.get('age') < 3)
print(young_pets_generator)
# #<generator object <genexpr> at 0x10777b900>

#good labs
# Deli counter: https://learning.flatironschool.com/courses/7598/assignments/274126?module_item_id=661652
# Oxford Comma: https://learning.flatironschool.com/courses/7598/assignments/274154?module_item_id=661651

#list comprehension practice: 

# 1. Find all of the numbers from 1-1000 that are divisible by 7
# 2. Find all of the numbers from 1-1000 that have a 3 in them
# 3. Count the number of spaces in a string
# 4. Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
# 5. Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)
# 6. Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
# 7. Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
# 8. Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
# 9. Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
# 10. Find all of the words in a string that are less than 4 letters
# 11. Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

#https://bbookman.github.io/Python-list-comprehension1/
