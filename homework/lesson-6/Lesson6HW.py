#Number1
#Numbers in a list and the average
import random

def generate_random_numbers():
    rand_numbers = []
    for _ in range(10):
        rand_numbers.append(random.randint(1, 100))
    return rand_numbers

rand_numbers = generate_random_numbers()
print("Generated numbers:", rand_numbers)

#Average_alt1
average = sum(rand_numbers) / len(rand_numbers)
print("Average:", average)



#Excerise2
#Create a Calculator that can perform four basic operations: addition, subtraction, multiplication, and division!
from random import randint

def numbers(number1, number2):
    return randint(number1, number2)

print("Welcome to the Basic Calculator!")
print("Enter two numbers to perform operations.")
print("Type 'q' to quit.\n")

while True:
    first_input = input("Give a number (or 'q' to quit): ")
    if first_input.lower() == 'q':
        print("Goodbye! 👋")
        break

    second_input = input("Give another number (or 'q' to quit): ")
    if second_input.lower() == 'q':
        print("Goodbye! 👋")
        break


    try:
        number1 = int(first_input)
        number2 = int(second_input)
    except ValueError:
        print("⚠️ One or both inputs were not valid integers.\n")
        continue


    
    print("\n🔢 Number Operations")
    print(f"Addition: {number1} + {number2} = {number1 + number2}")
    print(f"Subtraction: {number1} - {number2} = {number1 - number2}")
    print(f"Multiplication: {number1} * {number2} = {number1 * number2}")
    
    if number2 != 0:
        print(f"Division: {number1} / {number2} = {number1 / number2}")
    else:
        print("⚠️ Cannot divide by zero.")

    print("\n---\n")



#Exerise3 
#Guessing game with the computer
from random import randint
def guess_number (start_number,end_number):
    user_number = randint(start_number,end_number)
    return user_number

computers_number= guess_number(1,100)

print("\n---\n")
print("\nLets play a game\n")
print("Guess a number between 1-100, lets try to guess the same number")
print("You have five tries to guess it.\n")

MAX_TRIES = 5

for attempt in range(1, MAX_TRIES + 1):
    try:
        users_number = int(input(f"Attempt {attempt}/{MAX_TRIES} — your guess: "))
    except ValueError:
        print("Please enter a valid whole number.\n")
        # Don’t count this as an attempt; let them try again
        continue

    if users_number == computers_number:
        print(f" Correct! You guessed it in {attempt} {'try' if attempt == 1 else 'tries'}.")
        break
    elif users_number > computers_number:
        print("Too high!\n")
    else:
        print("Too low!\n")
else:
    # This block runs if we never hit `break` (i.e. all tries used up)
    print(f" You’ve used all {MAX_TRIES} tries. You lose!")
    print(f"The number was: {computers_number}") 


