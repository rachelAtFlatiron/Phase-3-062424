# Sequence Types

# Creating Lists
#✅ 1. Create a list of 10 pet names

#------------------------ Reading Information from Lists
#✅ 1a. Return the first pet name 

#✅ 1b. Return the last value

#✅ 1c. Return all pet names beginning from the 3rd index

#✅ 1d. Return all pet names before the 3rd index

#✅ 1e. Return all pet names beginning from the 3rd index and up to (exclusive of) the 7th

#✅ 1f. Find the index of a given element

#✅ 1g. Reverse the original list

#✅ 1h. Return the frequency of a given element 

#---------------------------------- Updating Lists
#✅ 1i. Change the first element to all uppercase

#---------------------------------- Adding items to list
#✅ 1j. Append a new name to the list

#✅ 1k. Add a new name at a specific index

#✅ 1l. Add two lists together 

#---------------------------------- Removing 
#✅ 1m. Remove the final element from the list

#✅ 1n. Remove element by specific index

#✅ 1o. Remove a specific element 

#✅ 1p. Remove all pet names from the list

#---------------------------------- Tuple 
#✅ 2. Create a Tuple of pet 10 ages 

#✅ 2a. Print the first pet age

#---------------------------------- Testing Changeability 
#✅ 2b. Attempt to remove an element with .pop (should error)

#✅ 2c. Attempt to change the first element (should error)

#---------------------------------- Tuple Methods
#✅ 2d. Return the frequency of a given element

#✅ 2e. Return the index of first matching element 

#✅ 2f. Create a range 

#---------------------------------- Demo Sets
#✅ 3. Create a set of 3 pet foods

# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 4. Create a dictionary of pet information with the keys name, age and breed

#✅ 4a.  Use dict to create a dictionary of pet information with the keys name, age and breed

#---------------------------------- Reading
#✅ 4b. Print the pet attribute of name using bracket notation

#✅ 4c. Print the pet attribute of age using .get

#---------------------------------- Updating 
#✅ 4d. Update the pets age to 12

#✅ 4e. Update the other pets age to 26

#---------------------------------- Deleting
#✅ 4f. Delete a pets age using the del keyword 

#✅ 4g. Delete the other pets age using the .pop, returns removed value

#✅ 4h. Delete the last item in the pet dictionary using popitem()

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

#✅ 5a. loop through a range between 50 and 60 that iterates by 2 and print every number

#✅ 5b. Loop through the pet_info list and print every dictionary  

#✅ 6. Create a function that takes a list as an argument. 
    # The function should use a for loop to loop through the list and print every item in the list 
    # Invoke the function and pass it pet_names as an argument

#✅ 7. Create a function that takes a list as an argument.(simple example) 
    # The function should define a counter and set it to 0
    # Create a while loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # return the counter 

#✅ 8. Create a function that updates the age of a given pet
        # The function should take a list of dicts, name and age as parameters 
        # Create a index variable and set it to 0
        # Create a while loop. 
            # The loop will continue so long as the list does not contain a name matching the name param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found update the items age with the new age 
        # else return 'pet not found'

# map like 
#✅ 9. Use list comprehension to return a list containing every pet name from pet_info changed to uppercase

# find like
#✅ 9a. Use list comprehension to find a pet named spot

# filter like
#✅ 9b. Use list comprehension to find all of the pets under 3 years old

#✅ 9c. Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
