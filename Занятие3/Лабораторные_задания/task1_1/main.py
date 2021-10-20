def task_1_1():
    max_sum = 500
    current_sum = 0
    n = 1
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

    return n



if __name__ == "__main__":
    print(task_1_1())

