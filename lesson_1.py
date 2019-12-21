# 1. Найти среднее арифметическое трёх чисел в двух вариантах: только целую часть и точное значение.
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=(a+b+c)//3
e=(a+b+c)/3
print(d)
print(e)

# 2. Определить, какому из трех отрезов (-inf; -10), [-10; 10], (10; inf) принадлежит заданная точка.
a=int(input('a='))
if a<-10:
    print('left')
elif -10<=a<=10:
    print('center')
else:
    print('right')

# 3. Проверить четность числа.
a=int(input('a='))
if a%2==0:
    print('even')
else:
    print('odd')

# 4. Проверить, делится ли одно число на другое без остатка. Если не делится - напечатать остаток от деления.
a=int(input('a='))
b=int(input('b='))
if a%b==0:
    print('ok')
else:
    print(a%b)

# 5. Среди трех различных чисел выбрать "среднее".
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>b and a<c:
    print(a)
elif b>a and b<c:
    print(b)
else:
    print(c)

# 6. Дана строка, в которой записано трехзначное целое число. Нужно проверить, делится ли это число на 3.
a=int(input('a='))
if a%3==0:
    print('yes')
else:
    print('no')

# 7. Дано три числа. Подсчитать разницу между самым большим и самым маленьким значением.
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>c and c>b:
    print(a-b)
elif a>b and b>c:
    print(a-c)
elif b>c and c>a:
    print(b-a)
elif b>a and a>c:
    print(b-c)
elif c>b and b>a:
    print(c-a)
else:
    print(c-b)

# 8. Дано два числа x и y - координаты точки на плоскости, необходимо сказать в какой четверти лежит эта точка.
x=int(input('x='))
y=int(input('y='))
if x>0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
elif x>0 and y<0:
    print('4')
else:
    print('0')

# 9. Дано три числа. Проверить, что существует треугольник с такими сторонами (выполняется неравенство треугольника:
# сумма любых двух сторон больше, чем третья).
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a+b>c and b+c>a and c+a>b:
    print('yes')
else:
    print('no')

# 10. Дано шестизначное целое число (первая цифра не 0). Проверить, что сумма первых трех цифр равна сумме последних
# трех цифр.
# 1 вариант
a=int(input('a='))
d1=100000
d2=10000
d3=1000
d4=100
d5=10
d6=1
a1=a//d1
b1=a1*d1
a2=(a-b1)//d2
b2=a2*d2
a3=(a-b1-b2)//d3
b3=a3*d3
a4=(a-b1-b2-b3)//d4
b4=a4*d4
a5=(a-b1-b2-b3-b4)//d5
b5=a5*d5
a6=(a-b1-b2-b3-b4-b5)//d6
if a1+a2+a3==a4+a5+a6:
    print('yes')
else:
    print('no')

# 2 вариант
a1=int(input('a1='))
a2=int(input('a2='))
a3=int(input('a3='))
a4=int(input('a4='))
a5=int(input('a5='))
a6=int(input('a6='))
if a1+a2+a3==a4+a5+a6:
    print('yes')
else:
    print('no')