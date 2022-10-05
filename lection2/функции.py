# Это фрагмент программы, используемый многократно

def function_name(x):
    # body line 1
    # . . .
    # body line n
    # optional return


# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# # print(new_string('!')) # TypeError missing 1 required

# ************************

def new_string(symbol, count = 3):

    return symbol * count
print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

*******************************

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# ***************************************

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range(1, 10):
        list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

# *******************************************