#     1.10) написать функцию, которая принимает массив и возвращает среднее арифметическое эл-тов,
#     без учета максимального и минимального (максимальных и минимальных, если их несколько)
#     [-3,-2,5,4,-2,5,-3,5]--->0
def avg(arr:list[int]) -> float|int:
    minimal = arr[0]
    maximal = arr[0]
    for num in arr[1:]:
        if num < minimal:
            minimal = num
        if num > maximal:
            maximal = num
    total = 0
    count = 0
    for num in arr:
        if num != minimal and num != maximal:
            total += num
            count += 1
    if count == 0:
        return 0.0
    return total/count

print(avg([10, 6, 5, 3, -2, 1, -1, 10, 17, 7, 6]))