#Using the function in section A, generate 10 integers that are between 1 and 100.
#Create a list. Call it rand_numbers. Use this list to save the generated integers. Print the list.

#Just one Random number
from random import randint
def rand_numbers(start_number,end_number):
    rand_number = randint(start_number,end_number)
    return rand_number

random = rand_numbers(1,100)
print("A random number between 1 to 100 is :" + str(random))

#Number1
import random
import statistics

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

#Average_alt2
average = statistics.mean(rand_numbers)
print("Average:", average)

#Excerise2
#Create a Calculator that can perform four basic operations: addition, subtraction, multiplication, and division!
from random import randint

def numbers(number1,number2):
    user_numbers = randint(number1(int(input())), number2(int(input())))
    return user_numbers

#addition = number1 + number2
#print("Addition:", addition)

#subtraction = 
#multiply =
#division =


#Your program asks the user to input the operation they want to perform and input two numbers.
#Then it performs the operation and display the result
