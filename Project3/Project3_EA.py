from os import system, name
import random

# Create list of player names in the order that player selections are made.
players = ["", "", "Computer"]

# Create dictionary of weapons with corresponding key/value pairs.
weapons = {"1": "Rock", "2": "Paper", "3": "Scissors", "4": "Saw"}

# Create 2D dictionary (array) to hold all player statistics.
player_stats = {
    "1": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0, "games_tied": 0},
    "2": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0, "games_tied": 0},
    "3": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0, "games_tied": 0}
}

# Create 2D dictionary (array) to hold all player v. computer win/lose/tie outcomes.
player_v_computer_matrix = {
    "1": {"1": 0, "2": -1, "3": 1, "4": 1},
    "2": {"1": 1, "2": 0, "3": -1, "4": -1},
    "3": {"1": -1, "2": 1, "3": 0, "4": -1},
    "4": {"1": -1, "2": 1, "3": 1, "4": 0}
}

# Create 3D dictionary (array) to hold all win/lose/tie outcomes for the round with ALL THREE PLAYERS accounted for.
# Structure of third dimesion values is Win:X,X,X or Tie:X,X,X
# The third dimesion values denote the round outcome (e.g. Win/Tie) and the player number(s) associated with that status.
round_win_matrix = {
    "1": {
        "1": { "1": "Tie:1,2,3", "2": "Win:3", "3": "Tie:1,2", "4": "Tie:1,2", },
        "2": { "1": "Win:2", "2": "Tie:2,3", "3": "Tie:1,2,3", "4": "Tie:1,2,3", },
        "3": { "1": "Tie:1,3", "2": "Tie:1,2,3", "3": "Win:1", "4": "Win:1", },
        "4": { "1": "Tie:1,3", "2": "Tie:1,2,3", "3": "Win:1", "4": "Win:1", },
    },
    "2": {
        "1": { "1": "Win:1", "2": "Tie:1,3", "3": "Tie:1,2,3", "4": "Tie:1,2,3", },
        "2": { "1": "Tie:1,2", "2": "Tie:1,2,3", "3": "Win:3", "4": "Win:3", },
        "3": { "1": "Tie:1,2,3", "2": "Win:2", "3": "Tie:2,3", "4": "Win:3", },
        "4": { "1": "Tie:1,2,3", "2": "Win:2", "3": "Win:2", "4": "Tie:2,3", },
    },
    "3": {
        "1": { "1": "Tie:2,3", "2": "Tie:1,2,3", "3": "Win:2", "4": "Win:2", },
        "2": { "1": "Tie:1,2,3", "2": "Win:1", "3": "Tie:1,3", "4": "Win:3", },
        "3": { "1": "Win:3", "2": "Tie:1,2", "3": "Tie:1,2,3", "4": "Win:3", },
        "4": { "1": "Win:3", "2": "Win:2", "3": "Win:2", "4": "Tie:2,3", },
    },
    "4": {
        "1": { "1": "Tie:2,3", "2": "Tie:1,2,3", "3": "Win:2", "4": "Win:2", },
        "2": { "1": "Tie:1,2,3", "2": "Win:1", "3": "Win:1", "4": "Tie:1,3", },
        "3": { "1": "Win:3", "2": "Win:1", "3": "Win:1", "4": "Tie:1,3", },
        "4": { "1": "Win:3", "2": "Tie:1,2", "3": "Tie:1,2", "4": "Tie:1,2,3", },
    },
}

# clear() - Function to clear the screen.
def clear():
    print("\033[H\033[J", end="")

# get_player_name - Function to input the player names at runtime. Validates for correct length.
# Attribute player_number - corresponds to the player index in order being played (Valid: 0,1).
# Return name - the name of the player being input.
def get_player_name(player_number):
    playerString = ""
    if player_number == 0: playerString = "first"
    elif player_number == 1: playerString = "second"

    while True:
        name = input(f"What is the name of the {playerString} player? ")
        if 5 <= len(name) <= 20:
            return name
        else:
            print("Name should be 5-20 characters long.")

# get_player_choice - Function to output round screen and input the player weapon choice during a round. Valiudates input.
# Attribute player_name - Player name as a string.
# Returns the string version of the numerical weapon choice.
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
                return str(choice)
            else:
                print("Invalid choice. Please enter a valid option (1/2/3/4).")
        except ValueError:
            print("Invalid input. Please enter a valid option (1/2/3/4).")

# get_computer_choice - Function to randomly select the computer's weapon choice during a round. Valiudates input.
# Returns the string version of the numerical weapon choice.
def get_computer_choice():
    return str(random.randint(1, 4))

