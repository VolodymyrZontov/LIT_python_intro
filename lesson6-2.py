# git

# Цикл — це алгоритмічна структура, за допомогою якої реалізується багаторазове повторення команд.
# Серія команд, що повторюється при кожному повторенні (ітерації) циклу, називається тілом циклу

# Обробку помилок

########################################

# value = 10
#
# while value > 0:
#     print(value)
#     value -= 1
#
# print("done")
########################################

# value = 10
#
# while True:
#     print(value)
#     value -= 1
#     if value <= -100:
#         break
#
# print("Done")

########################################

# go_loop = True
#
# while go_loop:
#     value = input("Enter a string: ")
#     print(value)
#     user_input = input("Do you want to continue? (y/n): ")
#     if user_input != "y":
#         go_loop = False
#
# print("Goodby!")

########################################

# go_loop = True
#
# while go_loop:
#     value = input("Enter a number: ")
#
#     try:
#         value_int = int(value)
#         result = value_int ** 2
#         new_res = 1 / result
#         print("new_res", new_res)
#     # except ValueError:
#     #     result = -1
#     # except ZeroDivisionError:
#     #     result = -100
#     except (ValueError, ZeroDivisionError):
#         result = -1000
#
#     #############################
#     # if value.isdigit():
#     #     value_int = int(value)
#     #     result = value_int ** 2
#     # else:
#     #     result = -1
#     #############################
#
#     print(result)
#
#
#     user_input = input("Do you want to continue? (y/n): ")
#     if user_input != "y":
#         go_loop = False
#
# print("Goodby!")

########################################
# from random import randint
#
# rand_value = randint(1, 10)
# print(rand_value)