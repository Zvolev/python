# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)

print("Введите элементы второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)

common_elements = sorted(list(set1.intersection(set2)))
print(f"Общие без повторений в порядке возрастания: {common_elements}")


# Сначала мы запрашиваем у пользователя n и m - количество элементов
# первого и второго множеств соответственно.
# Затем создаем два пустых множества set1 и set2.
# Затем мы запускаем два цикла for, чтобы пользователь мог
# ввести элементы каждого множества. Внутри циклов мы добавляем
# каждый введенный элемент в соответствующее множество.
# После того, как пользователь ввел все элементы, мы получаем множество,
# содержащее общие элементы, при помощи метода intersection()
# и преобразуем его к списку (чтобы отсортировать элементы)
# и выводим его на экран.