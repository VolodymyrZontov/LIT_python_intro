# сортування
# лямбда-функції
# map()

people = [
    {"name": "John", "age": 25, "job": "programmer"},
    {"name": "Alice", "age": 30, "job": "designer"},
    {"name": "Eve", "age": 22, "job": "analyst"},
    {"name": "Bob", "age": 28, "job": "manager"},
    {"name": "Charlie", "age": 35, "job": "engineer"},
]


numbers = [3, 6, -1, 2, "50", 23]
ordered_numbers = sorted(numbers)
print(ordered_numbers)

points = [(2, -2), (2, -10), (1, -1)]
ordered_points = sorted(points)
print(ordered_points)

def sort_by_age(item):
    age = item["age"]
    return age

def sort_by_name(item):
    return item["name"]


def sort_by_name_length(item):
    return len(item["name"])

def sort_by_name_length_and_alphabet(item):
    return len(item["name"]), item["name"]

ordered_people = sorted(people, key=sort_by_name_length_and_alphabet)
[print(person) for person in ordered_people]

ordered_people = sorted(people, key=lambda item: item["name"])
[print(person) for person in ordered_people]

str_numbers = tuple(map(int, numbers))
names = tuple(map(sort_by_name, people))
ages = tuple(map(lambda item: item["age"], people))

print(ages)
