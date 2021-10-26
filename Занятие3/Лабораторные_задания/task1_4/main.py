def func(epsilon=0.0001):
    current_sum = 0
    current_element = 0.5
    while current_element > epsilon:
        current_sum += current_element
        current_element = current_element / 2
        print(current_element)



    # return current_sum

if __name__ == "__main__":
    print(func())
