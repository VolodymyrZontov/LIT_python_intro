from random import randint

# Задача 1.
#
# Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 10.
# Користувач намагається вгадати число. Програма може давати підказки тільки "More", "Less", "You won!"

goal_number = randint(1, 10)

go_loop = True
while go_loop:
    try:
        user_number = int(input("Enter a number between 1 and 10: "))
        if user_number < goal_number:
            print("More")
        elif user_number > goal_number:
            print("Less")
        else:
            print("You won!")
            go_loop = False
    except ValueError:
        print("Please enter a number")

#########################################################################################################
# Задача 2.
#
# Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 12.
# Програма виводить на екран число, яке створено і назву місяця, який відповідає цьому числу.

goal_month = randint(1, 12)

if goal_month == 1:
    print(goal_month, "January")
elif goal_month == 2:
    print(goal_month, "February")
elif goal_month == 3:
    print(goal_month, "March")
elif goal_month == 4:
    print(goal_month, "April")
elif goal_month == 5:
    print(goal_month, "May")
elif goal_month == 6:
    print(goal_month, "June")
elif goal_month == 7:
    print(goal_month, "July")
elif goal_month == 8:
    print(goal_month, "August")
elif goal_month == 9:
    print(goal_month, "September")
elif goal_month == 10:
    print(goal_month, "October")
elif goal_month == 11:
    print(goal_month, "November")
elif goal_month == 12:
    print(goal_month, "December")

#########################################################################################################
# Задача 3.
#
# Написати програму в якій користувач вводить два цілих числа.
# Програма виводить результат піднесення першого числа у степінь відповідний другому числу.
# Зробити обробку всіх можливих помилок.
# В разі неможливості виконання дії - вивести відповідне повідомлення. ("Введено не число", тощо ... )

try:
    first_number = int(input("Enter an integer: "))
    second_number = int(input("Enter another integer: "))
    result = first_number ** second_number
    print(result)
except ValueError:
    print("You entered not a number")
except ZeroDivisionError:
    print("First number cannot be zero if second is negative")