"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
2
"""
# my_str="blablacar"
# my_symbol="bla"

# Old school
# count = 0
# for idx in range(len(my_str)):
#     if my_str[idx] == my_symbol:
#         count += 1
# print(count)

# new way
# count = my_str.count(my_symbol)
# print(count)

"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""

# count = my_str.count(my_symbol)
# for _ in range(count):
#     print(my_symbol)


"""
3) У вас есть переменная my_str, тип - str. 
Большая и маленькая буква считается как один символ.
Напечатать ЧИСЛО сколько РАЗНЫХ символов встречается в my_str.  
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
# my_str="bla BLAQ car"

# Old school

# uniques = []
# for symbol in my_str.lower():
#     if symbol not in uniques:
#         uniques.append(symbol)
# print(len(uniques), uniques)

# new way ()

"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""

# my_str="bla BLAQ car"
# my_list = []
# print(id(my_list))
# for idx, symbol in enumerate(my_str):
#     if idx % 2 == 0:
#         my_list.append(symbol)
# print(my_list, id(my_list))

#######

# new_list = list(my_str[::2])
# my_list.extend(new_list)
#
# print(my_list, id(my_list))


"""
6)
Дано целое число (тип int). Определить сколько цифр в этом числе.
"""
# number = 218734681235473465923894012936845627389209039387
#
# result = len(str(number))
# print(result)


"""
7)
Дано целое число (тип int). Определить наибольшую цифру в этом числе.
"""
# number = 12345
# result = max(str(number))
# print(result)

##################
# my_str = ".*$123zAQWSZqwerty"
# # ASCII - таблиця кодування
# print(min(my_str), max(my_str))

"""
8)
Дано целое число (тип int). Составить число (int) с цифрами в обратном порядке.
"""

# number = 12345
# result = int(str(number)[::-1])
# print(result)


"""
9)
Дано целое число (тип int). Составить число с цифрами в порядке возрастания(убывания).
"""

# number = 27634572163545457123457812
#
# result = int("".join(sorted(str(number))))
# print(result)
# ############################################
# str_number = str(number)
# sorted_str_number = sorted(str_number)
# str_new_number = "".join(sorted_str_number)
# result = int(str_new_number)
# print(result)

# генератор списків

# my_str = "asjdhg364tasjdh"
# result = []
# for symbol in my_str:
#     if symbol.isdigit():
#         result.append(int(symbol))
# print(result)
#
# result_2 = [int(symbol) for symbol in my_str if symbol.isdigit()]
# print(result_2)
#
# my_list = [12, 23, 34, 45]
# result_3 = [value ** 2 for value in my_list]
# print(result_3)







# set (task 3)

