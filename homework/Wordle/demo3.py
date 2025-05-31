
import random


GREEN = '\033[42m'
YELLOW = '\033[43m'
GRAY = '\033[100m'
RESET = '\033[0m'

word_list = ['spain', 'japan', 'sudan', 'niger', 'malta', 
             'egypt','apple', 'grape', 'mango', 'pearl', 'stone', 
             'brave', 'flame', 'drink', 'fresh', 'video', 'wheel',
             'plane', 'fruit', 'lemon', 'poise', 'actor', 'earth',
             'house', 'field','green', 'travel', 'house', 'stamp',
             'nurse', 'climb'
] 

def play_wordle():

    wordle = random.choice(word_list)
    max_attempts = 6

    print("Welcome to Wordle! Guess the 5-letter word.")

    for attempt in range(max_attempts):
        
        while True:
            guess = input(f"Attempt {attempt + 1}/{max_attempts}: ").lower()
           
            if len(guess) == 5 and guess.isalpha(): 
                break
            print("Word not in List!")

    
        feedback = []
        for i in range(len(wordle)):
            if guess[i] == wordle[i]:
                feedback.append(GREEN + guess[i].upper() + RESET )
            elif guess[i] in wordle:
                feedback.append (YELLOW + guess[i].upper() + RESET )
            else:
                feedback.append (GRAY + guess[i].upper() + RESET )

        print("".join(feedback))  # Show feedback in Wordle format

        if guess == wordle:
            print("🎉 Congratulations! You guessed the word correctly!")
            break
    else:
        print(f"😢 Out of attempts! The correct word was '{wordle}'.")

play_wordle()
