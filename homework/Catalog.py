#Average of numbers
#Example1
import statistics
numbers = [10, 20, 30, 40, 50]
average = statistics.mean(numbers)
print("Average:", average)

#Example2
average = sum(numbers) / len(numbers) #length of numbers
print("Average:", average)

#Random number between 1-100
from random import randint
def rand_numbers(start_number,end_number):
    rand_number = randint(start_number,end_number)
    return rand_number

random = rand_numbers(1,100)
print("A random number between 1 to 100 is :" + str(random)) #Just one Random number

#What does the f stand for 
#An f-string (short for formatted string literal) 
# lets you insert variables or expressions directly inside a string, using curly braces {}
#-------------
#without the f-string
#print("Addition: " + str(number1) + " + " + str(number2) + " = " + str(number1 + number2))
#with the f-string
#print(f"Addition: {number1} + {number2} = {number1 + number2}")
name = "Alex"
age = 25
print(f"My name is {name} and I'm {age} years old.")

