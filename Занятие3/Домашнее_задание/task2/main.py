def check_string(str_):
    base = set('01')
    print(base)

    for d in set(str_):  # выделяем все уникальные символы из строки
        if d not in base:
            print("Строка не двоичное число")
            return False

    print("Строка двоичное число")
    return True


if __name__ == "__main__":
    check_string(input('Enter symbols: '))
