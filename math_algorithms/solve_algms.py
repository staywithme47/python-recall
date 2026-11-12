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

