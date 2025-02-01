# git

# Цикл — це алгоритмічна структура, за допомогою якої реалізується багаторазове повторення команд.
# Серія команд, що повторюється при кожному повторенні (ітерації) циклу, називається тілом циклу

# Обробку помилок

# value = 10
#
# while value > 0:
#     print(value)
#     value -= 1
# print("Done")

#####################################################

# value = 10
#
# while True:
#     print(value)
#     value -= 1
#     if value <= 0:
#         break
#
# print("Done")

#####################################################

# go_loop = True
#
# while go_loop:
#     value = input("Enter a string: ")
#     print(value)
#     user_input = input("Do we continue? y/n: ")
#     if user_input != "y":
#         go_loop = False

#####################################################

# go_loop = True
#
# while go_loop:
#     value = input("Enter a number: ")
#
#     try:
#         value_int = int(value)
#         result = value_int ** 2
#         new_result = 1 / result
#     # except ValueError:
#     #     result = -1
#     # except ZeroDivisionError:
#     #     result = -100
#     except (ValueError, ZeroDivisionError) :
#         result = -1000
#     print(result)
#
#     ######################
#     # if value.isdigit():
#     #     value_int = int(value)
#     #     result = value_int ** 2
#     # else:
#     #     result = -1
#     # print(result)
#     ######################
#
#     user_input = input("Do we continue? y/n: ")
#     if user_input != "y":
#         go_loop = False

#####################################################
from random import randint

rand_value = randint(1, 10)
print(rand_value)