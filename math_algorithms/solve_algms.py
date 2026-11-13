#6) числа Фибоначчи - это последовательность чисел, которая начинается с двух единиц, а дальше каждый эл-т считается
# как сумма 2х предыдущих. Напиши ф-цию которая принимает номер n и возвращает n-ое число Фибоначчи.
# вот первые несколько чисел: 1,1,2,3,5,8,13,21,34,55,...
def fibo(n: int) -> int:
    a = 1
    b = 1
    for i in range(n-2):
        c = a + b
        a = b
        b = c

    return b




#7) НОД - наибольший общий делитель от целых чисел a и b, это наибольшее число на которое делится и a, и b.
# Например, НОД(25,35) = 5, НОД(19, 30) = 1, НОД(24,48) = 24. Напиши функцию, которая принимает два целых числа
# и возвращает их НОД

def gcd_my(a: int, b: int) -> int:
    dividers = [x for x in range(1, b+1)]
    maximal_divider = None
    for num in dividers:
        if (a % num == 0 and b % num == 0) or maximal_divider is None:
            maximal_divider = num

    return maximal_divider


def gcd_right(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a%b
    return a

print(gcd_right(990000, 1000000))

#8) Напиши функцию, которая принимает три целых числа и возвращает их НОД
# (тоже самое, только теперь все три числа на него делятся). ИСПОЛЬЗУЙ ДЛЯ ВЫЧИСЛЕНИЙ ФУНКЦИЮ из п.7

def gcd_three(a:int,b:int,c:int) -> int:
    tmp = gcd_right(a,b)
    return gcd_right(tmp,c)

print(gcd_three(15,25,35))

#9) Напиши функцию, которая принимает массив целых чисел и возвращает их НОД (все в массиве делятся на него).
# ИСПОЛЬЗУЙ ДЛЯ ВЫЧИСЛЕНИЙ ФУНКЦИЮ из п.7

def gcd_list(nums:list[int]) -> int:
    result = nums[0]
    for num in nums[1:]:
        result = gcd_right(result, num)

    return result
print(gcd_list([15,25,35, 45, 95, 155, 185, 225, 300, 600]))

#10) Напиши функцию, которая принимает массив массивов целых чисел (двумерный массив)
# и возвращает НОД всех чисел во всех массивах. ИСПОЛЬЗУЙ ДЛЯ ВЫЧИСЛЕНИЙ ФУНКЦИЮ из п.9
def gcd_2d_array(nums:list[list[int]]) -> int:
    result = nums [0][0]
    for row in nums:
        for num in row:
            result = gcd_right(result, num)
    return result
print(gcd_2d_array([[15, 25, 35, 45, 95, 155, 185, 225],[10, 5, 60, 90, 125]]))