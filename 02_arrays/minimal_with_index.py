#1.3 написать функцию, которая принимает массив и возвращает минимальный элемент и его индекс
def minimal_with_index(numbers:list[int]) -> tuple[int, int]:
    idx = 0
    for i in range(1,len(numbers)):
        if numbers[i] < numbers[idx]:
            idx = i
    return numbers[idx], idx

print(minimal_with_index([3, 40, 20, 39, 25, -5, 19, 10]))