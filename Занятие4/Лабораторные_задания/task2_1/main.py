def func():
    number = input("Enter number: ")

    list_1 = []
    for i, b in enumerate(number):
        list_1.append(int(b))
    print(list_1)
    return list_1

def func_2():
    task_2 = sum(list_1)
    task_4 = len(list_1)
    print(task_2)
    print(task_4)
    return task_2, task_4

def even_number_sum():
    list_2 = []
    for i in list_1:
        if i % 2 == 0:
            list_2.append(i)
        print(list_2)
    return sum(list_2)

def min_number():
    min_numb = list_1[0]
    for i in list_1:
        if i < min_numb:
            min_numb = i

    return min_numb

def max_number():
    max_numb = 0
    for i in list_1:
        if i > max_numb:
            max_numb = i
    return max_numb

def odd_list():
    list_3 = []
    print(task_4, type(task_4))
    for i, b in enumerate(list_1, start=1):
        if i % 2 != 0:
            list_3.append(b)

    return list_3


def min_number_place():
    min_numb = list_1[0]
    place = 0
    for i, b in enumerate(list_1, start=1):
        if b < min_numb:
            min_numb = b
            place = i
    return min_numb, place

if __name__ == "__main__":
    list_1 = func()
    print(list_1, type(list_1))
    task_2, task_4 = func_2()
    task_3 = even_number_sum()
    print(task_3)
    task_5_1 = min(list_1)
    print("Minimal number, v.1:", task_5_1)
    task_5_1_v_2 = min_number()
    print("Minimal number, v.2:", task_5_1_v_2)
    task_5_2 = max_number()
    print(task_5_2)
    task_6 = odd_list()
    print(task_6)
    task_7 = abs(list_1[0] - list_1[task_4-1])
    print(list_1[task_4-1])
    print(task_7)
    min_numb, place = min_number_place()
    print("Минимальная цифра", min_numb, "стоит на", place, "месте")