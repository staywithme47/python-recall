#1.5написать функцию, которая принимает массив и удаляет из него максимальный и минимальный элемент. Если их несколько,
# то удалить все максимальные и все минимальные эл-ты. Напр, при [-7,0,4,11,2,3,-7,4,4,11,-7,1,6,7]->[0,4,2,3,4,4,1,6,7]

def delete_min_n_max(numbers:list[int]) -> list[int]:
    minimal = maximal = numbers[0]
    for i in numbers[1:]:
        if i < minimal:
            minimal = i
        if i > maximal:
            maximal = i
    return [num for num in numbers if num != minimal and num != maximal]
print(delete_min_n_max([-7,0,4,11,2,3,-7,4,4,11,-7,1,6,7]))