# Розгалуження - це така форма організації дій, при якій в залежності від виконання або невиконання
# деякої умови здійснюється одна, або інша послідовність дій

# value = -12
#
# if value > 0:
#     result = value + 1
# else:
#     result = value * -1
#
# print("Result is:", result)
# print("End")
#####################################
# value = ""
#
# if value:
#     print(value)
#####################################
# my_str = "qwerty"
# symbol = "a"
# if symbol in my_str:
#     print(symbol, "in", my_str)
# else:
#     print(symbol, "not in", my_str)
#####################################
# my_str = "QwertY"
# first_symbol = my_str[0]
#
# if first_symbol == first_symbol.upper():
#     result = my_str
# else:
#     result = first_symbol.upper() + my_str[1:]
#
# print(result)
#####################################
# my_str = "QwErty"
# last_symbol = my_str[-1]
#
# if last_symbol == last_symbol.upper():
#     result = my_str
# else:
#     result = my_str[:-1] + last_symbol.upper()
# print(result)

#####################################
#   нова_змінна = значення_якщо_так if умова else значення_якщо_ні
# result = my_str if last_symbol == last_symbol.upper() else my_str[:-1] + last_symbol.upper()
# print(result)

#####################################
# number = -10
# неякісний код
# if number >= 0:
#     if number > 0:
#         print(number, "- додатне число")
#     else:
#         print(number, "- ні додатне, ні відʼемне число")
# else:
#     print(number, "- відʼємне число")

# якісний код
# if number > 0:
#     print(number, "- додатне число")
# elif number == 0:
#     print(number, "- ні додатне, ні відʼемне число")
# elif number < 0:
#     print(number, "- відʼємне число")
# else:
#     print("Щось ми не врахували ))")