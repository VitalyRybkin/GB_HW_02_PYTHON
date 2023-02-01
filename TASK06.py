"""
Задача 5 - HARD необязательная

Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
в N-мерном пространстве. Сначала задается N с клавиатуры, потом задаются координаты точек.
"""
from check_input import check_num_input
from random import randint
import math

N = input('Введите количество измерений: ')
N = check_num_input(N)
x_set = []
y_set = []

for _ in range(N):
    x_set.append(randint(1, 10))
    y_set.append(randint(1, 10))

print(x_set)
print(y_set)
res = 0

for _ in range(N):
    res += pow((x_set[_] - y_set[_]), 2)

print(f'Расстояние между точками в {N}-мерном пространстве: ', round(math.sqrt(res), 2))