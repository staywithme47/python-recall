# 1 Comprehension с квадратом числа в пределах 10 для каждого четного
#nums = [x*x for x in range(10) if x%2==0]
#print(nums)


#2 Comprehension для отбора животного название которого больше 4 символов
#animals = ['cat', 'dog', 'elephant', 'ant', 'tiger']

#print([x for x in animals if len(x) > 4])

#3 Задачка вернуть словарь формата символ -> сколько раз встречается
#def count_chars(s: str) -> dict:
 #   result = {}
  #  for ch in s:
   #     if ch in result:
     #       result[ch] += 1
       # else:
        #    result[ch] = 1
    #return result
#print(count_chars('hello'))

#4 Задачка вернуть строку со словами в обратном порядке

#def reverse_words(s: str) -> str:
 #   return ' '.join(s.split()[::-1])

#print(reverse_words('hello world from python'))

#5 Задачка на проверку палиндрома

#def is_palindrome(s: str) -> bool:
   #normalized = s.lower().replace(" ", "")
   #return normalized == normalized[::-1]

