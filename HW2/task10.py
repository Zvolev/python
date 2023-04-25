from random import randint

""" На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное количество монет,
которые нужно перевернуть. С клавиатуры вводятся число монет
и сами монеты построчно. Пример: Ввод: 1 1 1 1 0 0 -> 2 """

""" N = int(input('укажите количество монет => '))
num_eagle = 0
num_tails = 0
for _ in range(N):
    #  coin = int(input())
    coin = randint(0, 1)
    print(coin)
    if coin == 1:
        num_eagle += 1
    else:
        num_tails += 1
print(f"Минимальное количество, которые нужно перевернуть {min(num_eagle, num_tails)}") """


N = int(input('укажите количество монет => '))
num_coins = 0
for _ in range(N):
    #  coin = int(input())
    coin = randint(0, 1)
    print(coin)
    num_coins += coin
print(f"Минимальное количество, которые нужно перевернуть {min(num_coins, N - num_coins)}")
