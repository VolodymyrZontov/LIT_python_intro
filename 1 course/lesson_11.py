# 1. Дан словник виду {str: int} (ключи - строки, значення - цілі числа).
# - Створити список ключів цього словнику
# - Створити список значень цього словнику
# - Порахувати суму числових значень цього словнику


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_keys = list(my_dict.keys())
# my_values = list(my_dict.values())
# result = sum(my_values)
#
# print(my_keys, my_values, result)

################################################

# 2. Дан словник виду {str: str} (ключи - строки, значення - строки)
# - Створити список з унікальних значень цього словнику
# - Створити строку з унікальних значень цього словнику. У якості роздільника взяти символ ___

# my_dict = {'a': 'b', 'b': 'b', 'c': 'c'}
#
# my_values = list(set(my_dict.values()))
# result = '___'.join(my_values)
#
# print(my_values, result)

################################################

# 3. Дано два списка строк однакової довжини. Створити словник з ключами із першого списка і значеннями із другого.

# my_list_1 = ['a', 'b', 'c']
# my_list_2 = [1, 2, 3]
#
# my_dict = dict(zip(my_list_1, my_list_2))
# print(my_dict)
#
# result = {}
# for idx, key in enumerate(my_list_1):
#     result[key] = my_list_2[idx]
# print(result)

################################################

# 4. Дано два списка строк однакової довжини. Строки в першому списку строки можуть бути однакові.
# Створити словник з ключами із першого списка і значеннями із другого.
# У разі повторення ключа - створити ключ з додатковим числовим суфіксом, що відповідає номеру ключа.

# my_list_1 = ['a', 'b', 'c', 'a', 'a', 'c']
# my_list_2 = [1, 2, 3, 4, 5, 6]
#
# result = {}
# indexes = {}
# for idx, key in enumerate(my_list_1):
#     if key not in result:
#         result[key] = my_list_2[idx]
#         indexes[key] = 1
#     else:
#         indexes[key] += 1
#         result[f'{key}{indexes[key]}'] = my_list_2[idx]
#
# print(result)

################################################

# def get_custom_dict():
#     my_list_1 = ['B', 'B', 'C', 'C', 'A', 'A']
#     print(my_list_1)
#
#     result = {}
#     indexes = {}
#     for idx, key in enumerate(my_list_1):
#         if key not in result:
#             result[key] = my_list_2[idx]
#             indexes[key] = 1
#         else:
#             indexes[key] += 1
#             result[f'{key}{indexes[key]}'] = my_list_2[idx]
#     print(result)
#
#
# my_list_1 = ['a', 'b', 'c', 'a', 'a', 'c']
# my_list_2 = [1, 2, 3, 4, 5, 6]
#
# get_custom_dict()
# print(my_list_1)

################################################

# def print_custom_message(msg: str = "TEST"):
#     new_msg = f"New message: {msg}"
#     print(new_msg)
#
#
# print_custom_message("Hello")
# print_custom_message("Goodbye")
# print_custom_message(123)
# print_custom_message(len)
# print_custom_message()

################################################

# def pow_two_int_numbers(num_1: int, num_2: int):
#     result = num_1 ** num_2
#     print(result)
#
#
# pow_two_int_numbers(num_2=2, num_1=3)
# pow_two_int_numbers(2, 3)
# pow_two_int_numbers(2, num_2=5)
# multiply_two_int_numbers(4, num_1=2)  # !!! error
# multiply_two_int_numbers(num_1=2, 3)  # !!! error

################################################

def pow_two_int_numbers(num_1: int, num_2: int):
    result = num_1 ** num_2
    return result


value_1 = 2
value_2 = 3

res = pow_two_int_numbers(num_1=value_1, num_2=value_2)

res *= 10

print(res)

################################################

def print_custom_message(msg):
    new_msg = f"New message: {msg}"
    print(new_msg)


msg = "TEST"
print_custom_message(msg=msg)
