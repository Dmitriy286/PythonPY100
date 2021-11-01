def input_():
    str_ = []
    while True:
        m = int(input("Enter: "))
        str_2 = str_.append(m)
        if m <= 0:
            break
    return str_
def search(str_2):
    print(str_2)
    print(str_2[3], type(str_2[3]))
    list_ = []
    for i in str_2:
        b = str_2[i]
        print(b)
        if 3 <= b <= 13:
            list_.append(str_2[i])
    print(list_)

if __name__ == "__main__":
    str_2 = input_()
    search(str_2)