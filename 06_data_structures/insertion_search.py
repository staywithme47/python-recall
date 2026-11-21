def find_insert_position(arr:list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return left

print(find_insert_position([1, 3, 5, 6], 5)) # 2
print(find_insert_position([1, 3, 5, 6], 2)) # 1
print(find_insert_position([1, 3, 5, 6], 7)) # 4