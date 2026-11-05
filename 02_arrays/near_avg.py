#1.11) написать функцию, которая принимает массив и возвращает индекс эл-та, значение которого ближе всего к среднему
# арифметическому эл-тов. если таких несколько, вернуть индекс первого встретившегося
#     например, [10, 6, 5, 3, -2, 1, -1, 10, 17, 7, 6]---->1 (здесь среднее арифм = 5.63636)
def near_avg(arr:list[int])-> int:
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1

    avg = total / count
    idx = 0
    best_diff = arr[0] - avg
    if best_diff < 0:
        best_diff = -best_diff

    for i in range(1,count):
        diff = arr[i] - avg
        if diff < 0:
            diff = -diff

        if diff < best_diff:
            best_diff = diff
            idx = i
    return idx


print(near_avg([10, 6, 5, 3, -2, 1, -1, 10, 17, 7, 6]))