#2.4) написать функцию, которая принимает словарь и возвращает имя человека с минимальным балансом. Если таких несколько
# вернуть первого встретившегося

def first_min_balance_name(balances: dict[str, float])-> str:
    minimal = None
    minimal_name = ''
    for name, balance in balances.items():
        if minimal is None or balance < minimal:
            minimal = balance
            minimal_name = name
    return minimal_name

print(first_min_balance_name({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10}))