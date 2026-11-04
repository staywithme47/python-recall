# 1 Comprehension с квадратом числа в пределах 10 для каждого четного
print([x*x for x in range(10) if x%2==0])


#2 Comprehension для отбора животного название которого больше 4 символов
animals = ['cat', 'dog', 'elephant', 'ant', 'tiger']
print([x for x in animals if len(x) > 4])