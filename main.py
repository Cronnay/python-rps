from game import Game, moves_beat_matrix

def main():
    print("Welcome! New game have started")
    rounds = []
    while True:
        new_game = Game()
        rounds.append(new_game)
        make_your_move_text = f"Make your move between these: {', '.join(list(moves_beat_matrix.keys()))}"
        player_move = input(
            f"A new round has started and computer made their move. {make_your_move_text}\n"
        )
        while not player_move.lower() in moves_beat_matrix:
            player_move = input(
                f"Sorry. Not a valid move. Please try again. {make_your_move_text}\n"
            )

        new_game.set_player_move(player_move)
        winner = new_game.determine_winner()

        if winner == "tie":
            print("That was a tie! Play again")
            continue
        elif winner == "computer":
            print(f"Computer won :( Computer chose {new_game.computer_move}, you chose {new_game.player_move}")
        else:
            print("You won!!! Hooray!")
        break

    text_to_print = f"""
Game is done!
Rounds made: {len(rounds)}
"""
    for game in rounds:
        text_to_print += f"{game}"

    print(text_to_print)

if __name__ == "__main__":
    main()
