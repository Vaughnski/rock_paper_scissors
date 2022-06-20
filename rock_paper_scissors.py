# 6.17.22 Andrew Vaughn

# libraries
import random
import time


# function purpose is to print lines with 1-second delay for UX
def print_pause(print_statement):
    print(print_statement)
    time.sleep(1)


# this function welcomes the user, accepts their choice
def introduction(computer_choice):
    print_pause("Welcome to Rock Paper Scissors Extravaganza!")
    print_pause("Since I am a computer, I am really good")
    user_choice = validate_input("Please select an option: "
                                 "rock, paper or scissors ",
                                 ['rock', 'paper', 'scissors'])
    display_result(computer_choice, user_choice)


# function displays result
def display_result(computer_choice, user_choice):
    print_pause(f"You selected {user_choice}. Computer selected " +
                f"{computer_choice}.")
    print_pause(determine_winner(computer_choice, user_choice))
    determine_play_again()


# function's purpose is to determine the winner
def determine_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return 'Tie'

    elif ((computer_choice == 'rock' and user_choice == 'paper') or
          (computer_choice == 'paper' and user_choice == 'scissors') or
          (computer_choice == 'scissors' and user_choice == 'rock')):
        return 'You win!'

    elif ((computer_choice == 'paper' and user_choice == 'rock') or
          (computer_choice == 'scissors' and user_choice == 'paper') or
          (computer_choice == 'rock' and user_choice == 'scissors')):
        return 'Computer wins!'


def validate_input(prompt, options):
    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        else:
            print_pause("Input invalid, please try again.")


# this function serves to initialize variables and pass them to the intro
def play_game():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    introduction(computer_choice)


def determine_play_again():
    play_again = validate_input("Would you like to play again? (yes/no)",
                                ['yes', 'no'])
    if play_again == 'yes':
        play_game()
    else:
        quit()


# used to start the game
play_game()
