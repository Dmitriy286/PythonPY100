# Записать условие, которое является истинным, когда каждое из чисел А и В нечетное.

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

#1
# def func():
#     A = int(input("Enter number 1: "))
#     B = int(input("Enter number 2: "))
#     if A and B % 2 != 0:
#         print("Both numbers are odd")
#     else:
#         print("Some of numbers is even")
# if __name__ == "__main__":
#     func()

#2
# Записать условие, которое является истинным, когда каждое из чисел А,В,С кратно трем.
# def func(A, B, C):
#     if A % 3 == 0 and B % 3 == 0 and C % 3 == 0:
#         print("True")
#     else:
#         print("False")
# if __name__ == "__main__":
#     func(9, 6, 12)

#3
#Ввести с клавиатуры три числа, положительные возвести в квадрат, а отрицательные оставить без изменений.
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

def func(A):
    a = A
    while
if __name__ == "__main__":
    func(4, 12)
    
    
    
# def func(A, B):
# 
# if __name__ == "__main__":
#     func(4, 12)
#     
#     
#     
# def func(A, B):
# 
# if __name__ == "__main__":
#     func(4, 12)