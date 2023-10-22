from os import system, name
import random

players = ["", "", "Computer"]
player_stats = {
    "Player 1": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0, "games_tied": 0},
    "Player 2": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0, "games_tied": 0},
    "Computer": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0, "games_tied": 0}
}

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_player_name(player_number):
    while True:
        name = input(f"What is the name of Player {player_number}?: ")
        if 5 <= len(name) <= 20:
            return name
        else:
            print("Name should be 5-20 characters long.")

def get_player_choice(player_name):
    print(f"{player_name}, enter your choice:\n")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Saw\n")
    while True:
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

def determine_round_winner(player_choice, computer_choice):
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

def determine_game_winner(player1_rounds_won, player2_rounds_won, computer_rounds_won):
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

def rules():
    print("--------------------\nGAME RULES\n--------------------\n")
    print("Winner of the round will be determined as follow:\n")
    print("Rock breaks scissors and Saw therefore rock wins over scissors and saw. Rock loses against paper.\n")
    print("Scissors cut paper therefore scissors win over paper. Scissors lose against rock and Saw.\n")
    print("Paper covers rock therefore paper wins over rock. Paper loses against scissors and Saw.\n")
    print("Saw cuts through scissors and paper therefore saw wins over scissors and paper. Saw loses against rock.\n")
    print("If player and computer make the same selection, there is a tie.\n")
    print("The winner of the game is one who won most rounds. The program must account for ties.\n")
    print("Overall human winner is based on the greater number of won games against the computer and least games lost (must account for tie between human players).\n")
    input("Press ENTER to return to the main menu.")

def stats(player1_name, player2_name, computer_name):
    print("--------------------\nSTATISTICS\n--------------------\n")

    index = 0

    for player_name in player_stats.keys():
        player_info = player_stats[player_name]
        rounds_won = player_info["rounds_won"]
        rounds_lost = player_info["rounds_lost"]
        rounds_tied = player_info["rounds_tied"]
        games_won = player_info["games_won"]
        games_lost = player_info["games_lost"]
        games_tied = player_info["games_tied"]
        player_name = player_info.get("name", player_name)  # Update player_name with name attribute

        print(f"{players[index]} - Rounds won: {rounds_won}, Rounds lost: {rounds_lost}, Rounds tied: {rounds_tied}, Games won: {games_won}, Games lost: {games_lost}, Games tied: {games_tied}")
        index = index + 1

    input("\nPress ENTER to return to the main menu.")

def play(player1_name, player2_name, computer_name):
    for round_number in range(1, 4):
        print(f"--------------------\nROUND {round_number}\n--------------------\n")
        player1_choice = get_player_choice(player1_name)
        print("")
        player2_choice = get_player_choice(player2_name)
        print("")
        computer_choice = get_computer_choice()

        print(f"--------------------\nROUND {round_number} RESULTS\n--------------------\n")
        print(f"{player1_name} chose: {player1_choice}")
        print(f"{player2_name} chose: {player2_choice}")
        print(f"{computer_name} chose: {computer_choice}")

        result1 = determine_round_winner(player1_choice, computer_choice)
        result2 = determine_round_winner(player2_choice, computer_choice)
        print("")
        print(f"{player1_name}: {result1}")
        print(f"{player2_name}: {result2}")
        print("")

        if result1 == "Player wins!":
            player_stats["Player 1"]["rounds_won"] += 1
        elif result1 == "Computer wins!":
            player_stats["Player 1"]["rounds_lost"] += 1
        else:
            player_stats["Player 1"]["rounds_tied"] += 1

        if result2 == "Player wins!":
            player_stats["Player 2"]["rounds_won"] += 1
        elif result2 == "Computer wins!":
            player_stats["Player 2"]["rounds_lost"] += 1
        else:
            player_stats["Player 2"]["rounds_tied"] += 1

        if result1 == "Computer wins!":
            player_stats["Computer"]["rounds_won"] += 1
        elif result1 == "Player wins!":
            player_stats["Computer"]["rounds_lost"] += 1
        else:
            player_stats["Computer"]["rounds_tied"] += 1

        if round_number % 3 == 0:
            for player_name in player_stats.keys():
                rounds_won = player_stats[player_name]["rounds_won"]
                if rounds_won >= 3:
                    player_stats[player_name]["games_won"] += 1
                    player_stats[player_name]["rounds_won"] = 0
            for player_name in player_stats.keys():
                rounds_lost = player_stats[player_name]["rounds_lost"]
                if rounds_lost >= 3:
                    player_stats[player_name]["games_lost"] += 1
                    player_stats[player_name]["rounds_lost"] = 0

    print("GAME OVER!\n")
    input("Press ENTER to return to the main menu.")

def menu():
    while players[0] == players[1]:
        clear()

        if (players[0] == players[1]) & (players[0] != "") & (players[0] != None):
            print("Player names cannot match. Please choose a different name.")
                
        players[0] = get_player_name(1)
        players[1] = get_player_name(2)
        
    while True:
        clear()
        print("--------------------\nMAIN MENU\n--------------------\n")
        print("1. Play Game")
        print("2. Show Game Rules")
        print("3. Show Statistics")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            clear()
            play(players[0], players[1], players[2])
        elif choice == "2":
            clear()
            rules()
        elif choice == "3":
            clear()
            stats(players[0], players[1], players[2])
        elif choice == "4":
            print("\nGoodbye!\n")
            break

if __name__ == "__main__":
    menu()

