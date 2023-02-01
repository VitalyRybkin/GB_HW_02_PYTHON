"""
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
"""
from random import randint
from check_input import check_num_input

n = ''

def main():
    global n
    while True:
        n = input('Введите количество монет на столе или "Q" для выхода: ')
        if n == 'Q':
            exit()

        n = check_num_input(n)
        coins = []
        for _ in range(n):
            coins.append(randint(0 ,1))

        print(coins)

        count_heads = 0
        count_tails = 0
        for c in coins:
            if c == 0:
                count_heads += 1
            else:
                count_tails += 1

        print(f'Минимальное количество монет, которые необходимо перевернуть: {count_heads if count_heads < count_tails else count_tails}')

main()
