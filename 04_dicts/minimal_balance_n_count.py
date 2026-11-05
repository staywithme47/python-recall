#2.6) написать функцию, которая принимает словарь и возвращает минимальный баланс. Если людей с таким балансом
# несколько, то вернуть минимальный баланс и количество людей с таким балансом

def minimal_balance_n_count(balances: dict[str, float])-> tuple:
    minimal = None
    count = 0
    for balance in balances.values():
        if minimal is None or balance < minimal:
            minimal = balance
            count = 1
        elif balance == minimal:
            count += 1
    return minimal, count

print(minimal_balance_n_count({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10, "Lewis": 10000.00,
                             "John": -1500.10}))