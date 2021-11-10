from TicTacToe_functions import display_board,player_input,player_choice,\
    replay, place_marker,win_check, choose_first, full_board_check


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board1 = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    markers = player_input()
    player1_marker = markers[0]
    player2_marker = markers[1]
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.').upper()

    if play_game == 'YES':
        game_on = True
    else:
        game_on = False

    while game_on == True:

        if turn == "Player 1":
            # Player 1 Turn

            display_board(board1)
            position = player_choice(board1)
            place_marker(board1, player1_marker, position)

            if win_check(board1, player1_marker) == True:
                display_board(board1)
                print("Player1 WON!")
                game_on = False
            else:
                if full_board_check(board1) == True:
                    print("It's a TIE!")
                    break
                else:
                    turn = "Player 2"


        else:
            # Player2's turn.

            display_board(board1)
            position = player_choice(board1)
            place_marker(board1, player2_marker, position)

            if win_check(board1, player2_marker) == True:
                print("Player2 WON!")
                game_on = False

            else:
                if full_board_check(board1) == True:
                    display_board(board1)
                    print("It's a TIE!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break