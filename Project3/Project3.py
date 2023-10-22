from os import system, name
import random

WEAPONS = ["Rock", "Paper", "Scissors", "Saw"]
players = ["Player 1", "Player 2", "Computer"]
player_stats = {
    "Player 1": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0},
    "Player 2": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0},
    "Computer": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0}
}

def get_player_name(player_number):
    while True:
        player_name = input(f"What is the name of Player {player_number}? ").strip()
        if 5 <= len(player_name) <= 20:
            return player_name
        else:
            print("Player name must be between 5 and 20 characters.")

def get_player_choice(player_name):
    while True:
        player_choice = input(f"{player_name}, select your weapon (Rock, Paper, Scissors, or Saw): ").strip().title()
        if player_choice in WEAPONS:
            return player_choice
        else:
            print("Invalid weapon. Choose from Rock, Paper, Scissors, or Saw.")

def play_round():
    for player_name in players[:2]:
        player_choice = get_player_choice(player_name)
        computer_choice = random.choice(WEAPONS)

        print(f"{player_name} chose {player_choice}.")
        print(f"Computer chose {computer_choice}.")

        round_winner = determine_round_winner(player_choice, computer_choice)

        if round_winner == player_name:
            print(f"{player_name} wins this round!")
            player_stats[player_name]["rounds_won"] += 1
        elif round_winner == "Computer":
            print("Computer wins this round!")
            player_stats["Computer"]["rounds_won"] += 1
        else:
            print("It's a tie!")
            player_stats[player_name]["rounds_tied"] += 1
            player_stats["Computer"]["rounds_tied"] += 1

def determine_round_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    if (
        (player_choice == "Rock" and (computer_choice == "Scissors" or computer_choice == "Saw")) or
        (player_choice == "Scissors" and computer_choice == "Paper") or
        (player_choice == "Paper" and (computer_choice == "Rock")) or
        (player_choice == "Saw" and (computer_choice == "Scissors" or computer_choice == "Paper"))
    ):
        return player_choice
    return "Computer"

def determine_game_winner(player1_rounds_won, player2_rounds_won):
    if player1_rounds_won > player2_rounds_won:
        return "Player 1"
    elif player2_rounds_won > player1_rounds_won:
        return "Player 2"
    else:
        return "Tie"

def determine_overall_winner():
    player1_wins = player_stats["Player 1"]["games_won"]
    player2_wins = player_stats["Player 2"]["games_won"]
    computer_wins = player_stats["Computer"]["games_won"]

    player1_losses = player_stats["Player 1"]["games_lost"]
    player2_losses = player_stats["Player 2"]["games_lost"]
    computer_losses = player_stats["Computer"]["games_lost"]

    max_wins = max(player1_wins, player2_wins, computer_wins)
    min_losses = min(player1_losses, player2_losses, computer_losses)

    if player1_wins == player2_wins and player1_losses == player2_losses:
        print("Overall Human Winner: Tie")
    else:
        if player1_wins > player2_wins:
            print(f"Overall Human Winner: {player_stats['Player 1']['name']}")
        else:
            print(f"Overall Human Winner: {player_stats['Player 2']['name']}")

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def play():
    round_number = 0
    player1_rounds_won = 0
    player2_rounds_won = 0

    while round_number < 3:
        print("Round", round_number + 1)
        play_round()

        round_number += 1

    player1_rounds_won = player_stats["Player 1"]["rounds_won"]
    player2_rounds_won = player_stats["Player 2"]["rounds_won"]

    game_winner = determine_game_winner(player1_rounds_won, player2_rounds_won)

    if game_winner == "Player 1":
        print("Player 1 wins the game!")
        player_stats["Player 1"]["games_won"] += 1
        player_stats["Computer"]["games_lost"] += 1
    elif game_winner == "Player 2":
        print("Player 2 wins the game!")
        player_stats["Player 2"]["games_won"] += 1
        player_stats["Computer"]["games_lost"] += 1
    else:
        print("It's a tie game!")

    play_again = input("Do you want to play another game? (yes/no): ").strip().lower()
    if play_again == "yes":
        play()

def menu():
    player_stats["Player 1"]["name"] = get_player_name(1)
    player_stats["Player 2"]["name"] = get_player_name(2)

    while player_stats["Player 1"]["name"] == player_stats["Player 2"]["name"]:
        print("Player 2's name must be different from Player 1's name")
        player_stats["Player 2"]["name"] = get_player_name(2)

    while True:
        print("Menu:")
        print("1. Play game")
        print("2. Show game rules")
        print("3. Show statistics")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            play()
        elif choice == '2':
            rules()
        elif choice == '3':
            stats()
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def stats():
    print("Statistics:")
    for player_name in player_stats.keys():
        player_info = player_stats[player_name]
        rounds_won = player_info["rounds_won"]
        rounds_lost = player_info["rounds_lost"]
        rounds_tied = player_info["rounds_tied"]
        games_won = player_info["games_won"]
        games_lost = player_info["games_lost"]
        player_name = player_info.get("name", player_name)  # Update player_name with name attribute

        print(f"{player_name} - Rounds won: {rounds_won}, Rounds lost: {rounds_lost}, Rounds tied: {rounds_tied}, Games won: {games_won}, Games lost: {games_lost}")

    determine_overall_winner()

    input("Press Enter to return to the menu...")

def rules():
    print("Game Rules:")
    print("a. Rock breaks scissors and Saw, so rock wins over scissors and saw. Rock loses against paper.")
    print("b. Scissors cut paper, so scissors win over paper. Scissors lose against rock and Saw.")
    print("c. Paper covers rock, so paper wins over rock. Paper loses against scissors and Saw.")
    print("d. Saw cuts through scissors and paper, so Saw wins over scissors and paper. Saw loses against rock.")
    print("e. If player and computer make the same selection, there is a tie.")
    input("Press Enter to return to the menu...")

if __name__ == "__main__":
    menu()