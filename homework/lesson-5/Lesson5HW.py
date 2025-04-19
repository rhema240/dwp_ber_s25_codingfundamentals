#By using Google, find a function that gives you current date and time and print the current date and time
from datetime import datetime
now = datetime.now()
print("Current date and time:", now)

## HOMEWORK 2
#Do you still remember loops?
#1. Write a function that counts number of letters in a string you input.
#2. The function will have 1 parameter, the string that's letters you want to count.
#3. Try both variants - print the result (number of letters in the inputed string) and also store the result in the memory using return. Try to recall what is the difference between using print and return

def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():  
            count += 1
    return count

user_input = input("Enter a string: ")
print("Number of letters:", count_letters(user_input))


## HOMEWORK 3: Using results of function in another function
#1. Create a simple function with two parameters that returns their sum.
#2. Call the function and save the result into a variable (name of the variable is up to you).
#3. Create another function with one parameter that decides if the parameter can be divided by 3 and prints appropriate messages
#4. Call the second function and use the variable that you created in the b) part as argument.

'''
def addition(number1 =  int(input("Write a number:")) , number2 = int(input("Give another number:"))):
    print(number1 + number2)
    total = number1 + number2
    return total

print("Total sum is:" + total)


def divisible_by3(addition):
    if addition % 3 == 0:
        print(f"{addition} is divisible by 3.")
    else:
        print(f"{addition} is NOT divisible by 3.")

'''


## (Bonus) HOMEWORK 4: Rock, Paper, Scissors
#Here's what you need to do:
#1. Complete the game logic inside the play_game(user_choice) function. The function should determine the outcome of the game based on the user's choice (0 for rock, 1 for paper, and 2 for scissors) and the computer's randomly generated choice.
''''
import random 
def playgame (user_choice):
    choices =("rock","paper","scissors")
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print("Its a Tie")
'''

user_choice = int(input("Pick a number 0-2:", ))

if user_choice==0:
     print("Your choice is rock")
elif user_choice==1:
    print("Your choice is paper")
elif user_choice==2:
    print("Your choice is scissors")  
else:
     print("Your number is too big, pick a number between 0 and 2")

print("Computer's Choice")
from random import randint
def generate_number(start_number, end_number):
    generated_number = randint(start_number, end_number)
    return generated_number

random_number= generate_number(0,2)
print("Random number:"+ str(random_number))

if random_number==0:
    print("Computer's choice is Rock")
elif random_number==1:
    print("Computer's choice is Paper")
else:
    print("Computer's choice is Scissors")    

#2. The possible outcomes are as follows:
#   - If the user's choice is the same as the computer's choice, it's a "Tie."
#   - If the user wins, return "You win."
#   - If the computer wins, return "You lose."
if user_choice== 0 and random_number==1:
    print("You lose")
if user_choice==1 and random_number==0:
    print("You win")
if user_choice==2 and random_number==0:
    print("You lose")
if user_choice==0 and random_number==2:
    print("You win")
if user_choice==1 and random_number==2:
    print("You lose")
else:
    print("Tie")

#3. Test the game by calling the function with different user choices and print the results.
#Reminder:
#- Rock beats Scissors
#- Scissors beats Paper
#- Paper beats Rock