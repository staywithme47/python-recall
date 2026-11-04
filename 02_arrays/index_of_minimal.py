#1.2) написать функцию, которая принимает массив и возвращает индекс минимального элемента
def index_of_minimal(numbers:list[int]) -> int:
    idx = 0
    for i in range(1,len(numbers)):
        if numbers[i] < numbers[idx]:
            idx = i
    return idx

print(index_of_minimal([3, 40, 20, 39, 25, -5, 19, 10]))