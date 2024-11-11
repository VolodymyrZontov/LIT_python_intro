from string import ascii_lowercase as alphabet
######################################

my_str = "ajwh"

for symbol in my_str:
    print(symbol)

######################################
# f-строки

name = "John"
email = "test@test.com"
msg = "User " + name + " with email " + email + " created"
msg = f"User {name} with email {email} was created"

print(f"{name=}, {email=}")

######################################

for symbol in alphabet:
    if symbol not in "eyuioa":
        print(symbol)

print(f"{symbol=}")

######################################

my_str = "qwerty"
new_str = ""

for idx, symbol in enumerate(my_str):
    # print(f"{idx}: {symbol}")
    # // - ділення націло, % - остача від ділення
    if idx % 2 == 0:
    # if not idx % 2:
        new_str += symbol.upper()
    else:
        new_str += symbol
    print(f"{idx=} {new_str=}")

print(f"===>{new_str=}")

######################################

for value in range(3):
    print(value)

######################################
# кортеж (tuple) - неможна змінити!!! (оптимізація виділення памʼяті)
first_tuple = ("a", "b", "c")
my_tuple = (1, "qwe", 3.14, "asd", alphabet, first_tuple)
new_tuple = my_tuple[:-1] + first_tuple
print(new_tuple)
print(my_tuple)

for value in my_tuple:
    print(f"{value=}, {type(value)=}")

######################################
# список (list) - можна змінити!!!
first_list = ["a", "b", "c"]
my_list = [1, "qwe", 3.14, "asd", alphabet, first_list]

print(my_list)

my_list[0] = "qweqweqwe"
print(my_list)

print(my_list[3][-1])
######################################
my_str = "jvbjySRBNLNkgcshdbccGCVHJBHlvycrvjKJNI"

results = []

for symbol in my_str:
    if symbol.upper() == symbol:
        results.append(symbol)
        print(results)

for value in range(len(results)):
    last_value = results.pop()
    print(results, last_value)

res = ["aa", "bb", "cc", "dd", "ee", "ff", "1"]
res_str = " ".join(res)
print(res_str)

res_str = "".join(results)
print(res_str)
