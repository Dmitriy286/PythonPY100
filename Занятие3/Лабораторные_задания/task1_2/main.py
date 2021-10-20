def factorial (n):
    current_number = 1
    fact = 1
    for value in range(0,n):
        current_number += 1
        fact *= current_number

    return fact

if __name__ == "__main__":
    print(factorial(7))
