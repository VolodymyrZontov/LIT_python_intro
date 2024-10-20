# Розгалуження - це така форма організації дій, при якій в залежності від виконання або невиконання
# деякої умови здійснюється одна, або інша послідовність дій

# value = 1
#
# if value > 5:
#     result = value * 2
# else:
#     result = value * 3
#
# print("Result is:", result)
# print(value)
# print("End")
#####################################
# my_str = "qwerty"
#
# symbol = "e"
#
# if symbol in my_str:
#     print(symbol * 5)
# else:
#     print(my_str)
#####################################
# value = ""
# if value:
#     print(value)
#####################################
# value = "qWerty"
#
# first_symbol = value[0]
#
# if first_symbol == first_symbol.upper():
#     result = value
# else:
#     result = first_symbol.upper() + value[1:]
# print(result)
#####################################
# value = "qWerty"
# last_symbol = value[-1]
# if last_symbol == last_symbol.upper():
#     result = value
# else:
#     result = value[:-1] + last_symbol.upper()
# print(result)
#####################################
#   нова_змінна = значення_якщо_так if умова else значення_якщо_ні
# result = value if last_symbol == last_symbol.upper() else value[:-1] + last_symbol.upper()
# print(result)
#####################################
number = 0
# неякісний код
# if number >= 0:
#     if number > 0:
#         print(number, "- додатнє число")
#     else:
#         print(number, "- ні додатнє, ні відʼємне число")
# else:
#     print(number, "- відʼємне число")

# якісний код
if number > 0:
    print(number, "- додатнє число")
elif number == 0:
    print(number, "- ні додатнє, ні відʼємне число")
elif number < 0:
    print(number, "- відʼємне число")
else:
    print(number, "- невідоме число ))")