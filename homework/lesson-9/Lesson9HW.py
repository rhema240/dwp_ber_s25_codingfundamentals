# Python Exercises
import random

## Exercise 1: Student Grouping
#Imagine you are a teacher who needs to group their students into pairs or small groups. 
# Given the following list of dictionaries, create random pairs or groups of students – each pair has to have the same project choice.

students = [
    {
        "name": "Jane",
        "choice": "Project B"
    },
    {
        "name": "Janet",
        "choice": "Project A"
    },
    {
        "name": "Jack",
        "choice": "Project A"
    },
    {
        "name": "Jimmy",
        "choice": "Project B"
    },
    {
        "name": "Jean",
        "choice": "Project A"
    },
    {
        "name": "Juan",
        "choice": "Project B"
    },
    {
        "name": "Juanita",
        "choice": "Project B"
    },
    {
        "name": "Janine",
        "choice": "Project A"
    },
    {
        "name": "Jill",
        "choice": "Project B"
    },
    {
        "name": "John",
        "choice": "Project B"
    },
]



#You can use the following helper function:

def pick_random_name(list_names):
    random_name = random.choice(list_names)
    return random_name




def assign_pairs(students):
    ProjectA = []
    ProjectB = []
    Pairs = []

    for student in students:
        if student["choice"] == "Project A":
            ProjectA.append(student["name"])

        else:
            ProjectB.append(student["name"])

    print(ProjectA)
    print(ProjectB)
    

    while len(ProjectA) >= 2:
        name1 = pick_random_name(ProjectA)
        ProjectA.remove(name1)
        name2 = pick_random_name(ProjectA)
        ProjectA.remove(name2)
        Pairs.append([name1, name2])
    

assign_pairs(students)

#pairs = [pick_random_name(ProjectA), pick_random_name(ProjectB)]



# Exercise 2: Meal cost calculator
#Write a function which calculates the sum of the 3 meals for each friend (use the 'result' variable as input to your function).

def meal_sum(meals):
    return sum(meals)

print("Meal Calculator")
print("Enter the amount of money each friend spent")
print("Type 'done' when finished\n")

while True:
    breakfast = input("Jane's breakfast price (or type 'done'): ")
    if breakfast.lower() == 'done':
        break

    lunch = input("Jane's lunch price (or type 'done'): ")
    if lunch.lower() == 'done':
        break

    dinner = input("Jane's dinner price (or type 'done'): ")
    if dinner.lower() == 'done':
        break

    # Convert inputs to floats
    try:
        total_meal = [float(breakfast), float(lunch), float(dinner)]
        total = meal_sum(total_meal)
        print(f"Jane's sum is: ${total:.2f}")
    except ValueError:
        print("Please enter valid numbers for all meals.\n")
    
    break  # Exit after one friend (remove this if doing multiple friends)


#Example output:
#- Jane sum: $74


def convert_dollars(value):
    number_value = int(value.replace("$", ""))
    return number_value

#**Bonus**: - Replace the value of the name variable with your own name.


'''
## Exercise 4: Meal cost game
Run this code a few times and try to understand how the game works to then be 
able to try and win the game. Slightly change the low and high limit range to make the game easier to win.


def play_game():
    name = "ReDi"
    lower_limit = 42 
    higher_limit = 55 
    meals = inquire(name)[name] 
    total = 0

    for meal_value in meals.values(): 
        total += convert_dollars(meal_value) 
    if (lower_limit > total or higher_limit < total): 
        print("You lost.. try again!") 
    else: 
        print("Congrats! You won 👏")

# Uncomment the lines below to test your answer 👇👇👇
# play_game()






## Exercise 4: Credit Card Masking
Complete the `mask_credit_card_number` function that takes in a 16-digit credit card number and masks all but the last 4 digits.


sample_credit_card_number = '1234567890987654'
expected_credit_card_result = 'XXXXXXXXXXXX7654'

def mask_credit_card_number(credit_card_number):
    masked_credit_card_number = 'X' + 12 + 
    # write your code here!
    return masked_credit_card_number

# Uncomment the lines below to test your answer 👇👇👇
# print('Expected result: ', expected_credit_card_result)
# result = mask_credit_card_number(sample_credit_card_number)
# print('Your result:', result)

'''