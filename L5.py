# ФУНКЦИИ
from typing import List #это штука, чтобы использовать все функции, доступные спискам

#сумма цифр числа
def sum_of_digits(number):
    return sum([int(x) for x in str(number)])
print(sum_of_digits(1234))

#сумма квадратов цифр числа
def sum_of_q(number):
    return sum([int(x)**2 for x in str(number)])
print(sum_of_q(1234))

#сумма двух элементов
def sum_of_two_element(a,b):
    #введи 3 кавычки и нажми enter (пример того, как можно упростить)
    #строка документации
    """
    функция для вычисления суммы двух чисел
    :param a: первое число для суммы
    :type a: int
    :param b: второе число для суммы
    :type b: int
    :return: сумма двух чисел
    :rtype: int
    """
    return a+b
print(sum_of_two_element(1,2))

#функция возвращает только положительные элементы
def find_positive_elements(data):
    """

    :type data: List[int]
    """
    result=[]
    for element in data:
        if element>0:
            result.append(element)
    return result
print(find_positive_elements([1,-2,3,-5]))

def my_join(*args):
    print(args[0])
    print(args[1])
my_join('Hello','world')
my_join('a','b','c','d')

def my_join(*args):
    return ' '.join(args)
print(my_join('Hello','world'))
print(my_join('a','b','c','d'))

def my_join(*args,delimiter=' '):
    return delimiter.join(args)
print(my_join('Hello','world'))
print(my_join('a','b','c','d'))

print('hello','world','!',sep=',',end='!!!\n')

def most_common_function(*args,**kwargs):
    print(args)
    print(kwargs)
most_common_function('hello','world','!',sep=',',end='!!!')

# словарь
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
str_value = months.get(14)  # str_value=months[11] <-можно заменить на это
if str_value is None:
    print('Wrong number')
else:
    print(str_value)
# как перебрать значения в словаре (обращаемя к ключам (номера))
for value in months:
    print(value)
# показывает все номера и названия месяцев
    print(months[value])

keys = [value for value in months]
keys = months.keys()

#как добавлять новое значение в словарь
months[13]='13 month'
print(months[13])
#как удалить элемент
del months[13]

#пустой словарь (один из двух вариантов)
dictionary=dict()
dictionary={}

phones=set()
phones.add('12345')
phones.add('1235645')
print(phones)
phones.add('123445')
print(phones)
phones.add('197655')
phones.add('67645')
print(phones)

for element in phones:
    print(element)

another_phones=set()
another_phones.add('3785629765')
another_phones.add('34565')
another_phones.add('67645')

#объединение множеств
united_set=phones.union(another_phones)
print(united_set)

#пересечение множеств
intersect_set=phones.intersection(another_phones)
print(intersect_set)

element='123'
if element in united_set:
    print('yes')


# 1. Напечатать максимум из трёх чисел
def max_3(a,b,c):
    return max(a,b,c)
print(max_3(8,10,3))

# 2. Дан год (число), определить, является ли он високосным (делится на 4 и не делится на 100)
def is_vic(year):
    if year%4==0 and year%100!=0:
        return 'Yes'
    else:
        return 'No'
print(is_vic(2020))
print(is_vic(1990))
print(is_vic(2001))

# 3. Даны длины двух катетов прямоугольного треугольника, посчитать гипотенузу (c=sqrt(a^2+b^2)
def gip(a,b):
    return (a**2+b**2)**(1/2)
print(gip(12,13))

# 4. Проверить, что число является простым (делится без остатка только на 1 и на себя)
def simple_number(a):
    for i in range(2,a):
        if a%i==0:
            return 'not simple'
    return 'simple'
print(simple_number(13))

# 5. Дана дата в формате "12.04.2019", требуется перевести в запись "12 апреля 2019"
