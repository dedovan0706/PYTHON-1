# 26. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# Отношения к нормальной, положительной последовательности чисел Фибоначчи:
# {\displaystyle F(-n)=(-1)^{n+1}\cdot F(n)}



def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input


def fib(n):
 if n == 0:
    return 0   
 if n in [1, 2]:
  return 1
 else:
  return fib(n-1) + fib(n-2)

num = check_input('Введите число k:')
list1 = []
for e in range(num+1):
 list1.append(fib(e))
print(list1) # [0, 1, 1, 2, 3, 5, 8, 13, 21]

list2=[]
for el in range(0,num):
    if el%2!=0:
        list2.append(-list1[el+1])
    else: 
        list2.append(list1[el+1])
print(list2) #[1, -1, 2, -3, 5, -8, 13, -21]

list2= list2[::-1]
print(list2) #[1, -1, 2, -3, 5, -8, 13, -21]
list3 = list()
list3=list2+list1
print(list3)