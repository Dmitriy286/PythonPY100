def input_():
    str_ = []
    while True:
        m = int(input("Enter: "))
        str_.append(m)
        if m <= 0:
            break
    return str_

def search(str_2):
    print(str_2)
    print(str_2[3], type(str_2[3]))
    list_ = []
    for i in str_2:
        if 3 <= i <= 13:
            list_.append(i)
    print(list_)

if __name__ == "__main__":
    str_2 = input_()
    search(str_2)
