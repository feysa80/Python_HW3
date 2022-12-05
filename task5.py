# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введите число: '))


def Fibonacci(number):
    if number in range(1, 2):
        return 1
    elif number == 0:
        return 0
    else:
        return Fibonacci(number - 1) + Fibonacci(number - 2)


def Fibonacci_nego(number):
    if number == -1:
        return 1
    elif number == -2:
        return -1
    else:
        return Fibonacci_nego(number + 2) - Fibonacci_nego(number + 1)

def Fibonacci_both(number):
    result = []
    for i in range(0, number + 1):
        result.append(Fibonacci(i))
    for i in range(1, number + 1):
        result.insert(0, Fibonacci_nego(-i))
    return result


print(Fibonacci_both(num))