# determine_round_winner - Determines round winner, displays this information to the users, and updates the game statistics accrodingly.
# Attributes player1_choice, player2_choice, computer_choice - String representation of the user/computer's weapon choices.
# Returns a six-element list representing each user's wins/losses and the computer's wins/losses.
def determine_round_winner(player1_choice, player2_choice, computer_choice):
    rounds_won = [0, 0, 0]
    rounds_lost = [0, 0, 0]
    rounds_tied = [0, 0, 0]
    
    print("")

    round_result = round_win_matrix[player1_choice][player2_choice][computer_choice]
    parsed_list = round_result.split(":")
    round_winner_or_tie = parsed_list[0]
    round_player_indices = parsed_list[1].split(",")

    if round_winner_or_tie == "Win":
        print("Round Winner:\n------------")
        for player_name in player_stats.keys():
            if player_name in round_player_indices:
                print(f"{players[int(player_name) - 1]} wins!")
                player_stats[player_name]["rounds_won"] += 1
                rounds_won[int(player_name) - 1] += 1
            else:
                player_stats[player_name]["rounds_lost"] += 1
                rounds_lost[int(player_name) - 1] += 1
    elif round_winner_or_tie == "Tie":
        print("Tied:\n-----")
        for player_name in player_stats.keys():
            if player_name in round_player_indices:
                print(f"{players[int(player_name) - 1]}")
                player_stats[player_name]["rounds_tied"] += 1
                rounds_tied[int(player_name) - 1] += 1
            else:
                player_stats[player_name]["rounds_lost"] += 1
                rounds_lost[int(player_name) - 1] += 1

    print("")

    print("Individual Results:\n------------------")
    # Player 1 vs. Computer Result
    if player_v_computer_matrix[player1_choice][computer_choice] == 0:
        print(f"{players[0]}: It's a tie against the computer!")
    elif player_v_computer_matrix[player1_choice][computer_choice] == -1:
        print(f"{players[0]}: Computer wins against the player!")
    elif player_v_computer_matrix[player1_choice][computer_choice] == 1:
        print(f"{players[0]}: Player wins against the computer!")

    # Player 2 vs. Computer Result
    if player_v_computer_matrix[player2_choice][computer_choice] == 0:
        print(f"{players[1]}: It's a tie against the computer!")
    elif player_v_computer_matrix[player2_choice][computer_choice] == -1:
        print(f"{players[1]}: Computer wins against the player!")
    elif player_v_computer_matrix[player2_choice][computer_choice] == 1:
        print(f"{players[1]}: Player wins against the computer!")

    print("")

    return rounds_won + rounds_lost

# determine_game_winner - Determines round winner, displays this information to the users, and updates the game statistics accrodingly.
# Attribute round_won_lost_tied - Nine-element dictionary represeting user/computer wins/losses/ties
def determine_game_winner(rounds_won_lost_tied):
    # Create lists for wins and losses
    wins = rounds_won_lost_tied[0:3]
    losses = rounds_won_lost_tied[3:6]
    
    # Find the maximum number of wins
    max_wins = max(wins)
    
    win_list = []

    # Find players with the maximum number of wins
    for player in range(3):
        if wins[player] == max_wins:
            win_list.append(1)
        else:
            win_list.append(0)

    loss_dict = {}
    
    # If only one player has the maximum wins, declare them the winner
    if win_list.count(1) == 1:
        for x in range(3):
            if win_list[x] == 0:
                player_stats[str(x + 1)]["games_lost"] += 1
            else:
                print(f"{players[x]} wins the game!")
                player_stats[str(x + 1)]["games_won"] += 1
    # If more than one player has the highest number of wins, declare a loser and compare the highest number of wins to determine if there is a definitive winner or a tie.
    else:
        for x in range(3):
            if win_list[x] == 0:
                player_stats[str(x + 1)]["games_lost"] += 1
            else:
                loss_dict[str(x + 1)] = losses[x]

    # If the list of losses is calculated, run this code. The list of losses is only calculated if there are 2+ playes with the same amount of wins.
    if loss_dict:
        min_losses = min(loss_dict.values())
        loss_list = {}

        for key in loss_dict.keys():
            if loss_dict[key] == min_losses:
                loss_list[key] = 1
            else:
                player_stats[key]["games_lost"] += 1

        if len(loss_list) == 1:
            for y in loss_list.keys():
                print(f"{players[int(y) - 1]} wins the game!")
                player_stats[y]["games_won"] += 1
        else:
            all_values = list(loss_list.values())
            if all(value == all_values[0] for value in all_values):
                print(f"The game is a tie!")
                for y in loss_list.keys():
                    player_stats[y]["games_tied"] += 1
            else:
                for y in loss_list.keys():
                    if loss_list[y] == min(loss_list.values()):
                        print(f"{players[int(y) - 1]} wins the game!")
                        player_stats[y]["games_won"] += 1
                    else:
                        player_stats[y]["games_lost"] += 1

