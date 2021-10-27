def func():
    list_even = [i for i in list_ if i % 2 == 0]
    print(list_even)
    list_odd = [b for b in list_ if b % 2 != 0]
    print(list_odd)
    a = len(list_even)
    b = len(list_odd)
    print(a, b)
    if a > b:
        print("Больше четных")

    elif a < b:
        print("Больше нечетных")

    else:
        print("Равно")





if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 4]
    func()
