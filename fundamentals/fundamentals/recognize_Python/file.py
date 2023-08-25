num1 = 42   # variable declaration, initialize number
num2 = 2.3  # variable declaration, initialize number
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) # prints the data type of the variable fruit
print(pizza_toppings[1]) # prints the element at index 1 from the pizza_toppings list.
pizza_toppings.append('Mushrooms') # append the string 'Mushrooms' to the pizza_toppings list.
print(person['name']) # prints the value associated with the key "name" in the person dictionary
person['name'] = 'George' # assigns the value 'George' to the key 'name' in the person dictionnary.
person['eye_color'] = 'blue' # assigns the value 'eye_color' to the key 'eye_color' in the person dictionnary.
print(fruit[2])  # prints the element at index 2 from the fruit tuple

if num1 > 45:   # beginning of if statement
    print("It's greater") # prints the "It's a greater" when num1 is greater than 45
else: 
    print("It's lower") # prints the "It's lower" when num1 is smaller than 45

if len(string) < 5: # beginning of if statement that checks the lenght of a string
    print("It's a short word!") # prints "It's a short world!" if lenght of the string is smaller than 5
elif len(string) > 15:
    print("It's a long word!") # prints "It's a long world!" if lenght of the string is greater than 15
else:
    print("Just right!") # prints "Just right!" when none of the condition is true

for x in range(5): # declaration of a for loop that iterates a sequence of numbers from 0 to 5
    print(x) # prints the value of x
for x in range(2,5): # starts a loop that iterates over a sequence of numbers from 2 to 4
    print(x) # prints the value of x
for x in range(2,10,3): # starts a for loop that iterates over a sequence of numbers starting from 2 and incrementing by 3, until it reaches a number less than 10
    print(x) # prints the value of x
x = 0  # initialize the varaible x with a value of 0
while(x < 5): # starts a while loop that continues executing the indented block of code as long as the condition x < 5 is True.
    print(x) # prints the value of x
    x += 1 # increments the value of x by 1

pizza_toppings.pop() #remove the last element from to the pizza_toppings list
pizza_toppings.pop(1) # removes the element at index 1 from the pizza_toppings list

print(person)  # prints the string representation of the dictionary
person.pop('eye_color') # remove the key-value "eye_color" from the person dictionary
print(person) # prints the string representation of the dictionary

for topping in pizza_toppings: # declaration of the for loop that iterates over each element('topping') in the pizza_toppings list
    if topping == 'Pepperoni': # checks if the value of topping is equal to 'Pepperoni'
        continue
    print('After 1st if statement') # prints 'After 1st if statement' regarless the previous If condition is True of False
    if topping == 'Olives':  # checks if the value of topping is equal to 'Olives'
        break

def print_hello_ten_times(): # defines a function named print_hello_ten_times()
    for num in range(10):    # declaration of a for loop that iterates a sequence of numbers from 0 to 9, and assigned each iteration to num
        print('Hello')  # prints the value of the string 'Hello'

print_hello_ten_times() # calls the function Print_hello_ten_times

def print_hello_x_times(x): # defines a function named print_hello_ten_times that takes a single parameter x
    for num in range(x): # declaration of a for loop that iterates a sequence of numbers from 0 to x-1, and assigned each iteration to num
        print('Hello') # prints the value of the string 'Hello'

print_hello_x_times(4) # calls the function Print_hello_x_times with the argument of 4

def print_hello_x_or_ten_times(x = 10): # defines a function named print_hello_x_or_ten_times with a parameter that has a default value of 10
    for num in range(x): # declaration of a for loop that iterates a sequence of numbers from 0 to x-1, and assigned each iteration to num
        print('Hello')  # prints the value of the string 'Hello

print_hello_x_or_ten_times()  # calls the function Print_hello_ten_x_or_times
print_hello_x_or_ten_times(4) # calls the function Print_hello_x_or_times with the argument of 4


"""
Bonus section
"""

# print(num3) 
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)