def binary_search_recursive(arr: list[int], target: int, left: int = 0, right: int = None) -> int:
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search_recursive(arr, target, left = mid + 1, right = right)

    else:
        return binary_search_recursive(arr, target, left, right = mid -1)


arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search_recursive(arr, 15)) # 7
print(binary_search_recursive(arr, 1))  # 0
print(binary_search_recursive(arr, 100))# -1


