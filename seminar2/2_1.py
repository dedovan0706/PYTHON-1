# sp= [2,True,"hi",6666]
# sp.append(777) #добавить значение списку
# sp.remove (2) #удалить значение из списка
# sp.pop(-2) # удалить по индексу -2 второй справа значит
# print(sp)

# slov ={}
# slov ["Петр"] = 894564656
# slov ["Иван"] = 5465646
# print(slov)
# print(slov.keys())

sp = [2,True, "Hi",6666]
sp.append(777)
print(sp)
sp[1]="замена"
print(sp)

sp.remove(2) #удалили по значению
print(sp)

sp.pop(-1) #удалили по индексу
print(sp)

slov = {}
slov["Петр"] = 8927116646
slov["Иван"] = 444444
print(slov)
print(slov.keys())
for i in slov:
 print(i,slov[i])

for x,y in slov.items():
 print(x,y)