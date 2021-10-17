if __name__ == "__main__":
    list_ = [3, 7, 8, 9, 5, 6, 1, 4, 3, 3]

    count_even = 0  # количество четных чисел
    count_odd = 0  # количество нечетных чисел

    for number in list_:
        if number % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    if count_even > count_odd:
        print('Четных чисел больше')
    else:
        print('Нечетных чисел больше')



# TODO посчитать количество четных и нечетных значений в списке

# if count_even > count_odd:
#     print('Четных чисел больше')
# else:
#     print('Нечетных чисел больше')
