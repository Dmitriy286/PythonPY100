from logic import init_field, is_empty_cell, set_cell, is_win, is_available_cell

def get_first_player():
    ...

def print_field(field: list) -> None:
    for row in field:
        for cell in row:
            print(cell, end=" ")
        print()

def get_step(field: list, player_symbol: str) -> tuple[int, int]:
    step = input(f"Игрок {player_symbol} введите координаты от 1 до 9: ")
    if not step.isdigit():
        print("Вы дебил")
        continue

    int_step = int(step)
    if not 1 <= int_step <= 9:
        print("Вы идиот")
        continue

    x = int_step // field_size
    y = int_step % field_size
    if not is_empty_cell(field, x, y):
        print("Ячейка занята. Повторите ввод")
        continue

    return x, y

def main():
    size_field = 3
    field == init_field()
    print_field(field)

    first_player, second_player = "X", "0"

    # for _ in range(size_field * size_field):

    while True:

    row_index, col_index = get_step(field, first_player)
    set_cell(field, row_index, col_index, first_player)
    print_field(field)

    if is_win(field):
        print(f"Победил игрок {first_player}")
        break

    if not is_available_cell(field):
        print("Ничья")
        break

    row_index, col_index = get_step(field, second_player)
    set_cell(field, row_index, col_index, second_player)
    print_field(field)

    if is_win(field):
        print(f"Победил игрок {second_player}")
        break

    if not is_available_cell(field):
        print("Ничья")
        break



if __name__ == '__main__':
    main()