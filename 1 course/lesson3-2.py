# value_1 = 12
# value_2 = .12
# value_3 = "12"
#
# print(value_1, value_2, value_3, type(value_1), type(value_2), type(value_3))


######################################################################
# str
# str_1 = "qwerty"
# str_2 = "1111"
# res_1 = str_1 + str_1
# print(res_1)
# res_2 = str_1 * 2
# print(res_2)

# symbol = str_1[1]
# print(symbol)

# len_str_1 = len(str_1)
# print(len_str_1)

# symbol = str_1[len(str_1) - 1]
# symbol = str_1[-1]  # Перший елемент з кінця строки
# print(symbol)

# sub_str_1 = str_1[1:4]  # З(включно):ПО(не включно)
# sub_str_1 = str_1[3:]  # До кінця строки
# sub_str_1 = str_1[:4]  # З початку строки
# sub_str_1 = str_1[:]  # З початку до кінця строки
# sub_str_1 = str_1[10:40]
# sub_str_1 = str_1[::2]  # Крок зрізу
# sub_str_1 = str_1[::-1]  # "переворот" строки
# print(sub_str_1)

######################################################################
# Методи строк
str_1 = "john Snow"
# str_1 = str_1.replace("q", "Q")
# res_1 = str_1.replace("asd", "1")
# print(res_1)
# res_2 = str_1.lower()
# res_2 = str_1.upper()
res_2 = str_1.capitalize()
print(res_2)
