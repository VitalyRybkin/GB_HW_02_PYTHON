"""
задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

*Пример:*

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

from check_input import check_num_input

while True:
    k = input('Введите количество элементов ряда: ')
    if k == 'Q':
        exit()

    k = check_num_input(k)

    fst_num = 0
    snd_num = 1
    nums =[snd_num, fst_num, snd_num]
    flag = True

    for _ in range(k - 1):
        fst_num, snd_num = snd_num, fst_num + snd_num
        nums.append(snd_num)
        if flag:
            nums.insert(0, -snd_num)
            flag = False
        else:
            nums.insert(0, snd_num)
            flag = True


    print(nums)
