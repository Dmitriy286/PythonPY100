# def sum_():
#     list_ = []
#     current_number = int(input("Введите любое целое число или 0: "))
#     list_.append(current_number)
#     while current_number != 0:
#         current_number = int(input("Введите любое целое число или 0: "))
#         if current_number > 0:
#             list_.append(current_number)
#     print(list_)
#     return sum(list_)


def sum_():
    list_ = []
    while True:
        current_number = int(input("Введите любое целое число или 0: "))

        if current_number == 0:
            break

        list_.append(current_number)
    print(list_)
    return sum(list_)

if __name__ == "__main__":
    print(sum_())
