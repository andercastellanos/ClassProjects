import random

def get_player_name(player_number):
    while True:
        name = input(f"Enter Player {player_number}'s name: ")
        if len(name) >= 5:
            return name
            if player_number == player_number:
                print("Player names cannot match. Please choose a different name.")    
        else:
            print("Name should be at least 5 characters long.")

def get_player_choice(player_name):
    while True:
        print(f"{player_name}, enter your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Saw")
        try:
            choice = int(input(f"Your choice: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a valid option (1/2/3/4).")
        except ValueError:
            print("Invalid input. Please enter a valid option (1/2/3/4).")

def get_computer_choice():
    return random.randint(1, 4)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 1 and computer_choice == 3) or
        (player_choice == 2 and computer_choice == 1) or
        (player_choice == 3 and computer_choice == 2) or
        (player_choice == 4 and computer_choice in [1, 2, 3])
    ):
        return "Player wins!"
    else:
        return "Computer wins!"

def display_game_rules():
    print("Game Rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("Saw beats Rock, Paper, and Scissors")
    input("Press Enter to return to the main menu.")

def display_statistics(player1_name, player2_name, computer_name, player1_stats, player2_stats, computer_stats):
    print("Statistics:")
    print(f"{player1_name} - Wins: {player1_stats['wins']}, Losses: {player1_stats['losses']}, Ties: {player1_stats['ties']}")
    print(f"{player2_name} - Wins: {player2_stats['wins']}, Losses: {player2_stats['losses']}, Ties: {player2_stats['ties']}")
    print(f"{computer_name} - Wins: {computer_stats['wins']}, Losses: {computer_stats['losses']}, Ties: {computer_stats['ties']}")
    input("Press Enter to return to the main menu.")

def main():
    player1_name = None
    player2_name = None
    computer_name = "Computer"

    player1_stats = {"wins": 0, "losses": 0, "ties": 0}
    player2_stats = {"wins": 0, "losses": 0, "ties": 0}
    computer_stats = {"wins": 0, "losses": 0, "ties": 0}

    while True:
        print("Main Menu:")
        print("1. Play Game")
        print("2. Show Game Rules")
        print("3. Show Statistics")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if player1_name is None:
                player1_name = get_player_name(1)
            if player2_name is None:
                player2_name = get_player_name(2)

            for round_number in range(1, 4):
                print(f"Round {round_number}")
                player1_choice = get_player_choice(player1_name)
                player2_choice = get_player_choice(player2_name)
                computer_choice = get_computer_choice()

                print(f"{player1_name} chose: {player1_choice}")
                print(f"{player2_name} chose: {player2_choice}")
                print(f"{computer_name} chose: {computer_choice}")

                result1 = determine_winner(player1_choice, computer_choice)
                result2 = determine_winner(player2_choice, computer_choice)

                print(f"{player1_name}: {result1}")
                print(f"{player2_name}: {result2}")

                if result1 == "Player wins!":
                    player1_stats["wins"] += 1
                elif result1 == "Computer wins!":
                    player1_stats["losses"] += 1
                else:
                    player1_stats["ties"] += 1

                if result2 == "Player wins!":
                    player2_stats["wins"] += 1
                elif result2 == "Computer wins!":
                    player2_stats["losses"] += 1
                else:
                    player2_stats["ties"] += 1

                if result1 == "Computer wins!":
                    computer_stats["wins"] += 1
                elif result1 == "Player wins!":
                    computer_stats["losses"] += 1
                else:
                    computer_stats["ties"] += 1

            print("Game over!")
          
        elif choice == "2":
            display_game_rules()
        elif choice == "3":
            display_statistics(player1_name, player2_name, computer_name, player1_stats, player2_stats, computer_stats)
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
