# Когда мы знаем, что хотим

# for i in enumeration:
#     # operator 1
#     # operator 2
#     # . . .
#     # operator n


for i in 1, -2, 3, 14, 5:
    print(i)
# 1
# -2
# 3
# 14
# 5

# Знакомьтесь – range
r = range(5) # range(0, 5)
r = range(2, 5) # range(2, 5)
r = range(-5, 0) # range(-5, 0)
r = range(1, 10, 2) # range(1, 10, 2)
r = range(100, 0, -20) # range(100, 0, -20)

r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20
for i in range(5):
    print(i)
# 0 1 2 3 4


# Вложенные циклы

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)



