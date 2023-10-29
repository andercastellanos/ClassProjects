elif player1_rounds_won == player2_rounds_won:
        if player1_rounds_lost == player2_rounds_lost:
            print(f"\nIt's a tie between {players[0]} and {players[1]}.")
        elif player1_rounds_lost < player2_rounds_lost:
            print(f"\n{players[0]} wins!")
        elif player2_rounds_lost < player1_rounds_lost:
            print(f"\n{players[1]} wins!")
    elif player1_rounds_won == computer_rounds_won:
        if player1_rounds_lost == computer_rounds_lost:
            print(f"\nIt's a tie between {players[0]} and {players[2]}.")
        elif player1_rounds_lost < computer_rounds_lost:
            print(f"\n{players[0]} wins!")
        elif computer_rounds_lost < player1_rounds_lost:
            print(f"\n{players[2]} wins!")
    elif player2_rounds_won == computer_rounds_won:
        if player2_rounds_lost == computer_rounds_lost:
            print(f"\nIt's a tie between {players[1]} and {players[2]}.")
        elif player2_rounds_lost < computer_rounds_lost:
            print(f"\n{players[1]} wins!")
        elif computer_rounds_lost < player2_rounds_lost:
            print(f"\n{players[2]} wins!")