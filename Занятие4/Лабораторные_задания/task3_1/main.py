def sentence():
    str_ = main_str
    print(str_)
    str_ = str_.lower()
    print(str_)
    str_ = str_.split(" ")
    print(str_)
    str_.sort()
    print(str_)
    str_ = "".join(str_)
    print(str_)
    return str_

def dict_():
    dict_1 = {}
    for char in str_:
        if char.isalpha():
            if char not in dict_1:
                dict_1[char] = 1
            else:
                dict_1[char] += 1
    print(dict_1)
    return(dict_1)

def new_one():
    full_count = 0
    for char, count in dict_1.items():
        print(char, count)
        full_count += count
    print(full_count)
    return full_count

# ast Frt brt 2 rty iao crv!

# def dict_change():
#     total_count = sum(dict_1.values())
#     print(total_count)
#     dict_2 = {}
#     for key, counts in dict_1.items():
#
#         dict_2[key] = (counts / total_count) * 100
#
#     for key, counts in dict_2.items():
#         print(key, counts)

def dict_change():
    total_count = sum(dict_1.values())
    dict_2 = {key: (counts / total_count) * 100 for key, counts in dict_1.items()}
    # return {char: round(value / total_count, 3) for char, value in char_dict.items()}

    for key, counts in dict_2.items():
        print(key, counts)


if __name__ == "__main__":
    main_str = """
            Данное предложение будет разбиваться на отдельные слова.
            В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
            Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
        """
    str_ = sentence()
    dict_1 = dict_()
    full_count = new_one()
    dict_change()



