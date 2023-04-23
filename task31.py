""" Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи| """


def fibonacci(n: int) -> int:
    """ Функция ищет число из ряда Фибоначи по заданному порядковому номеру """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(int(input('Какое N-е число Фибоначи найти? ->'))))