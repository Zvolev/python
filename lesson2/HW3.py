""" Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
не превосходящие числа N.
Пример:
Ввод: 13 -> 1, 2, 4, 8 """

N = int(input())
k = 0
while 2 ** k < N:
    print(2 ** k)
    k += 1