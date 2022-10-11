# Идея: часто описывать функцию некогда и незачем

# Анонимные, lambda функции

def sum(x):
 return x+10

def mult(x):
 return x**2

sum(mult(2))

#****************

def sum1(x):
 return x+22

def mult2(x):
 return x**3

sum1(mult2(2))

#****************

def sum3(x):
 return x+242

def mult4(x):
 return x**5

sum3(mult2(2))

#****************

sum = lambda x: x+10
mult = lambda x: x**2
sum(mult(2))

sum1 = lambda x: x+22
mult2 = lambda x: x**3
sum1(mult2(2))

sum4 = lambda x: x+242
mult4 = lambda x: x**5
sum3(mult2(2))