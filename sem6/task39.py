""" Задача №39. Даны два массива чисел.
Требуется вывести те элементы первого массива
(в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве,
затем N чисел - элементы массива.
Затем число M - количество элементов во втором массиве.
Затем элементы второго массива """


def create_arr(n: int):
    """ Функция возвращает массив данных заданного размера """
    arr = []
    for i in range(n):
        arr.append(int(input(f"Введите {i+1} элемент -> ")))
    return arr
# return [int(input(f"Введите {i+1} элемент -> ")) for i in range(n)]


arr1 = create_arr(int(input("Введите размер первого массива -> ")))
arr2 = create_arr(int(input("Введите размер второго массива -> ")))
print(arr1)
print(arr2)
result = []
for element in arr1:
    if element not in arr2:
        result.append(element)
#  result = [element for element in arr1 if element not in arr2]
print(f'Ответ -> {result}')
