import random
from art import stages, logo, game_over_logo, winner
from word_list import word_bank


def how_many_spaces(word):
    """Shows how many letters are in the word to guess"""
    length_of_word = []
    for n in word:
        length_of_word += '_'
    return length_of_word


def start_game():
    """Function to start the game"""

    print(logo)
    print("")

    is_game_over = False

    game_lives = 6

    game_word = random.choice(word_bank)
    game_word_length = len(game_word)

    display = how_many_spaces(game_word)

    print(stages[game_lives])
    print("")
    print(display)

    while not is_game_over:

        user_guess = input("Choose a letter: ")

        if user_guess in display:
            print("You've already guessed this letter")

        elif user_guess not in display:
            for position in range(game_word_length):
                letter = game_word[position]
                if user_guess == letter:
                    print(stages[game_lives])
                    print("")
                    print("That guess is correct!")
                    display[position] = letter

        if user_guess not in game_word:
            game_lives -= 1
            print(stages[game_lives])
            print("")
            print("That guess is incorrect! You've lost a life")

            if game_lives == 0:
                is_game_over = True
                print(game_over_logo)
                print(stages[game_lives])
                print("")
                print("You're out of lives!")
                print("")
                print(f"The correct word was {game_word}")

        if '_' not in display:
            print(winner)
            is_game_over = True
            print("You've guessed the word correctly! You win")
        print("")
        print(display)


while input("Would you like to play Hangman? Type 'y' or 'n' ") == 'y':
    start_game()

print("Maybe another time perhaps?")
