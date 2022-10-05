# 13. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

str1 = input('Введите строку 1: ')
str2 = input('Введите строку 2: ')
counter = 0

for i in range(len(str2)):
  if str1 == str2[i: i+len(str1)]:
   counter += 1
print(counter)

# sp=[1,2,3,4,5,6,7,8,9,10]

# print(sp[2:4])

# print(sp[2:])

# print(sp[:2])


line1 = input("Введи 1 строку: ")
line2 = input("Введи 2 строку: ")
count = 0
def fun(line1,line2):
global count
  for i in range(len(line1) - len(line2) + 1):
       if line1[i:i+len(line2)] == line2:
             count += 1

       if len(line1) > len(line2):
     fun(line1,line2)
else:
    fun(line2,line1)

print(count)