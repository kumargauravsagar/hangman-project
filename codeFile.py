import random
import string

def choose_word(difficulty):
    if difficulty == "easy":
        words = ["apple", "banana", "orange", "grape", "pear"]
    elif difficulty == "medium":
        words = ["python", "java", "javascript", "ruby", "php"]
    else:
        words = ["hangman game", "machine learning", "openai", "artificial intelligence", "deep learning"]
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters or letter == ' ':
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def display_available_letters(guessed_letters):
    available_letters = [letter for letter in string.ascii_lowercase if letter not in guessed_letters]
    return ' '.join(available_letters)

def display_hangman(turns):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[turns]

def hangman():
    print("Welcome to Hangman!")
    
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
        if difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level. Please choose easy, medium, or hard.")
            continue
        word = choose_word(difficulty)
        guessed_letters = []
        attempts = 6
        turns = 0

        print("\nTry to guess the word.")
        while attempts > 0:
            print("\nAttempts left:", attempts)
            print(display_hangman(turns))
            print(display_word(word, guessed_letters))
            print("Available letters:", display_available_letters(guessed_letters))

            guess = input("Enter a letter: ").lower()

            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                if set(word.replace(' ', '')) == set(guessed_letters):
                    print("Congratulations! You guessed the word:", word)
                    break
            else:
                print("Incorrect guess.")
                attempts -= 1
                turns += 1

        else:
            print(display_hangman(turns))
            print("You ran out of attempts. The word was:", word)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing Hangman!")
            break

hangman()
