#4 Задачка вернуть строку со словами в обратном порядке

def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])

print(reverse_words('hello world from python'))