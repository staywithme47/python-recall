#1.1 Написать функцию, которая принимает массив и возвращает минимальный элемент
def search_minimal(numbers: list[int]) -> int:
    minimal = numbers[0]
    for number in numbers[1:]:
        if minimal is None or number < minimal:
            minimal = number
    return minimal

print(search_minimal([10, -2, 17,-52,35,40, -52]))