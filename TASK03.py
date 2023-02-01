"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

from check_input import check_num_input

n = ''

def main():
    global n
    while True:
        n = input('Введите число или "Q" для выхода: ')
        if n == 'Q':
            exit()

        n = check_num_input(n)
        nums = []
        num = 2
        i = 0
        while True:
            res = pow(num, i)
            if res <= n:
                nums.append(res)
            else:
                break
            i += 1


        print(nums)

main()
