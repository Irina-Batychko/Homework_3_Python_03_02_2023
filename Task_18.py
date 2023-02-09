"""Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
Пример:
5
1 2 3 4 5
6
-> 5
"""
import random

n = int(input("Введите количество элементов в массиве:  "))
array = []

for i in range(n):
    array.append(random.randint(0, 10))
print(*array)

x = int(input("Введите искомое число:  "))

diff, close = abs(array[0]-x), array[0]

for i in range(len(array)):
    if abs(array[i]-x) < diff:
        diff, close = abs(array[i]-x), array[i]
print(f"Самый ближайший к искомому числу {x} элемент {close}")