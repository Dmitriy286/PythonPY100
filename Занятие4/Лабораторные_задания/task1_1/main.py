def func_(n, m):
    list_ = [i ** 2 for i in range(n, m+1)]
    return list_
if __name__ == "__main__":
    print(func_(5, 23))
