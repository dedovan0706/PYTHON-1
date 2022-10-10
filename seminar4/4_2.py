# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python


def seq():
    if(a == 0 or b == 0 or c == 0):
        print("Уравнение не имеет решения")
    else:
        d=(b**2-4*a*c)
    if (d < 0):
        print("Уравнение не имеет решения")
    elif d == 0:
        x = -(b/(2*a))
        print(x)
    elif d > 0:
        x1 = (-b+(d**0.5))/(2*a)
        x2 = (-b-(d**0.5))/(2*a)
        print(x1,x2)

try:
    a = int(input("Введите коэф. а: "))
    b = int(input("Введите коэф. b: "))
    c  = int(input("Введите коэф. c: "))
    seq()
except:
    print("Некорректный ввод!")