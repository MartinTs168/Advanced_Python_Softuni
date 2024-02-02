class FullColumnError(Exception):
    pass


class InvalidColumnChoiceError(Exception):
    pass


ROWS = 6
COLS = 7
MAXIMUM_CONNECTIONS = 4

DIRECTION_MAPPER = {
    "left": (0, -1),
    # "right": (0, 1),
    "up": (-1, 0),
    # "down": (1, 0),
    "main_diagonal": (-1, -1),
    "anti_diagonal": (-1, 1),
}


def print_board(cur_board):
    for row in cur_board:
        print(row)


def validate_column_choice(cur_column):
    if 1 <= cur_column <= COLS:
        return True
    else:
        raise InvalidColumnChoiceError


def place_player_choice(col_index, player_num, cur_board):
    for row_index in range(ROWS - 1, -1, -1):
        if cur_board[row_index][col_index] == 0:
            cur_board[row_index][col_index] = player_num
            return row_index, cur_board
    else:
        raise FullColumnError("This column is already full, select another one")


def travel_direction(coordinates, cur_row, cur_col, element, cur_board):
    count = 0
    row_direction, col_direction = coordinates
    for i in range(1, MAXIMUM_CONNECTIONS):
        next_element_row_index = cur_row + row_direction * i
        next_element_col_index = cur_col + col_direction * i
        try:
            if cur_board[next_element_row_index][next_element_col_index] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count
    return count


def travel_opposite_direction(coordinates, cur_row, cur_col, element, cur_board):
    count = 0
    row_direction, col_direction = coordinates
    for i in range(1, MAXIMUM_CONNECTIONS):
        next_element_row_index = cur_row - row_direction * i
        next_element_col_index = cur_col - col_direction * i
        try:
            if cur_board[next_element_row_index][next_element_col_index] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count
    return count


def is_winner(cur_row_index, cur_col_index, cur_board):
    for direction, coords in DIRECTION_MAPPER.items():
        searched_element = cur_board[cur_row_index][cur_col_index]
        travel_direction_count = travel_direction(coords, cur_row_index, cur_col_index, searched_element, cur_board)
        travel_opposite_direction_count = travel_opposite_direction(coords, cur_row_index,
                                                                    cur_col_index, searched_element, cur_board)

        if travel_opposite_direction_count + travel_direction_count + 1 >= MAXIMUM_CONNECTIONS:
            return True
    else:
        return False


def is_board_full(cur_board):
    if 0 not in cur_board[0]:
        return True
    else:
        return False


board = []

for _ in range(ROWS):
    board.append([0 for _ in range(COLS)])

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1
    try:
        column = int(input(f"Player {player}, please choose a column "))
        validate_column_choice(column)
        column_index = column - 1
        row, board = place_player_choice(column_index, player, board)
        if is_winner(row, column_index, board):
            break
    except FullColumnError as ex:
        print(ex)
        continue
    except (InvalidColumnChoiceError, ValueError) as ex:
        print(f"Choose a valid column between 1 and {COLS}")
        continue

    print_board(board)
    turns += 1

print_board(board)
print(f"Winner is player {player}!")
