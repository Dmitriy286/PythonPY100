def func():
    print([(i - sum(list_) / len(list_)) for i in list_])


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    func()