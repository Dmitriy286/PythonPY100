str_1 = 'fghjcfvgbhn' \
        'sdfgh'

print(str_1)

str_2 = 'hjkkk\
gggg\
gg\
gg\
gggg'

print(str_2)

str_3 ='hjkkk\ngggg\ngg\ngg\ngggg'

print(str_3)

str_4 = '''fgh
gf
gf
gfd\tds''' # табуляция
print(str_4)

print('test', end='_') # ВОЗМОЖНА РАСПЕЧАТКА КЛЕТОК В КРЕСТИКАХ-НОЛИКАХ
print('test', end='')
print('test')

f = "west"
print(f, end='S')
print(f, end='\n')

print("Hello World".lower())

up_str = 'test'
up_str = up_str.upper()
print(up_str)

print('*******************')
str_5 = 'Hello World! Ho\nw are you?'
print(str_5)
list_words = str_5.split()
print(list_words, type(list_words))
list_words_2 = str_5.split("!")
print(list_words_2)

joined_str_2 = '?'.join(list_words)
print(joined_str_2)

# joined_str_3 = list_words.join('?')
# print(joined_str_3) # AttributeError: 'list' object has no attribute 'join'

print('++++++++++++')
list_words_str = str(list_words)
print(list_words_str)
joined_str_3 = list_words_str.join('?')
print(joined_str_3) # AttributeError: 'list' object has no attribute 'join'
print('++++++++++++')

str_6 = '4567892'

print('-----')
print(str_5.isdigit())
print('-----')
print(str_6.isdigit())
print('-----')
# str_7 = 2
# print(str_7.isdigit()) # AttributeError: 'int' object has no attribute 'isdigit'

joined_str_1 = str_5, str_6.join('_')
print(joined_str_1)

list_1 = [1, 2, 3]
list_1.insert(0, 1000)
print(list_1)
list_1.insert(2, 2000)
print(list_1)
list_1.insert(10, 10000)
print(list_1)
list_1.insert(8, 8000)
list_1.insert(11, 11000)
print(list_1)
list_1.insert(-2, -2000)
print(list_1)
list_2 = list_1[:]
print(list_2)
print(list_1 is list_2)
list_3 = ['wert']
list_4 = ['wert']
print(list_2)
print(list_3 is list_4)
list_5 = list_4[::-1]
print(list_5)
list_6 = list_4.copy()
print(list_6)
list_1.insert(len(list_1),"*")
print(list_1)

help("for")

