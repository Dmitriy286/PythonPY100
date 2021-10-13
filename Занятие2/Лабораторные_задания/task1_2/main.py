A = int(input("Enter number A: "))
B = int(input("Enter number B: "))
c_1 = A % 2 == 1
c_2 = B % 2 == 1

if c_1 and c_2:
    print("Оба числа нечетные")
elif not c_1 and not c_2:
    print("Оба числа четные")
else:
    print("Какое-то из чисел четное")