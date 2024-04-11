import random

def choose_word():
    words = ['python', 'hangman', 'game', 'programming', 'computer']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def display_hangman(attempts):
    stages = [
        '''
        -------
        |     |
        |     O
        |    \|/
        |     |
        |    / \\
        -
        ''',
        '''
        -------
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        -
        ''',
        '''
        -------
        |     |
        |     O
        |    \|/
        |     |
        |     
        -
        ''',
        '''
        -------
        |     |
        |     O
        |    \|
        |     |
        |     
        -
        ''',
        '''
        -------
        |     |
        |     O
        |     |
        |     |
        |     
        -
        ''',
        '''
        -------
        |     |
        |     O
        |    
        |     
        |     
        -
        ''',
        '''
        -------
        |     |
        |     
        |    
        |     
        |     
        -
        '''
    ]
    print(stages[attempts])

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has", len(word), "letters.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", attempts)
        display_hangman(attempts)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        elif guess in word:
            guessed_letters.append(guess)
            if set(word) == set(guessed_letters):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect guess.")
            if attempts == 0:
                print("Sorry, you're out of attempts. The word was:", word)
                break

hangman()
