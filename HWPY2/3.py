# Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, 
# выводится на экран, 
# затем перемешивается, опять выводится на экран. 
# SHUFFLE нельзя юзать!

import random
list = []
n =  10  
for i in range(1,n+1):
  list.append(i*random.randint(0,100))
print ('случайный список размерностью 10 ' ,  list)
list_shuffle=random.choices(list,k=n)
print ('перемешанный список              ', list_shuffle)

