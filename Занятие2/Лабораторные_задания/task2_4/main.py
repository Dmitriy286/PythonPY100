# if __name__ == "__main__":
#     str_ = "Hello,world"
#     index = str_[0]
#     for i in range(len(str_)):
#         index = str_[i]
#         print(" " * (5 + i) + index)
#     # постарайтесь не использовать "магические" числа,
#     # а по возможности дать переменным осмысленные названия и использовать их
#     # TODO Распечатать строку лесенкой



# if __name__ == "__main__":
#     str_ = "Hello,world"
#     meaning = str_[0]
#     for i in range(len(str_)):
#         meaning = str_[i]
#         print(" " * (5 + i), meaning)


if __name__ == "__main__":
    str_ = "Hello,world"
    for spaces, meaning in enumerate(str_):
        spaces = " " * (5 + spaces) #не очень понимаю, как это сработало!!!
        print(spaces, meaning)

#постарайтесь не использовать "магические" числа,
# а по возможности дать переменным осмысленные названия и использовать их
# TODO Распечатать строку лесенкой

# как решить через enumerate?
# как называется один шаг в цикле?