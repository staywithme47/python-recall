#2.3 Написать функцию, которая принимает словарь и возвращает имя человека с минимальным балансом и его баланс

def minimal_balance_n_name(balances: dict[str,float])-> tuple:
    minimal = None
    name_minimal = ''

    for name, balance in balances.items():
        if minimal is None or balance < minimal:
            minimal = balance
            name_minimal = name
    return name_minimal, minimal

print(minimal_balance_n_name({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10}))