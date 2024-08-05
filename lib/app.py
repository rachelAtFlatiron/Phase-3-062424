# Sequence Types
import ipdb 
# JS - arrays, Python - lists 
# JS - objects, Python - dictionaries 

# Creating Lists
#✅ 1. Create a list of 10 pet names
pets = ["momo", "merv", "wisp", "cooper", "bailey", "shelly"]


#------------------------ Reading Information from Lists
#✅ 1a. Return the first pet name 
pets[0]

#✅ 1b. Return the last value
pets[-1]

#✅ 1c. Return all pet names beginning from the 3rd index
pets[0:3]
pets[:3]
pets[3:] #everything after and including the 3rd index
pets[3:5] #everything from the 3rd index up to and not including the 5th index 

#https://docs.python.org/3/tutorial/datastructures.html
#✅ 1f. Find the index of a given element
pets.index('merv')
#✅ 1g. Reverse the original list
#mutates the original array 
pets.reverse()

#✅ 1h. Return the frequency of a given element 
pets.count('merv')
#---------------------------------- Updating Lists
#✅ 1i. Change the first element to all uppercase
pets[0] = "frankenstein"
#---------------------------------- Adding items to list
#✅ 1j. Append a new name to the list
pets.append('last')
#✅ 1k. Add a new name at a specific index
pets.insert(1, 'insert')
#✅ 1l. Add two lists together 
pets.extend(['a', 'b', 'c'])
['a', 'b', 'c'] + ['d', 'e', 'f']

#---------------------------------- Removing 
#✅ 1m. Remove the final element from the list
pets.pop() #removes AND returns 

#✅ 1n. Remove element by specific index
pets.pop(-2) #-2 for second to last element

#✅ 1o. Remove a specific element 
pets.remove('wisp')

#✅ 1p. Remove all pet names from the list
pets.clear() #pets is now []

#---------------------------------- Tuple 
# collection of items that CANNOT BE CHANGED (immutable)

#✅ 2. Create a Tuple of pet 10 ages 
pet_ages = (3, 1, 6, 9, 22, 1)


#✅ 2a. Print the first pet age
pet_ages[0]

#---------------------------------- Tuple Methods
#✅ 2d. Return the frequency of a given element
pet_ages.count(1) #count is a sequence operator that can be used by both lists and tuples

#✅ 2e. Return the index of first matching element 
pet_ages.index(22) #index is a sequence operator that can be used by both lists and tuples

#✅ 2f. Create a range 
# range(start_num, end_num, step)
tuple(range(0, 10, 2)) #(0, 2, 4, 6, 8)

one_tuple = (3, )
#---------------------------------- Demo Sets
# SETS ONLY HAVE UNIQUE ITEMS
#✅ 3. Create a set of 3 pet foods
test = {"test", "test", "test"} # => {"test"}
pairs = ["apple", "apple", "lemon", "lime", "lemon", "lime"]

# Demo Dictionaries (in JS its objects)
#---------------------------------- Creating 
#main difference is you need quotes surrounding the keys
merv = {
    'name': 'merv',
    'mood': 'bagagwa',
    'food': 'pad thai'
}
wisp = dict(name='wisp', mood='feisty', food='messy')


#---------------------------------- Reading
#✅ 4b. Print the pet attribute of name using bracket notation
wisp['name']
wisp.get('name')

#---------------------------------- Updating 
#✅ 4d. Update
wisp['mood'] = 'sleepy'
wisp.update({'mood': 'spicy'})
#---------------------------------- Deleting
#✅ 4f. Delete a pets age using the del keyword 
del wisp['food'] # => {'name': 'wisp', 'mood': 'spicy'}
wisp.pop('mood') # => remove key/value AND return value of removed pair

#---------------------------------- Demo Loops 
pet_info = [
    {
        'name': 'merv',
        'age': 6,
        'breed': 'domestic long-haired'
    }, 
    {
        'name':'wisp',
        'age': 2,
        'breed': 'weirdo',
    },
    {
        'name':'momo',
        'age': 4,
        'breed': 'silly goose',
    }
]
#✅ 5. loop through a range of 10 and print every number within the range
#for(int i = 0; i < 10, i++)
# for num in range(0, 10, 2):
#     print(num)

#✅ 5a. loop through a range between 50 and 60 that iterates by 2 and print every number

#✅ 5b. Loop through the pet_info list and print every dictionary  
# for pet in pet_info:
#     print(pet)

#✅ 7. Create a function that takes a list as an argument 
    # The function should define a counter and set it to 0
    # Create a while loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # return the counter 
counter = 0
while(counter < 10):
    print(counter)
    counter = counter + 2

#✅ 8. Create a function that updates the age of a given pet
        # The function should take a list of dicts, name and age as parameters 
        # Create a index variable and set it to 0
        # Create a while loop. 
            # The loop will continue so long as the list does not contain a name matching the name param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found update the items age with the new age 
        # else return 'pet not found'

def update_age(given_name, new_age):
    
    #look through pet_info 
    # for pet in pet_info:
    #     print(pet)
    #     #if current pet's name matches given_name param 
    #     if pet['name'] == given_name:
    #         pet['age'] = new_age 
    #         #update current pet's age to new_age param

    #use while loop
    #continue iterating while we haven't found the correct pet 
    #once we find the correct pet, update age and stop iterating

    #represent the current pet index that we're looking at 
    index = 0
    #while we haven't reached the end of our list, or while we haven't found the correct index, move to the next pet
    while(index != len(pet_info) and pet_info[index]['name'] != given_name):
        index += 1
    
    #once we exit while loop, hypothetically our index will be at the correct pet 
    pet_info[index]['age'] = new_age

ipdb.set_trace()

# pet_info.map(cur_pet => cur_pet.name.uppercase())
[pet['name'].upper() for pet in pet_info]

# filter
[pet for pet in pet_info if pet['name'] == 'wisp']
[pet for pet in pet_info if pet['age'] < 6]

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
