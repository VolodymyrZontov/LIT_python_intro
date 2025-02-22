# class Person:
#     name: str = "Test"
#     age: int = 0

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobby = []

    # def print(self):
    #     print(self.name, self.age, self.hobby)

    def __repr__(self):
        return f"({self.name}, {self.age})"

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, hobby: {self.hobby}"

    def get_birthday_year(self):
        return 2025 - self.age

#########################################

john_snow = Person(name='John Snow', age=20)
harry_potter = Person(name='Harry Potter', age=12)

print(john_snow)
print(harry_potter)

persons = [john_snow, harry_potter]

print(persons)

js_birthday = john_snow.get_birthday_year()
print(js_birthday)

# john_snow.print()
# harry_potter.print()

# john_snow.name = "John Snow"
# john_snow.age = 20
#
# harry_potter.name = "Harry Potter"
# harry_potter.age = 12
# harry_potter.magic = True

# print(john_snow.name)
# print(john_snow.age)
# print(john_snow.hobby)
#
# print(harry_potter.name)
# print(harry_potter.age)
# print(harry_potter.hobby)
