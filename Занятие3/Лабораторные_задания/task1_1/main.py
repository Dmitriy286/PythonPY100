# Первый вариант:
def task_1_1():
    max_sum = 500
    current_sum = 0
    n = 1
    list_ = []
    # b = a + 1
    # n = 2
    while True:
        current_value = n ** 2

        if current_sum + current_value > max_sum:
            break

        else:
            current_sum += current_value
            print(n, current_sum)
            n = n + 1

            i = current_sum
            list_.append(i)
            print(list_)
            # s = max(list_)
            # print((s))

    return list_

if __name__ == "__main__":
    a = task_1_1()

    for i, global_current_value in enumerate(a, start=1):
        if global_current_value == max(a):
            print("Количество чисел составляет: ", i)

# Второй вариант:
def task_1_1():
    max_sum = 500
    current_sum = 0
    n = 1

if __name__ == "__main__":
    a = task_1_1()