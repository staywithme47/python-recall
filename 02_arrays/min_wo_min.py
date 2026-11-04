#1.8) написать функцию, которая принимает массив и возвращает элемент,который является минимальным без учета текущего
#мин.эл - та(текущих минимальных элементов, если их несколько) напри.[4, 1, 3, 2] --> 2;
# [5, -3, 9, 12, -3, 17, 0, 5, -4, 1, 13, -4, 2] - -->   -3

def min_wo_min(arr:list[int]) -> int:
    min1 =  arr[0]

    for el in arr:
        if el < min1:
            min1 = el
    min2 = None
    for el in arr:
        if el > min1:
            if min2 is None or el < min2:
                min2 = el
    return min2
print(min_wo_min([4, 1, 3, 2]))
