#5 Задачка на проверку палиндрома

def is_palindrome(s: str) -> bool:
   normalized = s.lower().replace(" ", "")
   return normalized == normalized[::-1]