determine game winner

if player1_rounds_won > player2_rounds_won >= computer_rounds_won:
        player_stats["Player 1"]["games_won"] += 1
        player_stats["Player 2"]["games_lost"] += 1
        player_stats["Computer"]["games_lost"] += 1
        print("Player 1 Wins!")
    elif player2_rounds_won > player1_rounds_won >= computer_rounds_won:
        player_stats["Player 1"]["games_lost"] += 1
        player_stats["Player 2"]["games_won"] += 1
        player_stats["Computer"]["games_lost"] += 1
        print("Player 2 Wins!")
    elif computer_rounds_won > player1_rounds_won >= player2_rounds_won:
        player_stats["Player 1"]["games_lost"] += 1
        player_stats["Player 2"]["games_lost"] += 1
        player_stats["Computer"]["games_won"] += 1
        print("Computer Wins!")
    if player1_rounds_won == player2_rounds_won == computer_rounds_won:
    elif player1_rounds_lost < player2_rounds_lost < computer_rounds_lost:
        player_stats["Player 1"]["games_won"] += 1
        player_stats["Player 2"]["games_lost"] += 1
        player_stats["Computer"]["games_lost"] += 1
        print("Player 1 Wins!")
    elif player2_rounds_lost < player1_rounds_lost < computer_rounds_lost:
        player_stats["Player 1"]["games_lost"] += 1
        player_stats["Player 2"]["games_won"] += 1
        player_stats["Computer"]["games_lost"] += 1
        print("Player 2 Wins!")
    elif computer_rounds_lost < player1_rounds_lost < player2_rounds_lost:
        player_stats["Player 1"]["games_lost"] += 1
        player_stats["Player 2"]["games_lost"] += 1
        player_stats["Computer"]["games_won"] += 1
        print("Computer Wins!")
    else:
        print("It's a tie.")