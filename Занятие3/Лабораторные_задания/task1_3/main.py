def func(a):
    i = 2
    list_ = []
    while a != 1:

        if a % i == 0.0:
            list_.append(i)
            a = a / i
        else:
            i = i + 1
    return list_


if __name__ == "__main__":
    print(func(850))
    # print(list_)
