def palindrome(str_):
    str_ = str_.split()
    str_ = "".join(str_)

    str_ == str_[::-1]
    print(str_)
    print(str_2)


    # str_ = str_.split()
    # print(str_)
    # str_ = "".join(str_)
    # print(str_)
    # str_2 = str_2.split()
    # print(str_2)
    # str_2 = "".join(str_2)
    # print(str_2)
    # print(str_[0])
    # print(str_2[0])
    k = 0
    a = 0
    b = 0
    c = len(str_)
    for i in str_:
        if str_[k] == str_2[k]:

            a += 1
            # print("Palindrome")
            print("Печатаю a", a)
            k += 1
            print("Печатаю k", k)
        else:
            # b +=1
            print("Not Palindrome")
            # print("Печатаю b", b)
            # print(a, c)
            break

    return a, c

def max_min(q, w):
    if q == w:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    q, w = palindrome(input("Enter string: "))

    print(q, w)
    max_min(q, w)
# я иду с мечем судия