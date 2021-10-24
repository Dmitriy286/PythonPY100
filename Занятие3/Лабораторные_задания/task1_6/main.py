def salary (a, b):
    a_full = a * 10
    current_sum = 0
    for value in range(0,10):
        current_sum += b
        b *= 1.03

        print(current_sum)
        print(b)
    sum_ = current_sum - a_full

    return sum_

if __name__ == "__main__":

    print(salary(5000, 6000))

