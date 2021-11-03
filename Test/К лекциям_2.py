# str_5 = 'Hello World! Ho\nw are you?'
# print(str_5)
# list_words = str_5.split()
# print(list_words, type(list_words))
#
# str_6 = '2'
#
# str_7 = 2
# print('-----')
# print(str_5.isdigit())
# print('-----')
# print(str_6.isdigit())
# print('-----')
# print(str_7.isdigit())

# str_5 = 'Hello World! Ho\nw are you?'
# print(str_5.isdigit())
# str_6 = '2'
# print(str_6.isdigit())
# str_7 = 2
# print(str_7.isdigit())

# list_ = [1, 3, 5, 3, 6, 6]
# list_[2] = 1000
# print(list_)

import random
random_int = random.randint(4, 98)
print(random_int)
random_rand = random.random()
print(random_rand)

float_ = 5.2
int_ = int(float_)
print(int_)

list_ = [1, 2]
print(list_, type(list_))
str_ = str(list_)
print(str_, type(str_))
str_2 = str([1, 2])
print(str_2, type(str_2))
str_2_3 = str_.split()
print(str_2_3, type(str_2_3))
str_3 = " ".join(str_2_3)
print(str_3, type(str_3))

dict_ = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(dict_)

for i, b in dict_.items():
    b = b/2
    dict_[b] = b
    print(b)
print(dict_)