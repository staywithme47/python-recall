#2.8) написать функцию, которая принимает словарь и возвращает баланс, который является минимальным без учета текущего мин.
# баланса (текущих минимальных балансов, если их несколько)

def minimal_wo_current(balances: dict[str, float | int]) -> float|int:
    minimal = None
    sec_min = None
    for balance in balances.values():
        if minimal is None or balance < minimal:
            minimal = balance

    for balance in balances.values():
        if balance != minimal:
            if sec_min is None or balance < sec_min:
                sec_min = balance

    return sec_min

print(minimal_wo_current({"Ann": -1486.00,"Boris":15000,"Kent":4982, "Clarck":-1500.10, "Lewis": 10000.00,
                             "John": -1500.10}))