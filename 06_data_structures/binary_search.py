def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)-1
    if target not in arr:
        return -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid +1

        if arr[mid] > target:
            right = mid -1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(arr, 11))     # 3
print(binary_search(arr, 15))     # -1

