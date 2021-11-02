def func(number):
    number_local = str(number)
    # sum_ = number_local.split()
    list_ = []
    for i in number_local:
        list_.append(int(i))
    sum_ = sum(list_)
    print(sum_)
    return sum_

def compare(sum_):
    list_1 = []
    for i, b in enumerate(str(sum_)):
        list_1.append(int(b))
    print(list_1)

    if len(list_1) == 2:
        print("Сумма цифр является двузначным числом")
    else:
        print("Сумма цифр не является двузначным числом")

if __name__ == "__main__":
    sum_ = func(input("Введите трехзначное число: "))
    compare(sum_)

