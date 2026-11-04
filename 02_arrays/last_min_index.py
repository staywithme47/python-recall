def last_min_index(arr:list[int])-> int:
    idx = 0
    minimal = arr[0]
    for i in range(len(arr)):
        if arr[i] <= minimal:
            minimal = arr[i]
            idx = i
    return idx

print(last_min_index([-7,0,4,11,2,3,-7,4,4,11,-7,1,6,7]))