#2.10) написать функцию, которая принимает словарь и возвращает среднее значение баланса,
# без учета максимального и минимального (максимальных и минимальных, если их несколько)

def avg_balance_wo_min_max(balances:dict[str, float | int]) -> float | int:
    minimal = None
    maximal = None

    for balance in balances.values():
        if minimal is None or balance < minimal:
            minimal = balance

        if maximal is None or balance > maximal:
            maximal = balance

    count = 0
    total = 0
    for balance in balances.values():
        if balance != minimal and balance != maximal:
            count += 1
            total += balance
    if count == 0:
        return 0.0
    average = total / count
    return average

print(avg_balance_wo_min_max({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10, "Lewis": 10000.00,
                             "John": -1500.10}))
