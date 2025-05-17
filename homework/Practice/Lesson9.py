# BEFORE EXERCISES, LET'S DISCUSS THE FOLLOWING QUESTIONS: 

# 1. Why does the line below give an error? What can you do to fix it?
age = 26
first_name = "Ada"
print("I am " , first_name , "and I am " , age , " years old")


# 2. What will be the value of x at the end of these calculations?
#    (first try to figure it out without printing it!)
a = 5
b = 10
x = a + b
a = 2 + b
b = (a + 2) * b
x = 15

# 3. What are the problems with this conditional? How can you fix it?
weather = "sunny"

if weather == "rainy":
  print("Let's go to the museum!")
elif weather == "snowy":
  print("Let's go skiing!")
elif weather == "sunny":
  print("Let's go to the beach!")
else:
  print("Let's stay home!")



# 4. We want to print all even numbers from 1 to 100.
# but this loop doesn't print even numbers correctly for some reason.
# Can you find why and fix it?
for n in range(1, 100):
  if n % 2 == 0:
    print(n)


# 5. This code below does not execute properly. Try to figure out why.
def multiply(a, b):
  return a * b

result =  multiply(10, 10)
print(result)
print(".............\n")


### EXERCISES:


# The code below picks a random number between 1-100,
# and assigns it to the variable called "number". 
# Write code that prints out:
# - "wow it's exactly zero!" if the number is 0
# - "it's a small number" if the number is less than 10
# - "getting bigger" if the number is less than 50
# - "it's a big number" in any other case
import random
number = random.randint(1, 100)
print(number)

if number == 0:
  print("the number is:", number, "Wow its exactly zero")
elif number < 10:
  print("the number is:", number,"it's a small number")
elif number < 50:
  print("the number is:", number,"getting bigger")
else:
  print("the number is:", number,"Its a big number")



# For each fruit in the fruits list, display "It's a {fruit}" on the screen.
fruits = ["banana", "apple", "cherry", "pear"]

for fruit in fruits:
  print("Its a ", fruit)

print(".............\n")
# Slightly change your code to only print if the fruit length is smaller or equal to 5 characters

if len(fruits) <= 5:
  print("Its a ", fruit)

# You are given the following string:
magic_word = "abracadabra"

# Loop over each character in the string and print all the 'a's they are in the magic word:
for word in magic_word:
  if word == "a":
    print(word)

print(".............\n")
# Print the indices of all the 'a's in the magic word:
# Example: "aba" -> 0 and 2 (first and third letter)

for index,letter in enumerate(magic_word):
  if letter == "a":
    print(index)
  
print(".............\n")
# Finds the largest number in the list
numbers = [3,8,1,7,2,9,5,4]
largest_number= max(numbers)
print("The largest number is", largest_number)

print(".............\n")
# Compute the sum of all elements in the following list:
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sum_of_numbers = sum(lst)
print("Sum of list is ", sum_of_numbers)

print(".............\n")

# Write code that merges the two dictionaries below into one
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Hint: "Google is your best friend"
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# For the output dictionary, look over the key and values and print the key/value pairs:
merged_dict = dict1 | dict2
print(merged_dict)


print(".............\n")


#Track b

import random

#
#       OO O o o o...      ______________________ _________________
#      O     ____          |                    | |               |
#     ][_n_i_| (   ooo___  |                    | |               |
#    (__________|_[______]_|____________________|_|_______________|
#      0--0--0      0  0      0       0     0        0        0


# Exercise 1
# Draw a wagon in the terminal using 3 print operations
# This is what a wagon looks like:
#
#       ----
#      |    |
#      ------
print(" ----")
print("|    |")
print("-------")

# Exercise 2
# Define a variable train_size and give it a number of wagons
# Then, draw the train using loops and the train_size variable
# Hint: you can print stuff without a newline by using the print function as shown below
# print("Hello", end="")
# print("World", end="")
# Example:
#
#   ----  ----  ----  ----  ----  ----  ----  ----  ----  ----
#  |    ||    ||    ||    ||    ||    ||    ||    ||    ||    |
#  ------------------------------------------------------------


train_size = 4
print(" -----" * train_size)
print("|    |" * train_size)
print("------" * train_size)


# Exercise 3
# Draw a passenger with 'o' in each odd wagon
# and 'x' in the even wagons
#   ----  ----  ----  ----
#  |  x ||  o ||  x ||  o |
#  ------------------------


# Exercise 4
# Put the previous code in a function
# It takes the train size as an argument
# and draws the train


# Given a function that returns the character 'x' with 10% probability
# and 'o' with 90% probability called "get_random_passenger"
def get_random_passenger():
  r = random.randint(0, 100)
  if r <= 10:
    return 'x'
  else:
    return 'o'
  

# Exercise 5
# Change the train function so that each wagon carries a passenger with 90% probability


# Exercise 6
# After drawing the train,
# ask the user if they want to clear the screen:
# "would you like to clear the screen? (y/n)"
#
# import os
# os.system('cls' if os.name == 'nt' else 'clear')
#


# Exercise 7
# Before actually clearing the screen, wait for 3 seconds
#
# import time
# time.sleep(3)


# Exercise 8
# Let's observe the randomness by redrawing the train over and over again
# Use an infinite loop (while True)
# In the loop, draw a train of size 10, wait for 1 sec and clear the screen


# Exercise 9
# And finally, let's animate our train, choo choo!
# animate the train by using the two previously introduced functions (clear and sleep)
# you can start by drawing a train of size 10, clear, wait, draw a train of size 9, etc
# until it completely disappears from the screen


#Track c

#EXERCISE 1
#Write a program to find out how many times a number is increasing compared to the 
#previous one in the following list:

l = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

count = 0
for i,index in l:
    if i < index:
      count += 1
      print(i)

for number in range()

'''
# CODEWARS

https://www.codewars.com/kata/57f781872e3d8ca2a000007e

https://www.codewars.com/kata/55d24f55d7dd296eb9000030

https://www.codewars.com/kata/5168bb5dfe9a00b126000018



#EXERCISE 2
#Write a program to count the occurrence of each character in a given string.
#You solution should only use dictionary:
Input: "hello"
Output: {"h": 1, "e": 1, "l": 2, "o": 1}

magic_word = "abracadabra"


# MORE CODEWARS

https://www.codewars.com/kata/5715eaedb436cf5606000381

https://www.codewars.com/kata/5865918c6b569962950002a1
Hint: use the code from exercise 2.


'''