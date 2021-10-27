def poor_student(s, A, b, q = 1.05):
    months = 0
    current_sum = s
    while current_sum > b:
        current_sum = s + A
        rest_sum = current_sum - b
        b = b * q
        months += 1
    return months

if __name__ == "__main__":
    print(poor_student(1000, 500, 600))
