""" 35. Напишите функцию, которая принимает одно число
и проверяет, является ли оно простым """


def is_prime(num: int) -> str:
    """ Функция проверки числа: является ли число простым. """
    if num == 1:
        return 'Число не является простым'
    elif num == 2:
        return 'Число простое'
    else:  # проверяем, есть ли у числа другие делители, кроме 1 и самого числа
        for i in range(2, num):
            if num % i == 0:
                return 'Число не является простым'
        return 'Число простое'


print(is_prime(int(input('Введите число для проверки на простоту -> '))))