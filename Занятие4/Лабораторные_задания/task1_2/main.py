def func_(n, m):
    list_ = [i ** 2 for i in range(n, m+1) if i % 2 != 0]
    return list_
if __name__ == "__main__":
    print(func_(3, 15))
