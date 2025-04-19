word = "uzhuzfztfziojeeeeertzfzh"
'''
def greet (first_name)
    print("hello" + first_name)

greet("john")
greet("Sara")
greet("James")
'''
def make_smoothie(first_fruit, second_fruit):
    print("Here you go, smoothie of " + first_fruit + " and " + second_fruit)

make_smoothie("banana" , "Strawberry")
make_smoothie("Apples", "Orange")


'''
EXERCISE 1

Write a function `greeting` that takes 2 arguments (first_name and last_name) and prints the following message using the given arguments:
    "Hello, Alice Smith, are you ready for some fun coding today?"
'''

# solution for exercise 1 👇🏽
def greet (first_name, second_name):
    print("Hello," + first_name +" "+  second_name +" "+ "are you ready for some fun coding today?")

greet("Alice" , "Smith")


'''
EXERCISE 2

Write a function `repeat_character` that takes a character and a number as arguments and prins a string,
where the character is repeated the specified number of times. 
The number has a default value of 2.
For example, if the character is 'X' and the number is 4, the function should return "XXXX."
'''

# solution for exercise 2 👇🏽
def repeat(character,number):
    counter = 0
    while counter < number:
        print(character)
        counter = counter + 1

repeat("2",5)



'''
EXERCISE 3

Copy and paste your solution from exercise 2. 
This time, modify the function so that, if the given number is bigger than 10, it will print out "Sorry, too long!"
'''

# solution for exercise 3 👇🏽
def repeat1(character,number):
    if number>10:
        print("sorry, too long")
    else:
        print(character * number )

repeat1()

'''
EXERCISE 4

Create a simple dice roll simulator where you use the randint function to simulate rolling a six-sided die. Follow these steps:
    1. Import the random module to use the randint function.
    2. Create a function that uses randint function to generate a random integer between 1 and 6, and returns the integer.	
    3. Store the function result in a variable
    4. Print out the variable
'''

# solution for exercise 4 👇🏽
from random import randint
def generate_number(start_number, end_number):
    generated_number = randint(start_number, end_number)
    return generated_number

random_number= generate_number(1,6)
print("Random number:"+ str(random_number))

