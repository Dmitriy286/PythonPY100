# def task(str1, str2):
#     # str1 = input("Enter first string: ")
#     # str2 = input("Enter second string: ")
#
#     if str1[0] == str2[0]:
#         k = str1[0]
#         print("ДА")
#         print(k)
#     else:
#         print("НЕТ")
#     return k
#
# if __name__ == "__main__":
#     task(input("Enter first string: "), input("Enter second string: "))


def task(str1, str2, k):
    # str1 = input("Enter first string: ")
    # str2 = input("Enter second string: ")

    if str1[0] == str2[0] == k:

        print("ДА")
        print(k)
    else:
        print("НЕТ")
    return k

if __name__ == "__main__":
    task(input("Enter first string: "), input("Enter second string: "), input("Enter any symbol: "))
