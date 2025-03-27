import random

# Hangman stages (ASCII art)
hangman_stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''
]

# A list of 100 random English words
words = [
    'apple', 'banana', 'cherry', 'dragon', 'eagle', 'falcon', 'guitar', 'hacker', 'island', 'jungle',
    'kitten', 'lemon', 'monkey', 'night', 'orange', 'python', 'queen', 'rocket', 'snake', 'tiger',
    'umbrella', 'viking', 'wizard', 'xylophone', 'yogurt', 'zebra', 'anchor', 'bridge', 'candle', 'dancer',
    'engine', 'forest', 'garden', 'hammer', 'iceberg', 'jacket', 'kangaroo', 'lantern', 'mountain', 'nebula',
    'ocean', 'pencil', 'quartz', 'raven', 'saddle', 'temple', 'unicorn', 'valley', 'window', 'yarn',
    'zeppelin', 'blizzard', 'cactus', 'domino', 'emerald', 'fossil', 'geyser', 'harvest', 'igloo', 'jigsaw',
    'kitchen', 'labyrinth', 'meteor', 'necklace', 'orchid', 'palette', 'quest', 'radar', 'sapphire', 'tractor',
    'utopia', 'volcano', 'waffle', 'xenon', 'yacht', 'zipper', 'artist', 'bubble', 'castle', 'desert',
    'empire', 'flamingo', 'galaxy', 'horizon', 'inkwell', 'jungle', 'karma', 'library', 'mirror', 'noodle',
    'oxygen', 'pirate', 'quiver', 'rescue', 'spiral', 'thunder', 'upgrade', 'vortex', 'wander', 'zenith'
]

def play_game():
    word = random.choice(words)
    guessed_letters = []
    attempts = len(hangman_stages) - 1
    won = False

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(hangman_stages[len(hangman_stages) - 1 - attempts])
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Word: ", display_word.strip())
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            print("Wrong!\n")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            won = True
            break

    # Final state
    print(hangman_stages[len(hangman_stages) - 1 - attempts])
    if won:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game Over! The word was: {word}")

# Main loop
while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing Hangman!")
        break