if __name__ == "__main__":
    # Write your solution here
    list_ = [2, 4, 2, 7, 14, 3, 9, 0, 7, 11]
    first_value = list_[0]
    max_value_index = 0
    max_value = list_[max_value_index]
    for i, b in enumerate(list_):
        current_value = list_[i]
        if current_value > max_value:
            max_value = current_value
            max_value_index = i
            list_[0] = max_value
            list_[max_value_index] = first_value
    print(list_)

    # правильно или нет??? И НИЖЕ ЕЩЕ ВОПРОС!!!


# list_ = [1, 2, 3]
# print(list_)
# a = list_[0] # ЭТО КОСТЫЛЬ???
# list_[0] = list_[2]
# list_[2] = a
# print(list_)
