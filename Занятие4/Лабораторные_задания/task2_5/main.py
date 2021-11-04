def func(a):
    b = float(a)
    print(b)
    print(b.is_integer())

    if b.is_integer() and b > 0:
        print("Палиндром") if [i for i in str(a)] == [i for i in str(a)][::-1] else print("Не палиндром")
        print([i for i in str(a)])
        print([i for i in str(a)][::-1])
    else:
        print("Число не натуральное")


if __name__ == "__main__":
    func(34543)

