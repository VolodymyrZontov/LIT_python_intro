# set - множина - порядок не зберігається, тільки один "представник" обʼекта
# dict - словник - структура виду ключ:значення, тільки один ключ обʼекта!

# !!!!! {} - створює СЛОВНИК

results = [1, -2,  9, 3, "qwe", 1, 1, 1, 3]
print(results)

results_set = set(results)
print(results_set)

my_set = {"1", 2, 3, (4, 5)}
print(my_set)
empty_set = set()

my_set.add("asd")
print(my_set)

my_set.pop()
print(my_set)

connections = ["John", "Jake", "Jill", "Joe", "John", "Joe", "Joe", "Joe", "Joe", "Joe", "John", "John"]

connections_set = set(connections)
print(connections_set, len(connections_set))

for user in connections_set:
    print(f"User: {user}, connections: {connections.count(user)}")
#########################################################
my_str="bla BLAQ car"

# Old school
uniques = []
for symbol in my_str.lower():
    if symbol not in uniques:
        uniques.append(symbol)
print(len(uniques), uniques)

# # Set usages
unique_set = list(set(my_str.lower()))
print(len(unique_set), unique_set)
#########################################################

person = {"name": "John",
          "age": 36,
          "city": "New York",
          "is_married": True,
          "skills": ["python", "C#"],
          1: 100,
          "job": {
              "role": "IT engineer",
              "salary": 2000}
          }

print(person["job"]["salary"])
print(person["skills"][-1])
print(person.get("age"))

person["name"] = "Jane"
person["skills"].append("Java")
person[1] = 200
person["job"]["salary"] = 3000

person["sex"] = "Female"

print(person)


###########################################

my_str = "sjdhfgvlsdknvmos;difhvskuyjfhvnalsijdcnalksjhhdvgusjzkjkdjcm ani skejhgfsuyfhcjoaLIdwhaukertgvcb"
symbols = {}
count = 0
for symbol in my_str:
    if symbol not in symbols:
        symbols[symbol] = my_str.count(symbol)
        count += 1

# print(count, symbols)

for key in symbols:  # - перебирає ключи!
    print(key, symbols[key])

for key, value in symbols.items():
    print(key, value)