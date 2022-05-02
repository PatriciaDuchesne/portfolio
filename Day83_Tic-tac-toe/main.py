game_is_on = True
turn = 1
position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winning_positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
player1_choices = []
player2_choices = []


def show_grid():
    grid = (
        f"\n"
        f" {position[0]} | {position[1]} | {position[2]} \n"
        f"---+---+---\n"
        f" {position[3]} | {position[4]} | {position[5]} \n"
        f"---+---+---\n"
        f" {position[6]} | {position[7]} | {position[8]} \n"
    )
    print(grid)


print("\n*** TIC TAC TOE ***")

while game_is_on:
    if turn % 2 == 0:
        current_player = "player 2"
        current_symbol = "O"
        current_player_choices = player2_choices
    else:
        current_player = "player 1"
        current_symbol = "X"
        current_player_choices = player1_choices

    show_grid()
    print(f"It's {current_player}'s turn.")

    player_choice = int(input(f"Where will you place your '{current_symbol}'? Pick a number from the grid. >"))
    if player_choice in position:
        current_index = int(player_choice) - 1
        position[current_index] = current_symbol
        current_player_choices.append(player_choice)
        turn += 1

        if 2 < len(current_player_choices) < 5:
            for option in winning_positions:
                if all(o in current_player_choices for o in option):
                    show_grid()
                    print(f"\nCongratulation {current_player}, you won!")
                    game_is_on = False

        elif len(current_player_choices) > 4:
            show_grid()
            print(f"\nGame over, it's a draw.")
            game_is_on = False

    else:
        print("Please pick a valid number.")
