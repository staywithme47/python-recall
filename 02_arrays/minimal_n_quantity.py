#1.4 Написать функцию, которая принимает массив и возвращает минимальный элемент.
# Если таких несколько, то вернуть значение мин. эл-та и их количество. Например, при [4,5,-2,0,-2,13,-1,-2,5,7]
# вернуть (-2, 3)

def minimal_n_quantity(numbers:list[int]) -> tuple[int, int]:
    count = 0
    minimal = None
    for i in numbers:
        if minimal is None or i < minimal:
            minimal = i
            count = 0
        if i == minimal:
            count += 1

    return minimal, count

print(minimal_n_quantity([4,5,-2,0,-2,13,-1,-2,5,7]))