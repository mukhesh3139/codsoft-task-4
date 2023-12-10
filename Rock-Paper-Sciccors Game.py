import random
def play_game():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid input. Please try again.")
play_game()