def func(A):
    str_a = str(A)
    list_a = []
    for i in str_a:
        list_a.append(int(i))
    sum_a = sum(list_a)
    print(sum_a)
    return sum_a
def func_2(B):
    if B % 7 == 0:
        print("Кратно 7")
    else:
        print("Не кратно 7")

if __name__ == "__main__":
    sum_a = func(8947)
    func_2(sum_a)
