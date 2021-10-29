def str_(str_):
    str_ = "".split(str_)
    for i in str_:
        print(str_[i])


if __name__ == "__main__":
    str_(input("Введите предложение: "))
    print(str_())
