def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr) -1):
        for j in range(len(arr)-1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]

    return arr

test_arr = [64, 25, 12, 22, 11]


def selection_sort(arr: list[int]) -> list[int]:

    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print(selection_sort(test_arr.copy()))