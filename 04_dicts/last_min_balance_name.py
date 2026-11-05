#2.5) написать функцию, которая принимает словарь и возвращает имя человека с минимальным балансом. Если таких несколько
# вернуть последнего встретившегося

def last_min_balance_name(balances: dict[str, float])-> str:
    minimal = None
    minimal_name = ''
    for name, balance in balances.items():
        if minimal is None or balance <= minimal:
            minimal = balance
            minimal_name = name
    return minimal_name

print(last_min_balance_name({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10, "Lewis": 10000.00,
                             "John": -1500.10}))
