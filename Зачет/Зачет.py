

# def true_():
#     str_ = input("Enter number: ")
#
#
#     list_ = []
#     for i, b in enumerate(str_):
#         list_.append(b)
#     return list_
#
# def compare():
#     if len_ == 1
#
# if __name__ == "__main__":
#     list_ = true_()
#     set_ = set(list_)
#     print(set_)
#     len_ = len(set_)
#     compare()

# #1
# # Записать условие, которое является истинным, когда каждое из чисел А и В нечетное.
# def func():
#     A = int(input("Enter number 1: "))
#     B = int(input("Enter number 2: "))
#     if A % 2 != 0 and B % 2 != 0:
#         print("Both numbers are odd")
#     else:
#         print("Some of numbers is even")
# if __name__ == "__main__":
#     func()

# #2
# # Записать условие, которое является истинным, когда каждое из чисел А,В,С кратно трем.
# def func(A, B, C):
#     if A % 3 == 0 and B % 3 == 0 and C % 3 == 0:
#         print("True")
#     else:
#         print("False")
# if __name__ == "__main__":
#     func(9, 6, 12)

# #3
# #Ввести с клавиатуры три числа, положительные возвести в квадрат, а отрицательные оставить без изменений.
# def func():
#     A = int(input("Enter number 1: "))
#     B = int(input("Enter number 2: "))
#     C = int(input("Enter number 3: "))
#     list_1 = [A, B, C]
#     list_2 = []
#     for i in list_1:
#         if i >= 0:
#             list_2.append(i ** 2)
#         else:
#             list_2.append(i)
#     print(list_2)
#
# if __name__ == "__main__":
#     func()

#4
# Дано двузначное число.
# Определить: а) входят ли в него цифры 3 и 7; б) входят ли в него цифры (4 и 8) или цифра 9

# def func(a):
#     str_ = str(a)
#     print(str_)
#     if "3" in str_ and "7" in str_:
#         print("Входят 3 и 7")
#     elif ("4" in str_ and "8" in str_) or ("9" in str_):
#         print("Входят 4 и 8 или 9")
#     else:
#         print("Цифры в указанных комбинациях не входят")
#
# if __name__ == "__main__":
#     func(66)

#5
# Мастям игральных карт условно присвоены следующие порядковые номера:
# масти "пики" — 1, масти "трефы" — 2, масти "бубны" — 3, масти "червы" — 4,
# а достоинству карт: "валету" — 11, "даме" — 12, "королю" — 13, "тузу" — 14
# (порядковые номера карт остальных достоинств соответствуют их названиям: "шестерка", "девятка" и т. п.).
# По заданным номеру масти m (1 <= m <= 4) и номеру достоинства карты k (6 <= k <= 14)
# определить полное название (масть и достоинство) соответствующей карты
# в виде "Дама пик", "Шестерка бубен" и т. п.


# def func(m, k):
#     list_ = []
#     if k == 11:
#         list_.append("Валет")
#     elif k == 12:
#         list_.append("Дама")
#     elif k == 13:
#         list_.append("Король")
#     else:
#         list_.append("Туз")
#
#     if m == 1:
#         list_.append("пики")
#     elif m == 2:
#         list_.append("треф")
#     elif k == 3:
#         list_.append("бубен")
#     else:
#         list_.append("червы")
#
#     print(list_)
#
# if __name__ == "__main__":
#     func(4, 12)

#6
# Даны два целых числа A и B (A < B).
# Найти все целые числа, расположенные между данными числами (не включая сами эти числа),
# в порядке их убывания, а также количество N этих чисел.

# def func(A, B):
#     print([i for i in range(A+1, B)][::-1])
#     print(len([i for i in range(A+1, B)]))
# if __name__ == "__main__":
#     func(4, 12)

#7
# Гипотеза Сиракуз гласит, что любое натуральное число сводимо к единице при следующих действиях над ним:
# а) если число четное, то разделить его пополам,
# б) если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.
# Над вновь полученным числом вновь повторить действия a) или б) в зависимости от его четности.
# Рано или поздно число станет равным 1.

