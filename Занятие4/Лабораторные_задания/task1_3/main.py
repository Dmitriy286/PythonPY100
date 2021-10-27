from random import randint

def func_():
    list_ = []
    for b in range(1, 6):
        input("Enter number: ")
        list_.append(b)

    return list_


def get_random_list():
    len_ = 10
    start = 0
    end = 10
    return [randint(start, end) for _ in range(len_)]

def func_2():

    list_3 = [value for value in list_global if value % 2 == 0]
    len(list_3)
    return(list_3)

if __name__ == "__main__":

    # list_global = func_()
    list_global = get_random_list()

    print(list_global)
    print(func_2())
