""" Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
Пример:
Ввод: 5 6 -> 2 3 """

sum_num, mult_num = map(int, input().split())

for x in range(1001):
    for y in range(1001):
        if x * y == mult_num and x + y == sum_num:
            print(x, y)