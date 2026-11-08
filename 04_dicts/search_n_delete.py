#2.7) написать функцию, которая принимает словарь и удаляет из него людей с максимальным и минимальным балансом.
#Если их несколько, то удалить всех с максимальным и минимальным балансом
from zoneinfo import reset_tzpath


def search_n_delete(balances: dict[str, float | int]) -> dict [str, float | int]:
    minimal = None
    maximal = None
    result = {}
    for name, balance in balances.items():
        if minimal is None or balance < minimal:
            minimal = balance

        if maximal is None or balance > maximal:
            maximal = balance

    for name, balance in balances.items():
        if balance != minimal and balance != maximal:
            result[name] = balance

    return result

print(search_n_delete({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10, "Lewis": 10000.00,
                             "John": -1500.10}))