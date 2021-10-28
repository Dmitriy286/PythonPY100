def poor_student(s, A, b, q = 1.05):
    months = 0
    # rest_sum = s
    while (s + A) > b:
        print("Месяцев прошло: ", months)
        print("Предстоят траты в текущем месяце: ", b)
        current_sum = s + A
        s = current_sum - b
        b = b * q
        months += 1
        print("Сумма в наличии до трат: ", current_sum)

        print("Сумма в наличии после трат: ", s)
        print("Предстоят траты в следующем месяце: ", b)
        # if (s + A) < b:
        #     break
    return months

if __name__ == "__main__":
    print(poor_student(1000, 500, 600))

