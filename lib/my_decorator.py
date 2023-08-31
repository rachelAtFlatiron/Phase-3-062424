#✅ 1. Demonstrate First Class Functions
#⭐️ more -> http://bit.ly/3YQh8KR
#🛑 can assign first class functions to variables, store in data structures, pass to other functions, return them as value from other functions
#🛑 can treat functions just like anything else (ints, strings, etc)

#✅ 1a. Create functions to be used as callbacks 
#🛑 these will be invoked at a later point
def walk(pet):
    print(f'{pet} has been walked!')

def feed(pet):
    print(f'{pet} has been fed!')

#✅ 1b. Create a higher-order function that will take a callback as an argument
def execute_task(func):
    func("Rose") #🛑 what happens if we put return?

execute_task(walk)
print(execute_task(walk)) #🛑 Note this returns None

#✅ 2. Higher order functions
#✅ 2a. Create a higher-order function that returns a function
def execute_func():
    def feed(pet):
        return f'{pet} has been fed!'
    return feed #💡 What will return value be?

print(execute_func())
feed = execute_func()
feed("Rose")

print(execute_func()("Rose")) #🛑 similar to chaining

#✅ 3. Create a higher-order function that returns two functions
def execute_two_func():
    def feed(pet="Rose"):
        return f'{pet} has been fed!'
    def walk(pet="Rose"):
        return f'{pet} has been walked!'
    return feed, walk #💡 what data type is this? (tuple)

print(execute_two_func())
print(execute_two_func()[0]())
print(execute_two_func()[1]("Momo"))

#🛑 you can destructure the tuple
feed_func, walk_func = execute_two_func()
print(feed_func())

#✅ 4. Demonstrate how to create a decorator
# Create a function that:
#✅ 4a. takes a function as an argument, 
#✅ 4b. has an inner function, and 
#✅ 4c. returns the inner function

#🛑 ~~~~~~~ The following is without pie syntax

#✅ Decorator (coupon_calculator)
def coupon_calculator(func):
    #✅ Inner Function
    def report_price():
        print('Initial Price = $35.00')
        final_price = func(35.00)
        print(f'Newly Discounted Price = {final_price}')
    return report_price

#✅ Callback function to Calculate New Price
#🛑 use .format: https://www.geeksforgeeks.org/python-string-format-method/
#🛑 use .round: https://www.geeksforgeeks.org/round-function-python/
def calculate_price(price):
    #🛑 need this in case price/2 = 17.5
    return '{:.2f}'.format(round(price/2, 2)) 

# report_price_from_coupon_calculator = coupon_calculator(calculate_price)
# print(report_price_from_coupon_calculator())

#🛑 ~~~~~~~ The following is with pie syntax

@coupon_calculator #🛑 the below function gets passed into coupon_calculator
def calculate_price(price):
    #🛑 need this in case price/2 = 17.5
    return '{:.2f}'.format(round(price/2, 2)) 

@coupon_calculator
def some_other_function(price):
    return "Something"

calculate_price()
some_other_function()

