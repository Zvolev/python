""" Задача 36. На вход программы поступает строка в формате:
ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
Ввод:
house=дом car=машина men=человек tree=дерево
Вывод:
(('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево')) """


s = "house=дом car=машина men=человек tree=дерево"
tp = tuple(map(lambda x: tuple(x.split('=')), s.split()))

""" Каждый элемент исходной строки разбивается методом split()
и результат обрабатывается лямбда-функцией, которая создает кортеж
из двух элементов с помощью метода split('='). Затем все элементы,
полученные после этого разбиения, превращаются в кортежи,
которые объединяются в один конечный кортеж. """
