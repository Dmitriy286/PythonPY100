def pow_func(base, pow_=2):
    return base ** pow_


if __name__ == "__main__":
    print(pow_func(4))  # по умолчанию возводим число в степень два
    print(pow_func(3, pow_=3))  # переопределяем аргумент по умолчанию
    print(pow_func(5))
    print(pow_func(3, 4))