def factorial (n):
    # current_number = 0
    fact = 1
    for value in range(1, (n+1)):
        # current_number += 1
        fact *= value

    return fact

if __name__ == "__main__":
    print(factorial(15))
