# def func():
#     str_ = set(input("Введите двузначное число: "))
#     number_1 = set("48")
#     number_2 = set("9")
#     print(number_1)
#     print(number_2)
#     for value in str_:
#         if str_ == number_1:
#             print("Входит 4, 8")
#         elif value in number_2:
#             print("Входит 9")
#         else:
#             print("Не входит")
#
# if __name__ == "__main__":
#     func()

def func(number):
    mumber_str = str(number)
    print("Входит") if ("4" in mumber_str and "8" in mumber_str) or ("9" in mumber_str) else print("Не входит")

    # if ("4" in mumber_str and "8" in mumber_str) or ("9" in mumber_str):
    #     print("Входит")
    # else:
    #     print("Не входит")

if __name__ == "__main__":
    func(input("Введите двузначное число: "))