# def func(A):
#     a = A
#     while True:
#         if a % 2 == 0:
#             print(a)
#             a /= 2
#             if a == 1:
#
#                 print("Число приведено к 1")
#                 break
#
#         if a % 2 != 0:
#             print(a)
#             a = (a * 3 + 1) / 2
#
# if __name__ == "__main__":
#     func(9)
    
    
# # 8
# # Начав тренировки, спортсмен в первый день пробежал n км.
# # Каждый день он увеличивал дневную норму на y% нормы предыдущего дня.
# # Какой суммарный путь пробежит спортсмен за x дней?
# def func(n, y, x):
#     y_proc = 1 + 5 / 100
#     print(y_proc)
#     print(n)
#     sum_ = n
#     for i in range(1, x):
#         sum_ += n
#         n *= y_proc
#         print(n)
#         print(sum_)
# if __name__ == "__main__":
#     func(2, 5, 10)




# 9
# Определить, сколько в введенном пользователем числе четных цифр, а сколько нечетных.

def func(a):
    str_ = str(a)
    print(str_)
    even_numbers = 0
    odd_numbers = 0
    for i in str_:
        if int(i) % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    print("Четных чисел - ", even_numbers, "Нечетных чисел - ", odd_numbers)

if __name__ == "__main__":
    func(2345778)

# # 10
# # Написать программу в виде оператора цикла с параметром, обеспечивающий
# # вывод на экран "столбиком" всех целых чисел от 10 до 30.
# # Оформить этот фрагмент в виде:
# # а. оператора цикла с предусловием
# # б. оператора цикла с постусловием.
#
# # С ПОСТУСЛОВИЕМ
# def func(A, B):
#     i = A
#     while True:
#         print(i)
#         i += 1
#         if i == B:
#             print(i)
#             break
#
# # С ПРЕДУСЛОВИЕМ
# def func(A, B):
#     i = A
#     print(i) # ПО МОЕМУ ЭТО КОСТЫЛЬ!!!! НЕТ????
#     while i != B:
#         i += 1
#         print(i)
#         # i += 1
#
# if __name__ == "__main__":
#     func(10, 30)

#11
# В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64.
# Дано натуральное число n.
# Как наименьшим количеством таких денежных купюр можно выплатить сумму n
# (указать количество каждой из используемых для выплаты купюр)?
# Предполагается, что имеется достаточно большое количество купюр всех достоинств.

# def f_kupura_64(a):
#     kupura_64 = 0
#     while True:
#         a - 64
#         kupura_64 += 1
#         if a < 64:
#             return a, kupura_64
#
# def f_kupura_32(b):
#     kupura_32 = 0
#     while True:
#         b - 32
#         kupura_32 += 1
#         if a < 32:
#             return b, kupura_32
#
# def f_kupura_16(c):
#     kupura_16 = 0
#     while True:
#         a - 16
#         kupura_16 += 1
#         if c < 16:
#             return c, kupura_16
#
# def f_kupura_8(d):
#     kupura_8 = 0
#     while True:
#         d - 8
#         kupura_8 += 1
#         if d < 8:
#             return d, kupura_8
#
# def f_kupura_4(e):
#     kupura_4 = 0
#     while True:
#         e - 4
#         kupura_4 += 1
#         if e < 4:
#             return e, kupura_4
#
# def f_kupura_2(f):
#     kupura_2 = 0
#     while True:
#         f - 2
#         kupura_2 += 1
#         if f < 2:
#             return f, kupura_2
#
# def f_kupura_1(g):
#     kupura_1 = 0
#     while True:
#         g - 1
#         kupura_1 += 1
#         if g < 1:
#             return g, kupura_1
#
# if __name__ == "__main__":
#     b, kupura_64 = f_kupura_64(567)
#     c, kupura_32 = f_kupura_32(b)
#     d, kupura_16 = f_kupura_16(c)
#     e, kupura_8 = f_kupura_8(d)
#     f, kupura_4 = f_kupura_4(e)
#     g, kupura_2 = f_kupura_2(f)
#     h, kupura_1 = f_kupura_1(g)
#     print("Купюра 64: ", kupura_64)
#     print("Купюра 32: ", kupura_32)
#     print("Купюра 16: ", kupura_16)
#     print("Купюра 8: ", kupura_8)
#     print("Купюра 4: ", kupura_4)
#     print("Купюра 2: ", kupura_2)
#     print("Купюра 1: ", kupura_1)
#
# def f_kupura(a):
#     kupura_1 = 0
#     while True:
#         kupura_64 = a // 64
#         a = a % 64
#         print(kupura_64, a)
#
# if __name__ == "__main__":
#     f_kupura(657)