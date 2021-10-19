# TODO

if __name__ == "__main__":
    A = 47
    B = 34
    C = 67
    condition_1 = A < 45 and B >= 45 and C >= 45
    condition_2 = A >= 45 and B < 45 and C >= 45
    condition_3 = A >= 45 and B >= 45 and C < 45

    if condition_1 or condition_2 or condition_3:
        print('True')
    else:
        print("False")