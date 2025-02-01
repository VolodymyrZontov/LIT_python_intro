# Бібліотеки в python
# venv
# pip - пакетний менеджер, requirements.txt -> pip install -r requirements.txt
# API (Application Programming Interface)
# Типи запитів в REST API (Representational State Transfer API) - GET, POST, DELETE, PUT
# бібліотека requests
# http://numbersapi.com/
# Практична частина

from random import randint

import requests


################################################
# url = "http://numbersapi.com/42"
# response = requests.get(url)
#
# if response.status_code == 200:
#     print("Факт про число:", response.text)
# else:
#     print("Помилка:", response.status_code)

################################################

def get_number_info(number: int) -> str:
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    return response.text


def get_number_unique_facts(number: int, facts_count: int) -> list[str]:
    facts = []
    for _ in range(facts_count):
        facts.append(get_number_info(number))
    return list(set(facts))


number = randint(1, 10)
# number_info = get_number_info(number)
# print(f"{number}: {number_info}")
number_facts = get_number_unique_facts(number, 5)
[print(fact) for fact in number_facts]
