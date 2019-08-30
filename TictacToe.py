board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
key_mapping_dictionary = {1: (2, 0), 2: (2, 1), 3: (2, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (0, 0), 8: (0, 1),
                          9: (0, 2)}
user_marking = {1: 'X', 2: 'O'}
selected_position_list = []


def print_board():
    for index, row in enumerate(board):
        print(f"  {board[index][0]}  |  {board[index][1]}  |  {board[index][2]}  ")
        print("-----|-----|-----")


def is_not_vaid_input(user_input):
    return not type(user_input) == int


def update_board(user_id, user_input_position):
    (x, y) = key_mapping_dictionary[int(user_input_position)]
    board[x][y] = user_marking[user_id]
    print_board()


def check_for_game(user_id):
    user_mark = user_marking[user_id]

    for row in board:
        if row.count(user_mark) == 3:
            return True

    board_transpose = [[row[i] for row in board] for i in range(0, 3)]
    for row in board_transpose:
        if row.count(user_mark) == 3:
            return True

    if [board[i][i] for i in range(0, 3)].count(user_mark) == 3:
        return True
    elif [board[x][y] for x, y in zip(range(0, 3), range(0, 3)[::-1])].count(user_mark) == 3:
        return True

    return False


def is_valid_position(user_input):
    try:
        val = int(user_input)
        if val > 9 or val < 1:
            return (False, "value should be between 1 -> 9")
        elif user_input in selected_position_list:
            print_board()
            return (False, f" '{user_input}'  already taken")
        return (True, "")
    except ValueError:
        return (False, f" '{user_input}'  is not a number, legal values are 1 -> 9 ")


def start_tic_tac_toe():
    init()
    move_index = 0
    while True:
        if move_index == 9:
            print("----------------game DRAW------------------")
            break

        user_id = get_user_id(move_index)
        user_input_position = get_valid_position(user_id)
        selected_position_list.append(user_input_position)
        update_board(user_id, user_input_position)

        if check_for_game(user_id):
            print(f"\n\n############  Hurry Congrats User {user_id} won ....!!!!!!  ################\n")
            break
        else:
            move_index += 1
    return input("would you like to play a new game(y/n) : ")


def get_valid_position(user_id):
    user_input_position = input(f"user{user_id} : choose your position from keypad : ")
    t = is_valid_position(user_input_position)

    while not t[0]:
        print(f"!!!invalid choice!!! \n cause : {t[1]}")
        user_input_position = input(f"user{user_id} : please choose a valid position from keypad : ")
        t = is_valid_position(user_input_position);

    return user_input_position


def get_user_id(index):
    if index % 2 == 0:
        user_id = 1
    else:
        user_id = 2
    return user_id


def init():
    global board
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    selected_position_list.clear()


def start_game():
    print("**** welcome to  the tic tac toe ****")
    user_input = start_tic_tac_toe()
    while user_input.lower() == 'y':
        user_input = start_tic_tac_toe()
    else:
        print("Thank you for your time")


start_game()
