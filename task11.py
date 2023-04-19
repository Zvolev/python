# Дано натуральное число A > 1. Определите,
# каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

n = int(input())
n0 = 0
n1 = 0
n2 = 1
i = 2  # Так как 2 первых числа уже известны это 0 и 1
while n0 < n:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
    if n0 > n:
        i = 0
if i != 0:
    print(i)
else:
    print(-1)
