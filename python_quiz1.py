"""
Определить, какой тип будет иметь результат операции (переменная c)
"""
a = 3
b = 4
c = a / b
print(c,type(c))
"""
Посчитать сумму чисел от 1 до 100
"""
result=0
for i in range(1,101):
    result+=i
print(result)

"""
Проверить, что число является четным
"""
number = 4
if number%2==0:
    print('yes')
else:
    print('no')

"""
Будет ли работать данный код?
name = "Svetozar"
age = 24
name_and_age = name + age
"""
name = "Svetozar"
age = 24
print(name,age)

name = "Svetozar"
age = '24'
name_and_age = name + age
print(name_and_age)
"""
Проверить, если ли заданное число в списке
"""
number = 3
data = [1, 4, 2]
if number in data:
    print('yes')
else:
    print('no')

"""
Написать функцию, которая проверяет, делится ли одно число на другое без остатка
"""
def simple_division(a,b):
    if a%b==0:
        return 'yes'
    else:
        return 'no'

print(simple_division(21,7))