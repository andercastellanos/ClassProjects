import random

# Initialize statistics as a dictionary with player names as keys
# and their corresponding statistics as values
player_statistics = {}

def initialize_players():
    global player_statistics
    player1_name = input("What is the name of the first human player? ")
    player2_name = input("What is the name of the second human player? ")

    # Ensure player names are unique
    while player2_name == player1_name:
        print("Second player name must be different from the first player.")
        player2_name = input("What is the name of the second human player? ")

    player_statistics[player1_name] = {'rounds_won': 0, 'rounds_lost': 0, 'rounds_tied': 0, 'games_won': 0, 'games_lost': 0}
    player_statistics[player2_name] = {'rounds_won': 0, 'rounds_lost': 0, 'rounds_tied': 0, 'games_won': 0, 'games_lost': 0}
    player_statistics['Computer'] = {'rounds_won': 0, 'rounds_lost': 0, 'rounds_tied': 0, 'games_won': 0, 'games_lost': 0}

def display_menu():
    print("\nMenu:")
    print("1. Play game")
    print("2. Show game rules")
    print("3. Show statistics")
    print("4. Exit")

def show_rules():
    print("\nRules:")
    print("Rock breaks scissors and Saw, but loses against paper.")
    print("Scissors cut paper, but lose against rock and Saw.")
    print("Paper covers rock, but loses against scissors and Saw.")
    print("Saw cuts through scissors and paper, but loses against rock.")
    print("If both players make the same selection, it's a tie.")

def display_statistics():
    print("\n[Statistics]")
    for player_name, stats in player_statistics.items():
        print(f"{player_name}: Rounds Won={stats['rounds_won']}, Rounds Lost={stats['rounds_lost']}, Rounds Tied={stats['rounds_tied']}, Games Won={stats['games_won']}, Games Lost={stats['games_lost']}")

def play_round(player1, player2):
    choices = ["rock", "paper", "scissors", "saw"]
    player1_choice = input(f"{player1}, choose your weapon (rock, paper, scissors, saw): ").lower()
    while player1_choice not in choices:
        print("Invalid choice. Choose from rock, paper, scissors, saw.")
        player1_choice = input(f"{player1}, choose your weapon (rock, paper, scissors, saw): ").lower()

    computer_choice = random.choice(choices)

    print(f"{player1} chose {player1_choice}")
    print(f"Computer chose {computer_choice}")

    # Determine the winner of the round for player1
    if (player1_choice == "rock" and computer_choice in ["scissors", "saw"]) or \
       (player1_choice == "scissors" and computer_choice == "paper") or \
       (player1_choice == "paper" and computer_choice == "rock") or \
       (player1_choice == "saw" and computer_choice in ["scissors", "paper"]):
        print(f"{player1} wins this round!")
        player_statistics[player1]['rounds_won'] += 1
        player_statistics['Computer']['rounds_lost'] += 1
    elif player1_choice == computer_choice:
        print("It's a tie!")
        player_statistics[player1]['rounds_tied'] += 1
        player_statistics['Computer']['rounds_tied'] += 1
    else:
        print("Computer wins this round!")
        player_statistics['Computer']['rounds_won'] += 1
        player_statistics[player1]['rounds_lost'] += 1

    # Determine the winner of the round for player2
    player2_choice = input(f"{player2}, choose your weapon (rock, paper, scissors, saw): ").lower()
    while player2_choice not in choices:
        print("Invalid choice. Choose from rock, paper, scissors, saw.")
        player2_choice = input(f"{player2}, choose your weapon (rock, paper, scissors, saw): ").lower()

    print(f"{player2} chose {player2_choice}")

    # Determine the winner of the round for player2
    if (player2_choice == "rock" and computer_choice in ["scissors", "saw"]) or \
       (player2_choice == "scissors" and computer_choice == "paper") or \
       (player2_choice == "paper" and computer_choice == "rock") or \
       (player2_choice == "saw" and computer_choice in ["scissors", "paper"]):
        print(f"{player2} wins this round!")
        player_statistics[player2]['rounds_won'] += 1
        player_statistics['Computer']['rounds_lost'] += 1
    elif player2_choice == computer_choice:
        print("It's a tie!")
        player_statistics[player2]['rounds_tied'] += 1
        player_statistics['Computer']['rounds_tied'] += 1
    else:
        print("Computer wins this round!")
        player_statistics['Computer']['rounds_won'] += 1
        player_statistics[player2]['rounds_lost'] += 1

def play_game():
    global player_statistics

    # Get the player names dynamically from the dictionary
    player_names = list(player_statistics.keys())
    player1 = player_names[0]
    player2 = player_names[1]

    # Reset round statistics
    player_statistics[player1]['rounds_won'] = player_statistics[player1]['rounds_lost'] = player_statistics[player1]['rounds_tied'] = 0
    player_statistics[player2]['rounds_won'] = player_statistics[player2]['rounds_lost'] = player_statistics[player2]['rounds_tied'] = 0
    player_statistics['Computer']['rounds_won'] = player_statistics['Computer']['rounds_lost'] = player_statistics['Computer']['rounds_tied'] = 0

    # Play rounds until a player wins 3 rounds or loses 3 rounds
    while player_statistics[player1]['rounds_won'] < 3 and player_statistics[player2]['rounds_won'] < 3 \
            and player_statistics[player1]['rounds_lost'] < 3 and player_statistics[player2]['rounds_lost'] < 3:
        play_round(player1, player2)

    # Determine the winner of the game
    if player_statistics[player1]['rounds_won'] >= 3:
        print(f"\n{player1} wins the game!")
        player_statistics[player1]['games_won'] += 1
        player_statistics[player2]['games_lost'] += 1
    elif player_statistics[player2]['rounds_won'] >= 3:
        print(f"\n{player2} wins the game!")
        player_statistics[player2]['games_won'] += 1
        player_statistics[player1]['games_lost'] += 1

    else:
        print("\nGame tied!")
        
        player_statistics['Computer']['games_won'] += 1
        player_statistics[player1]['games_lost'] += 1
        player_statistics[player2]['games_lost'] += 1



def main():
    initialize_players()

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "3":
            display_statistics()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
