a=10
b=20
values=[x**2 for x in range(a,b+1)]

for x in range(a,b+1):
    values.append(x**2)

print(values)
# Строка 3 синонимична строкам 5 и 6, то есть это одно и тоже

# Покажет все чётные числа
values=[x for x in values if x%2==0]
print(values)

# Всё что меньше 200 заменяем на 100, всё что больше 200 - на 400
values=[100 if x<200 else 400 for x in values]
print(values)

# Таблица
print('TABLE')
n=4 #столбец
m=5 #строка
data=[[0 for y in range(m)] for x in range(n)]
print(data)
# Таблица прям таблица
for row in data:
    for element in row:
        print(element,end='')
    print()
print()
# Индексы
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j],end='')
    print()

# Сгенерировать список чисел от A до B
a=5
b=50
value=[x for x in range(a,b+1)]
print(value)
# Либо так:
print([x for x in range(a,b+1)])

# Сгенерировать список степеней двойки от 0 до n [1,2,4,8,...]
n=10
value=[2**i for i in range(n)]
print(value)

# Оставить в спискетолько строки полностью в верхнем регистре
value='abc'
upper_case=value.upper() # 'ABC'
print(value,upper_case)
values=['HELLO','world']
values=[x for x in values if x==x.upper()]
# Строчку выше можно заменить на "values=[x for x in values if x.isupper()]"
print(values)

# Сгенерировать список вида [1,2,2,3,3,3,4,4,4,4,...]

# Дано число n, сгенерировать таблицу умножения nxn и сохранить в список (таблицу)
print('TABLE NxN')
n=3
data=[[0 for y in range(n)] for x in range(n)]
for row in range(len(data)):
    for column in range(len(data[row])):
        data[row][column]=(row+1)*(column+1)
        print(data[row][column],end=' ')
    print()
print(data)


# Сгенерировать поле для игры "Сапер"
# [[0,-1,0],
#  [0,0,0],
#  [-1,0,0]]
# -1 - это мины

# Напечатать таблицу змейкой
# Дано n
# 123 ->
# 654 <-
# 789 ->

# Напечатать таблицу спиралью
# 123
# 894
# 765



first=[1,2,3]
second=[4,5,6]
result=[x+y for x in first for y in second]
print(result)

a=12
b=23
maximum=b if b>a else a # тернарный оператор сравнения