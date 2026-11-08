#    2.9) написать функцию, которая принимает словарь и возвращает суммарный баланс, без учета минимального
#    (минимальных если их несколько)

def sum_wo_min(balances:dict[str,int|float])->int | float:
    minimal = None

    for balance in balances.values():
        if minimal is None or balance < minimal:
            minimal = balance
    total = 0
    for balance in balances.values():
        if balance != minimal:
            total += balance

    return total

print(sum_wo_min({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10, "Lewis": 10000.00,
                             "John": -1500.10}))