def salary (a, b):
    a_full = a * 10
    current_sum = b
    for value in range(0,9):
        b *= 1.03
        current_sum += b
        # print(b)
        # print(current_sum)

    sum_ = current_sum - a_full

    return sum_

if __name__ == "__main__":

    print(salary(5000, 6000))

