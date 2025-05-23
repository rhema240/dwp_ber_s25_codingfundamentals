'''
import random

WORD_LIST = ['apple', 'grape', 'mango', 'pearl', 'stone', 'climb', 'brave', 'flame', 'drink', 'fresh', 'video', 'wheel', 'plane', 'fruit']

solution = random.choice(WORD_LIST)

def give_feedback(guess, solution):
    result = []
    for i in range(5):
        if guess[i] == solution[i]:
            result.append('🟩')
        elif guess[i] in solution:
            result.append('🟨')
        else:
            result.append('⬛')
    return ''.join(result)

#Does not stop the user from entering the guess
def is_valid_guess(word):
    return len(word) == 5 and word.isalpha()

print("Welcome to Wordle in Python!")
attempts = 6

for attempt in range(attempts):
    guess = input(f"Attempt {attempt + 1}/{attempts} - Enter a 5-letter word: ").lower()
    
    if not is_valid_guess(guess) and  guess not in WORD_LIST:
        print("Word is not in list")
        continue

    feedback = give_feedback(guess, solution)
    print("Feedback:", feedback)

    if guess == solution:
        print("🎉 Congratulations! You guessed the word!")
        break
else:
    print(f"❌ Out of attempts! The word was: {solution}")

'''
#Method 2 
#Does not accept an invalid input

import random

WORD_LIST = ['apple', 'grape', 'mango', 'pearl', 'stone', 'climb', 'brave', 'flame', 'drink', 'fresh', 'video', 'wheel', 'plane', 'fruit']
solution = random.choice(WORD_LIST)

def give_feedback(guess, solution):
    result = []
    for i in range(5):
        if guess[i] == solution[i]:
            result.append('🟩')
        elif guess[i] in solution:
            result.append('🟨')
        else:
            result.append('⬛')
    return ''.join(result)

def is_valid_guess(word):
    return len(word) == 5 and word.isalpha()

print("Welcome to Wordle in Python!")
attempt = 1
max_attempts = 6

while attempt <= max_attempts:
    guess = input(f"Attempt {attempt}/{max_attempts} - Enter a 5-letter word: ").lower()

    if not is_valid_guess(guess):
        print("❌ Invalid input: Only 5-letter alphabetic words allowed. Try again.")
        continue

    if guess not in WORD_LIST:
        print("❌ Word not in the list. Try again.")
        continue

    feedback = give_feedback(guess, solution)
    print("Feedback:", feedback)

    if guess == solution:
        print("🎉 Congratulations! You guessed the word!")
        break

    attempt += 1

else:
    print(f"❌ Out of attempts! The word was: {solution}")






