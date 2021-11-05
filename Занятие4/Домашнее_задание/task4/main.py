def proof(A):
    if len(A) == 6:
        print("Вы ввели шестизначное число. Продолжаю расчеты.")
        return A
    else:
        print("Вы ввели не шестизначное число.")
        C = 0
        return C


def func(B):
    whole_str = B
    middle_value = len(whole_str) // 2
    print(middle_value)
    first_part = [int(i) for i in whole_str[:middle_value]]
    second_part = [int(i) for i in whole_str[middle_value:]]
    print(first_part, type(first_part))
    print(second_part, type(second_part))
    print(sum(first_part))
    print(sum(second_part))
    print("Это число счастливое") if sum(first_part) == sum(second_part) else print("Это число не счастливое")


if __name__ == "__main__":
    B = proof(input("Введите шестизначное число: "))
    if B != 0:
        func(B)
    else:
        print("Расчеты остановлены.")
