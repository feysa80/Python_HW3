# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10
num = int(input("Введите число: "))


def convert(number):
    result = ''
    while number > 0:
        result += str(number % 2)
        number //= 2
    return result


def reverse(string):
    new_string = ''
    for i in range(len(string) - 1, -1, -1):
        new_string += string[i]
    return new_string
print(reverse(convert(num)))

