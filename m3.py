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
n=5
m=5
bomb=9
data=[[0 for i in range(n)] for j in range(m)]
print(data)
data[0][1]=bomb
data[2][3]=bomb
data[2][1]=bomb
print(data)
x=1
y=1
data.insert(0,[0]*(n+2)) #добавляем рамку сверху
data.append([0]*(n+2)) #добавляем рамку снизу
for i in range(1,m+1): #добавляем рамку с боков
    data[i].append(0)
    data[i].insert(0,0)
print(data)
#смещаем точку
x+=1
y+=1
bomb_count=0 #изначально считаем, что ничего нет
for i in range(-1,2):
    for j in range(-1,2):
        print(i,j)
        if data[x+i][y+j]==bomb:
            bomb_count+=1
print(bomb_count)

for row in range(m):
    for column in range(n):
        x=row+1
        y=column+1
        if data[x][y]!=bomb:
            bomb_count=0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if data[x + i][y + j]==bomb:
                        bomb_count+=1
            data[x][y]=bomb_count
for row in data:
    print(row)

# Напечатать таблицу змейкой
# Дано n
# 123 ->
# 654 <-
# 789 ->
result=[]
n=4
for i in range(n):
    current_list=[x for x in range(n*i+1,n*(i+1)+1)]
    print(current_list)
    if i%2==1:
        current_list.reverse()
    result.append(current_list)
for row in result:
    print(row)

# Напечатать таблицу спиралью
# 123
# 894
# 765
x=0
y=0
#x и y - начальные координаты
direction=0
#direction - направление
#направо - 0, вниз - 1, налево - 2, вверх - 3
n=3
result=[[0 for i in range(n)] for j in range(n)]
current=1
while current<n*n+1:
    if result[x][y]==0:
        result[x][y]=current #в координаты ставим начальное значение
        current+=1
    if direction==0: #движение вправо
        if y+1<n:
            y+=1
        else:
            direction+=1 #идём вниз
    elif direction==1: #движение вниз
        if x+1<n:
            x+=1
        else:
            direction+=1 #идём влево
    elif direction==2: #движение влево
        if y-1>=0:
            y-=1
        else:
            direction+=1 #идём вверх
    elif direction==3: #движение вверх
        if x-1>=0:
            x-=1
        else:
            direction=0 #движение вправо
for row in result:
    print(row)











first=[1,2,3]
second=[4,5,6]
result=[x+y for x in first for y in second]
print(result)

a=12
b=23
maximum=b if b>a else a # тернарный оператор сравнения





#---------------------------------------
# 5. Сгенерировать список вида [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ..., n, n, n, .., n] для заданного n.
values=[]
k=3
for i in range(k):
    values.append(k)
print(values)

values=[]
k=3
n=4
for k in range(1,n+1):
    for i in range(k):
        values.append(k)
    print(values)

values=[]
k=3
n=4
for k in range(1,n+1):
    for i in range(k):
        values.append(k)
print(values)

values=[]
k=3
n=4
for k in range(1,n+1):
    # for i in range(k): эту
    #     values.append(k) и эту строчки заменяем на:
    values+=[k]*k
print(values)

values=[k for k in range(1,n+1) for i in range(k)] #2 нижние строчки заменили на одну
# for k in range(1,n+1):
#     for i in range(k):
#         values.append(k) и убрали эту
print(values)
#---------------------------------------