# 20. Задайте список. Напишите программу, которая определит, присутствует ли 
# в заданном списке строк некое число.

seq =["uhbnsfdhu", "ij8", "jsj", "10"]

def sequence(number, seq):
    result = False

for i in seq:
    if str(number) in i:
        result = True
    break
return result

print(sequence(8, seq))

***************************************************************
def searchN(list1, n):
    global f
    for i in range(len(list1)):
        if n in list1[i]:
            f = 1
            break

try:
    n = int(input("Введите n: "))
except:
    print('Вводите числа!')
    exit()

f = 0
list1 = ['asd','qwwe','ddfgg','eeee','werwer3wewe34343w','4','233','wew']
searchN(list1,str(n))
if f == 1:
    print("есть")
else:
    print("нет")