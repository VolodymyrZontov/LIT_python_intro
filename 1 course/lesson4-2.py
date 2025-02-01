# import string
# from string import ascii_lowercase as alphabet, digits

# План:
# ввод тексту з клавіатури
# зведення типів
# тип None, bool
# *** imports

##################################################
# print("Start")
# value = input("Input some string:")
# print(value, type(value))

# value = input("Input some int number:")
# new_value = int(value)
# result = new_value * 5
# print(result, type(new_value))

# value = input("Input some float number:")
# new_value = float(value)
# result = new_value * 5
# print(result, type(new_value))

##################################################
# str->int, str->float, int->float, float->int (відкидання дробової частини), int->str, float->str

# value = -12.99
# new_value = str(value)
# print(new_value)

##################################################
# NoneType: None

# value = None
# print(value, type(value))
# value = print(2 + 3)
# print(value, type(value))

##################################################
# bool: True/False
# >, <, >=, <=, ==, !=, is (для None), in (для str)
# value = 12 != 120

# new_value = None
# value = new_value is None

# new_value = "qYwerty"
# value = "QY" in new_value.upper()
# print(value, type(value))

##################################################
# or, and, not

# or
#   T   F
#T  T   T
#F  T   F

# value_1 = False
# value_2 = False
# result = value_1 or value_2
# print(result)


# and
#   T   F
#T  T   F
#F  F   F

# value_1 = False
# value_2 = False
# result = value_1 and value_2
# print(result)


# not
#T  F
#F  T

# value = False
# result = not value
# print(result)

# server_response = True
# password_confirmed = False
#
# result = not(server_response and not password_confirmed) or password_confirmed
# print(result)

##################################################
# none->bool (False), int->bool (True окрім 0), float->bool (True окрім 0.0), str->bool (True окрім "")

# value = None
# new_value = bool(value)
# print(new_value)

# value = ""
# new_value = bool(value)
# print(new_value)

##################################################
# print(alphabet, digits)