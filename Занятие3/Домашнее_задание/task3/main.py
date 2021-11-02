def enter_string():
    str_ = input("Enter words, divided by spaces, it can be several spaces between words: ")
    print(str_)
    return str_
def divided_words(str_):
    str_ = str_.split()
    len_ = len(str_)
    print(str_)
    return str_, len_
def matching_words(str_, len_):
    number = 0
    for i in str_:
        if len(i) > number:
            number = len(i)
            print(number)
    return number

def finding_biggest_word(number, str_):
    list_ = []
    for i in str_:
        if len(i) == number:
            list_.append(i)
    return list_

if __name__ == "__main__":
    str_ = enter_string()
    str_, len_ = divided_words(str_)
    print(str_, len_)
    number = matching_words(str_, len_)
    print(finding_biggest_word(number, str_))

