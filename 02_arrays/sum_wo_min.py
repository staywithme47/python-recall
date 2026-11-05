#     1.9) написать функцию, которая принимает массив и возвращает сумму эл-тов, без учета минимального (минимальных если их несколько)
#     [10,1,7,1,4,7]--->28
def sum_wo_min(arr: list[int]) -> int:
    minimal = arr[0]
    for num in arr[1:]:
        if num < minimal:
            minimal = num
    total = 0
    for num in arr:
        if num != minimal:
            total += num
    return total

print(sum_wo_min([10,1,7,1,4,7]))
