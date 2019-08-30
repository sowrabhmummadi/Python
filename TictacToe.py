board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
key_mapping_dictionary = {1: (2, 0), 2: (2, 1), 3: (2, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (0, 0), 8: (0, 1),
                          9: (0, 2)}
user_marking = {1: 'X', 2: 'O'}
selected_position_list = []


def print_board():
    for index, row in enumerate(board):
        # print(f"-----|-----|-----|")
        print(f"  {board[index][0]}  |  {board[index][1]}  |  {board[index][2]}  ")
        print(f"-----|-----|-----")


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
    return False
    # 3 in a row
    # 3 in a coloumn
    # 3 diagnoloy-1
    # 3 diagnoloy-2


def start_tic_tac_toe():
    index = 0
    while True:
        if index % 2 == 0:
            user_id = 1
        else:
            user_id = 2
        user_input_position = input(f"user{user_id} : choose your position from keypad : ")
        selected_position_list.append(user_input_position)
        update_board(user_id, user_input_position)
        if check_for_game(user_id):
            print(f"Hurry Congrats User :{user_id} won")
            break
        else:
            index += 1


def start_game():
    user_input = input("welcome to  the tic tac toe : ")
    if user_input.lower() == 'yes':
        start_tic_tac_toe()
    else:
        print("thank you for your time")


start_game()
