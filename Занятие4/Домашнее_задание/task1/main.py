def func(A):
    a = str(A)
    set_ = set([i for i in a])
    print(set_)
    print("Все цифры одинаковые") if len(set([i for i in a])) == 1 else print("Не все цифры одинаковые")

if __name__ == "__main__":
    func(33433)