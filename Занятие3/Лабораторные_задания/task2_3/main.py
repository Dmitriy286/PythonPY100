def str_(str_):
    str_ = str_.split()
    print(str_)
    str_ = tuple(str_)
    print(str_)
    for number, word in enumerate(str_):

        print(number, word)

if __name__ == "__main__":
    str_(input("Введите слова через пробел: "))
    # print(str_)
