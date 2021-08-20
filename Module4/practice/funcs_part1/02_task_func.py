# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке


def palindrome(number):
    number2 = number
    res = 0
    while number2 > 0:
        test = number2 % 10
        res = res*10+test
        number2 = number2 // 10
    if res == number:
        return "true"
    else:
        return "false"
