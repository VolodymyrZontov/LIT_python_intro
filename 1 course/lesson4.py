# import string
from string import ascii_lowercase as alphabet, digits

# План:
# ввод тексту з клавіатури
# зведення типів
# тип None, bool
# *** imports
# *** try...

##################################################
# print("Start")
# value = input("Input the int number:")
# int_value = int(value)
# result = int_value * 3
# print(result)

# value = input("Input the float number:")
# float_value = float(value)
# result = float_value * 3
# print(result)

##################################################
# int(): str->int, float->int (відкидає все після коми)
# value = -5.9
# new_value = int(value)
# float(): str->float, int->float
# value = -123
# new_value = float(value)
# str(): int->str, float->str
# value = -123.4
# new_value = str(value)
# print(new_value, type(new_value))
##################################################
# none: None
# new_value = print(2 + 3)
# print(new_value, type(new_value))
##################################################
# bool: True/False
# >, <, >=, <=, ==, !=, is (для None), in (для str)

# new_value = "qwerty"
# value = "weR" in new_value
#
# value = 12 > 3
# print(value, type(value))

# value_1 = False
# value_2 = True
# or
#   T   F
#T  T   T
#F  T   F
# result = value_1 or value_2
# print(result)
# and
#   T   F
#T  T   F
#F  F   F
# result = value_1 and value_2
# print(result)
# not
#T  F
#F  T
# result = not value_1
# print(result)

# new_result = not (not value_1 or not value_2)
# print(new_result)

##################################################
# bool(): str->bool (True окрім пустої строки), int->bool (True окрім 0) , float->bool (True окрім 0.0), none->bool (False)
# value = None
# new_value = bool(value)
# print(new_value)

# value = ""
# new_value = bool(value)
# print(new_value)

# value = -1000
# new_value = bool(value)
# print(new_value)

# value = 0.01
# new_value = bool(value)
# print(new_value)

##################################################

print(alphabet, digits)