import random

def play_hangman():
    # 1. Use a small list of 5 predefined words (lists, strings)
    words = ["python", "coding", "agent", "laptop", "screen"]
    
    # Key concept: random
    word_to_guess = random.choice(words)
    guessed_letters = []
    
    # 2. Limit incorrect guesses to 6
    incorrect_guesses_allowed = 6
    incorrect_guesses = 0
    
    print("Welcome to Hangman!")
    
    # Key concept: while loop
    while incorrect_guesses < incorrect_guesses_allowed:
        # Build the current display string
        display = ""
        for letter in word_to_guess:
            # Key concept: if-else
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
                
        print(f"\nWord: {display.strip()}")
        
        # Check if they won
        if "_" not in display:
            print("Congratulations! You guessed the word correctly!")
            return
            
        # Basic console input/output
        guess = input("Guess a single letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        # Key concept: if-else
        if guess in word_to_guess:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            guesses_left = incorrect_guesses_allowed - incorrect_guesses
            print(f"Incorrect! You have {guesses_left} guesses left.")
            
    print(f"\nGame Over! You've run out of guesses. The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()