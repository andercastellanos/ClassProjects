from os import system, name
import random

players = ["", "", "Computer"]
weapons = {"1": "Rock", "2": "Paper", "3": "Scissors", "4": "Saw"}

player_stats = {
    "1": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0, "games_tied": 0},
    "2": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0, "games_tied": 0},
    "3": {"rounds_won": 0, "rounds_lost": 0, "rounds_tied": 0, "games_won": 0, "games_lost": 0, "games_tied": 0}
}

player_v_computer_matrix = {
    "1": {"1": 0, "2": -1, "3": 1, "4": 1},
    "2": {"1": 1, "2": 0, "3": -1, "4": -1},
    "3": {"1": -1, "2": 1, "3": 0, "4": -1},
    "4": {"1": -1, "2": 1, "3": 1, "4": 0}
}

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


def clear():
    print("\033[H\033[J", end="")


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


def get_computer_choice():
    return str(random.randint(1, 4))


def determine_round_winner(player1_choice, player2_choice, computer_choice):
    rounds_won = [0, 0, 0]
    rounds_lost = [0, 0, 0]
    
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


def determine_game_winner(rounds_won_and_lost):
    # Create a dictionary to map indexes to player names
    player_index_to_name = {0: players[0], 1: players[1], 2: players[2]}
    
    # Create lists for wins and losses
    wins = rounds_won_and_lost[0:3]
    losses = rounds_won_and_lost[3:6]
    
    # Find the maximum number of wins
    max_wins = max(wins)
    
    # Find players with the maximum number of wins
    max_winners = [i for i, win in enumerate(wins) if win == max_wins]
    
    # If only one player has the maximum wins, declare them the winner
    if len(max_winners) == 1:
        print(f"{player_index_to_name[max_winners[0]]} wins the game!")
    else:
        # If there are multiple players with the same maximum wins, compare their losses
        min_losses = min(losses[i] for i in max_winners)
        
        # Find the winners with the lowest losses
        tie_winners = [player for player in max_winners if losses[player] == min_losses]
        
        if len(tie_winners) == 1:
            print(f"{player_index_to_name[tie_winners[0]]} wins the game!")
        else:
            print("The game is tied.")


def determine_overall_winner():
    player1_wins = player_stats["Player 1"]["games_won"]
    player2_wins = player_stats["Player 2"]["games_won"]

    player1_losses = player_stats["Player 1"]["games_lost"]
    player2_losses = player_stats["Player 2"]["games_lost"]

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

        print(
            f"{players[index]} - Rounds won: {rounds_won}, Rounds lost: {rounds_lost}, Rounds tied: {rounds_tied}, Games won: {games_won}, Games lost: {games_lost}, Games tied: {games_tied}")
        index = index + 1

    determine_overall_winner()

    input("\nPress ENTER to return to the main menu.")


def play(player1_name, player2_name, computer_name):
    wins_and_losses = [0, 0, 0, 0, 0, 0]

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

        rounds_won_and_lost = determine_round_winner(player1_choice, player2_choice, computer_choice)

        test = []

        for x, y in zip(wins_and_losses, rounds_won_and_lost):
            test.append(x + y)

        wins_and_losses = test

    print(f"--------------------\nGAME RESULTS\n--------------------\n")
    determine_game_winner(wins_and_losses)

    input("\nPress ENTER to return to the main menu.")


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
            stats(players[0], players[1], players[2])
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")
            input("Press ENTER to try again.")


if __name__ == "__main__":
    menu()