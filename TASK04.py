"""
Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для.
проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) .
Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, сами значения предикатов случайные,
проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , сколько времени отработала программа.
В конце вывести результат проверки истинности этого утверждения.

Таблица истинности оператора AND
x	    and	y	    Результат
True	and	True	True
True	and	False	False
False	and	True	False
False	and	False	False

Таблица истинности оператора OR
x	    or	y	    Результат
True	or	True	True
True	or	False	True
False	or	True	True
False	or	False	False

Всегда будет false = false, кроме случая, когда все предикаты = false, тогда true = true
"""
import random
import time

start = time.time()
check_theory = 100
for _ in range(check_theory):
    n = random.randint(5, 25)
    predics = []
    for _ in range(n):
        predics.append(bool(random.getrandbits(1)))

    print(predics)

    not_or_sequence = predics[0]
    not_and_sequence = not predics[0]
    for p in range(1, len(predics)):
        not_or_sequence = bool(not_or_sequence or predics[p])
        not_and_sequence = bool(not_and_sequence and not predics[p])

    not_or_sequence = not not_or_sequence
    print(not_or_sequence, ' = ', not_and_sequence)

end = time.time()
print('Время исполнения - ', end-start)

"""
Проверка для всех предикатов = false
"""

predics = [False, False,  False,  False,  False,]

not_or_sequence = predics[0]
not_and_sequence = not predics[0]
for p in range(1, len(predics)):
    not_or_sequence = bool(not_or_sequence or predics[p])
    not_and_sequence = bool(not_and_sequence and not predics[p])

not_or_sequence = not not_or_sequence
print('\nПроверка когда все предикаты false:')
print(predics)
print('Проверка:', not_or_sequence, ' = ', not_and_sequence)
