#3 Задачка вернуть словарь формата символ -> сколько раз встречается
def count_chars(s: str) -> dict:
    result = {}
    for ch in s:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result
print(count_chars('hello'))