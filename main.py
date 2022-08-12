from random import choice

computer_choices = ["rock", "paper", "scissors"]


def game():
    end_number = 3
    userScore = 0
    computerScore = 0

    while userScore <= end_number or computerScore <= end_number:

        player_game = str(input("Play your game : ")).strip().lower()
        computer_choice = choice(computer_choices)

        if player_game not in computer_choices:
            print("Please enter valid game....")

        if player_game == "rock" and computer_choice == "paper":
            computerScore += 1
            print(f"Your choice is : {player_game} and computer_choice is : {computer_choice}\n",
                  f"Your score is : {userScore} and computer_score is : {computerScore}")

        elif player_game == "rock" and computer_choice == "scissors":
            userScore += 1
            print(f"Your choice is : {player_game} and computer_choice is : {computer_choice}\n",
                  f"Your score is : {userScore} and computer_score is : {computerScore}")

        elif player_game == "paper" and computer_choice == "scissors":
            computerScore += 1
            print(f"Your choice is : {player_game} and computer_choice is : {computer_choice}\n",
                  f"Your score is : {userScore} and computer_score is : {computerScore}")

        elif player_game == "paper" and computer_choice == "rock":
            userScore += 1
            print(f"Your choice is : {player_game} and computer_choice is : {computer_choice}\n",
                  f"Your score is : {userScore} and computer_score is : {computerScore}")

        elif player_game == "scissors" and computer_choice == "rock":
            computerScore += 1
            print(f"Your choice is : {player_game} and computer_choice is : {computer_choice}\n",
                  f"Your score is : {userScore} and computer_score is : {computerScore}")

        elif player_game == "scissors" and computer_choice == "paper":
            userScore += 1
            print(f"Your choice is : {player_game} and computer_choice is : {computer_choice}\n",
                  f"Your score is : {userScore} and computer_score is : {computerScore}")

        elif player_game == computer_choice:
            print(f"Your choice is : {player_game} and computer_choice is : {computer_choice}\n",
                  f"Your score is : {userScore} and computer_score is : {computerScore}")

        if userScore == end_number:
            print("You Win!!!")
            print(f"Your choice is : {player_game} and computer_choice is : {computer_choice}\n",
                  f"Your score is : {userScore} and computer_score is : {computerScore}")
            break

        elif computerScore == end_number:
            print("You lost!!")
            print(f"Your choice is : {player_game} and computer_choice is : {computer_choice}\n",
                  f"Your score is : {userScore} and computer_score is : {computerScore}")
            break


if __name__ == "__main__":
    game()
