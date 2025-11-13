
import random

STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]
WORDS = ["python", "winterblues",  "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage for the current number of mistakes."""
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word, "\n")

def print_game_header():
    """Print the header at start of the game"""
    print("⭐" * 25)
    print(" WELCOME TO SNOWMAN MELTDOWN! ".center(30, "~"))
    print("⭐" * 25)
    print("\nGuess the word before your snowman melts!\n")

def get_valid_guess(guessed_letters):
    """Validate and return a single unused letter from user input.
    Return validated lower case letter."""
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one character.")
        elif not guess.isalpha():
            print("Please enter a letter (a-z).")
        elif guess in guessed_letters:
            print("You have already guessed this letter. Try again.")
        else:
            return guess
def play_game():
    """The main function using the gameplay loop"""
    secret_word = get_random_word()
    print_game_header()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check if player has won
        if all(letter in guessed_letters for letter in secret_word):
            print("\n CONGRATULATIONS! YOU SAVED THE SNOWMAN! ")
            print(f"The word was: {secret_word.upper()}")
            print("⭐" * 25)
            return

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Incorrect! Snowman melts...")
        else:
            print("Correct!")

        # This executes if while loop completes normally (player lost)
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Oh no! The snowman melted completely!")
    print(f"The word was: {secret_word}")


if __name__ == "__main__":
    while True:
        play_game()
        user_input = input(
            "Would you like to end the game? Please press 'n'. If you would like to continue, press any other key.: ")
        if user_input.lower() == "n":
            break
