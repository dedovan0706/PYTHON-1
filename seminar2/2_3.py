# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# # - Для N = 5: 1, -3, 9, -27, 81

n = int(input('Введите число N -'))
z=1
for i in range(n):
    print(z,end=" ")
    z=z*-3
print()


# n = int(input('Введите N '))
# z = 1
# for i in range(n):
# print(z, end = " " )
# z = z * -3
# print()

import random
print(random.randint(-10,10) )

from random import randint
print (randint(-5,3) )