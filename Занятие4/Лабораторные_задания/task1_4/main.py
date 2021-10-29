# from random import randint
#
# def func():
#     list_1 = [randint(1, 10) for _ in range (10)]
#     print(list_1)
#     value = sum(list_1) / len(list_1)
#     print[list_1]
#     b = list_1[0]
#         while b < 5:
#
#             list_1[i] = randint(1, 500)
#             print(list_1)
#
#         # list_2 = [randint(1, 10) for i in list_1 if i > value]
#         # print(list_2)
#
# if __name__ == "__main__":
#     print(func())


from random import randint

def func():
    list_1 = [randint(1, 10) for _ in range (10)]
    print(list_1)
    value = sum(list_1) / len(list_1)
    print(value)

    list_2 = [i for i in list_1 if i > value]
    print(list_2)
if __name__ == "__main__":
    print(func())
