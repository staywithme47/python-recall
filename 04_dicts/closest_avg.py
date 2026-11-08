#    2.11) написать функцию, которая принимает словарь и возвращает имя человека, баланс которого ближе всего к среднему.
#    Если таких несколько, вернуть индекс первого встретившегося

def closest_to_avg(balances:dict[str, float|int]) -> str:
    total = 0
    count = 0

    for balance in balances.values():
        total += balance
        count += 1
    avg = total / count
    best_diff = None
    best_name = ""

    for name, balance in balances.items():
        diff = balance - avg
        if diff < 0:
            diff = -diff

        if best_diff is None or diff < best_diff:
            best_diff = diff
            best_name = name

    return best_name

print(closest_to_avg({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10, "Lewis": 10000.00,
                             "John": -1500.10}))

