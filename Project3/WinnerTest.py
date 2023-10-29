def determine_game_winner(player1_wins, player2_wins, computer_wins, player1_losses, player2_losses, player3_losses):
    # Create lists for wins and losses
    wins = [player1_wins, player2_wins, computer_wins]
    losses = [player1_losses, player2_losses, player3_losses]
    
    # Find the maximum number of wins
    max_wins = max(wins)
    
    # Find players with the maximum number of wins
    max_winners = [i + 1 for i, win in enumerate(wins) if win == max_wins]
    
    # If only one player has the maximum wins, declare them the winner
    if len(max_winners) == 1:
        return f"Player {max_winners[0]} is the winner."
    
    # If there are multiple players with the same maximum wins, compare their losses
    min_losses = min(losses[i - 1] for i in max_winners)
    
    # Find the winners with the lowest losses
    tie_winners = [player for player in max_winners if losses[player - 1] == min_losses]
    
    if len(tie_winners) == 1:
        return f"Player {tie_winners[0]} is the winner."
    else:
        return "It's a tie."

# Example usage:
player1_wins = 5
player2_wins = 5
computer_wins = 3
player1_losses = 2
player2_losses = 1
player3_losses = 3

result = determine_game_winner(player1_wins, player2_wins, computer_wins, player1_losses, player2_losses, player3_losses)
print(result)