# determine_overall_winner - Reviews game statistics to determine the overall human winner.
# Used in the statistics screen.
def determine_overall_winner():
    player1_wins = player_stats["1"]["games_won"]
    player2_wins = player_stats["2"]["games_won"]

    player1_losses = player_stats["1"]["games_lost"]
    player2_losses = player_stats["2"]["games_lost"]

    if player1_wins == player2_wins:
        if player1_losses == player2_losses:
            print("\nOverall Human Winner: Tie")
        elif player1_losses < player2_losses:
            print(f"\nOverall Human Winner: {players[0]}")
        elif player2_losses < player1_losses:
            print(f"\nOverall Human Winner: {players[1]}")
    if player1_wins > player2_wins:
        print(f"\nOverall Human Winner: {players[0]}")
    if player2_wins > player1_wins:
        print(f"\nOverall Human Winner: {players[1]}")

# rules() - Displays the rules screen. All rules are displayed to the users.
def rules():
    print("--------------------\nGAME RULES\n--------------------\n")
    print("Winner of the round will be determined as follow:\n")
    print("Rock breaks scissors and Saw therefore rock wins over scissors and saw. Rock loses against paper.\n")
    print("Scissors cut paper therefore scissors win over paper. Scissors lose against rock and Saw.\n")
    print("Paper covers rock therefore paper wins over rock. Paper loses against scissors and Saw.\n")
    print("Saw cuts through scissors and paper therefore saw wins over scissors and paper. Saw loses against rock.\n")
    print("If player and computer make the same selection, there is a tie.\n")
    print("The winner of the game is one who won most rounds. The program must account for ties.\n")
    print(
        "Overall human winner is based on the greater number of won games against the computer and least games lost (must account for tie between human players).\n")
    input("Press ENTER to return to the main menu.")

# stats() - Displays the user and computer statistics for both round and game results.
def stats():
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

        print(
            f"{players[index]} - Rounds won: {rounds_won}, Rounds lost: {rounds_lost}, Rounds tied: {rounds_tied}, Games won: {games_won}, Games lost: {games_lost}, Games tied: {games_tied}")
        index = index + 1

    determine_overall_winner()

    input("\nPress ENTER to return to the main menu.")

# play() - Displays the game screen, and calls the get_player_choice, get_computer_choice(), determine_round_winner(), and determine_game_winner() funtions
# Attributes player1_name, player2_name, computer_name - String representations of the player name.
def play(player1_name, player2_name, computer_name):
    wins_losses_ties = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for round_number in range(1, 4):
        print(f"--------------------\nROUND {round_number}\n--------------------\n")
        player1_choice = get_player_choice(player1_name)
        print("")
        player2_choice = get_player_choice(player2_name)
        print("")
        computer_choice = get_computer_choice()

        print(f"--------------------\nROUND {round_number} RESULTS\n--------------------\n")
        print(f"{player1_name} chose: {weapons[player1_choice]}")
        print(f"{player2_name} chose: {weapons[player2_choice]}")
        print(f"{computer_name} chose: {weapons[computer_choice]}")

        rounds_won_lost_tied = determine_round_winner(player1_choice, player2_choice, computer_choice) + [0, 0, 0]

        combined_rounds_won_lost = []

        for x, y in zip(wins_losses_ties, rounds_won_lost_tied):
            combined_rounds_won_lost.append(x + y)

        wins_losses_ties = combined_rounds_won_lost

    print(f"--------------------\nGAME RESULTS\n--------------------\n")
    determine_game_winner(wins_losses_ties)

    input("\nPress ENTER to return to the main menu.")

# play() - Displays the game menu, and allows for selection of play(), rules(), stats(), or Exit selections.
def menu():
    clear()

    for x in range(2):
        players[x] = get_player_name(x)

        while (players[0] == players[1]) & (players[0] != "") & (players[0] != None):
            print("Player names cannot match. Please choose a different name.")
            players[x] = get_player_name(x)

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
            stats()
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")
            input("Press ENTER to try again.")

# Default the Python script to the menu() function
if __name__ == "__main__":
    menu()