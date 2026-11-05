#2.1) написать функцию, которая принимает словарь и возвращает минимальный баланс
def minimal_balance(balances: dict[str, float])-> int|float:
    minimal = None
    for balance in balances.values():
        if minimal is None or balance < minimal:
            minimal = balance

    return minimal

print(minimal_balance({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10}))

