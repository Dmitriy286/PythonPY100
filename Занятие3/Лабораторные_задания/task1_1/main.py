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
            return  n
        else:
            current_sum += current_value
            print(n, current_sum)
            n = n + 1

            i = current_sum
            list_.append(i)
            print(list_)
            # s = max(list_)
            # print((s))

    return n

if __name__ == "__main__":
    print(task_1_1())

