if __name__ == "__main__":
    A = int(input("Enter number A: "))
    B = int(input("Enter number B: "))

    a = A**2 + B**2
    b = (A + B)**2

    if a > b:
        print("Сумма квадратов больше")
    elif a < b:
        print("Квадрат суммы больше")
    else:
        print("Значения равны")