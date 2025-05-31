#import colorama
#from colorama import Back, Fore, Style

print('\x1b[6;30;42m' + 'SUCESS!' + '\x1b[0m')
print('\x1b[6;33;32m' + 'SUCESS!' + '\x1b[0m')
print('\33[103mHello\33[0m')


#Method 2 
#Does not accept an invalid input

import random

GREEN = '\033[42m'
YELLOW = '\033[43m'
GRAY = '\033[100m'
RESET = '\033[0m'

WORD_LIST = [
    'apple', 'grape', 'mango', 'pearl', 'stone', 'climb',
    'brave', 'flame', 'drink', 'fresh', 'video', 'wheel',
    'plane', 'fruit', 'lemon', 'poise', 'actor', 'earth',
    'house', 'field','green', 'travel', 'house', 'stamp',
    'nurse',
]
solution = random.choice(WORD_LIST)

def give_feedback(guess, solution):
    result = []
    used = [False] * 5  

    # First pass: exact matches (green)
    for i in range(5):
        if guess[i] == solution[i]:
            result.append(GREEN + guess[i].upper() + RESET)
            used[i] = True
        else:
            result.append(None)

    # Second pass: partial matches (yellow), or gray
    for i in range(5):
        if result[i] is not None:
            continue  # already matched green
        if guess[i] in solution:
            for j in range(5):
                if guess[i] == solution[j] and not used[j]:
                    result[i] = YELLOW + guess[i].upper() + RESET
                    used[j] = True
                    break
            else:
                result[i] = GRAY + guess[i].upper() + RESET
        else:
            result[i] = GRAY + guess[i].upper() + RESET

    return result

def is_valid_guess(word):
    return len(word) == 5 and word.isalpha()

print("🎮 Welcome to Wordle in Python!\n")
attempt = 1
max_attempts = 6

while attempt <= max_attempts:
    guess = input(f"Attempt {attempt}/{max_attempts} - Enter a 5-letter word: ").lower()

    if not is_valid_guess(guess):
        print("Word not in List")
        continue

    if guess not in WORD_LIST:
        print("Word not in list.")
        continue

    feedback = give_feedback(guess, solution)
    print(" ".join(feedback))  # Prints the colored feedback

    if guess == solution:
        print("🎉 You guessed the word!")
        break

    attempt += 1

else:
    print(f"❌ Out of attempts! The word was: {solution.upper()}")

