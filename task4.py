# Rock-Paper-Scissor Game

import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"


def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)


def play_round():
    user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        return None, None, None

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    return user_choice, computer_choice, result


def play_again():
    return input("Do you want to play again? (yes or no): ").lower() == 'yes'


def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to the Rock-Paper-Scissors Game!")

    while True:
        user_choice, computer_choice, result = play_round()

        if user_choice and computer_choice:
            display_result(user_choice, computer_choice, result)

            
            if result == "You win!":
                user_score += 1
            elif result == "You lose!":
                computer_score += 1


            print(f"\nScore: You {user_score} - {computer_score} Computer")

        if not play_again():
            print("\nThanks for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break


if __name__ == "__main__":
    play_game()
