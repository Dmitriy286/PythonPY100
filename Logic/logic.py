# matrix = [
#     [i * j for j in range(1, 10)]
#     for i in range(1, 10)
# ]
#
#
#
#
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         # ceil = matrix[row][col]
#         print(f"{matrix[row][col]:2}", end=" ")
#     print()


EMPTY_CELL = "-"



def init_field(size=3):
    # empty_cell = "-"
    field = [
        [EMPTY_CELL for _ in range(size)]
        for _ in range(size)
    ]

    return field

def get_cell(field: list, row_index: int, col_index: int):
    return field[row_index][col_index]

def set_cell(field: list, row_index: int, col_index: int,
             symbol) -> None:
    field[row_index][col_index] ...

def is_win(field) -> bool:
    win_combinations = [
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],

        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],

        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)],
    ]
    for win_comb in win_combinations:
        # row_index = win_comb[0][0]
        # col_index = win_comb[0][1]
        # cell_1 = field[row_index][col_index]
        cell_1 = field[win_comb[0]][win_comb[1]] # что-то дописать
        cell_2 = field[win_comb[0]][win_comb[1]]
        cell_3 = field[win_comb[0]][win_comb[1]]



def is_available_cell(field) -> bool:
    for row in field:
        for cell in row:
            if cell == EMPTY_CELL:
                return True
    return False

def is_empty_cell(field: list, x: int, y: int) -> bool:
    cell = field[x][y]
    # if cell == EMPTY_CELL:
    #     return True
    # else:
    #     return False
    return True if cell == EMPTY_CELL else False

