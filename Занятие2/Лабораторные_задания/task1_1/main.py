a = int(input("Enter number: "))
c_1 = a % 2 == 0
c_2 = a % 3 == 0

if c_1 or c_2:
    print("Число 'a' кратно 2 или 3")

else:
    print("Число 'a' не кратно 2 или 3")