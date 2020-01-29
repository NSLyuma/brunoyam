# A+B (#0001)
# inp=input().split()
# a=int(inp[0])
# b=int(inp[1])
# print(a+b)

# Орешки (#0766)
# inp=input().split()
# n=int(inp[0])
# m=int(inp[1])
# k=int(inp[2])
# if n*m>=k:
#     print('YES')
# else:
#     print('NO')

# Зарплата (#0021)
# num=input().split()
# a=int(num[0])
# b=int(num[1])
# c=int(num[2])
# mn=min(a, min(b,c))
# mx=max(a, max(b,c))
# print(mx-mn)

# Торт (#0539)
# n=int(input())
# if n%2==0:
#     print(n//2)
# elif n==1:
#     print(0)
# else:
#     print(n)

# Время года (#0892)
# n=int(input())
# if 0<n<3 or n==12:
#     print('Winter')
# elif 2<n<6:
#     print('Spring')
# elif 5<n<9:
#     print('Summer')
# elif 8<n<12:
#     print('Autumn')
# else:
#     print('Error')

# Спирт (#0757)
# inp=input().split()
# c=int(inp[0])
# h=int(inp[1])
# o=int(inp[2])
# num=[c//2, h//6, o]
# print(min(num))

# Неглухой телефон (#0108)
# n=input()
# print(n)

# Бисер (#0903)
# n=int(input())
# print(n+1)

# Олимпиада (#0942)
# print(1)

# Больше-меньше (#0025)
# a=int(input())
# b=int(input())
# if a>b:
#     print('>')
# elif a<b:
#     print('<')
# else:
#     print('=')

# Эния (#0195)
# num=input().split()
# n=int(num[0])
# a=int(num[1])
# b=int(num[2])
# print(a*b*n*2)

# Гулливер (#0773)
# num=input().split()
# k=int(num[0])
# m=int(num[1])
# print(k*k*m)

# Два бандита (#0033)
# num=input().split()
# g=int(num[0])
# l=int(num[1])
# sum=g+l-1
# print(sum-g, sum-l)

# Игра (#0004)
# k=int(input())
# a=9
# b=a-k
# print(k*100+a*10+b)

# Арифметика (#0008)
# num=input().split()
# a=int(num[0])
# b=int(num[1])
# c=int(num[2])
# if a*b==c:
#     print('YES')
# else:
#     print('NO')

# Баскетбол (0061)
# a1, b1=map(int,input().split())
# a2, b2=map(int,input().split())
# a3, b3=map(int,input().split())
# a4, b4=map(int,input().split())
# a=a1+a2+a3+a4
# b=b1+b2+b3+b4
# if a>b:
#     print(1)
# elif b>a:
#     print(2)
# else:
#     print('DRAW')

# Сбор земляники (#0755)
# a, b, c=map(int,input().split())
# if a+b>c:
#     print(a+b-c)
# elif a+b==c:
#     print(0)
# else:
#     print('Impossible')

# Журавлики (#0092)
# x=int(input())
# a=b=x//6
# c=a+b
# d=x-c
# print(a, d, b)

# Три толстяка (#0754)
# a, b, c=map(int,input().split())
# if 94<=a<=727 and 94<=b<=727 and 94<=c<=727:
#     print(max(a, max(b, c)))
# else:
#     print('Error')

# Бинарные числа (#0692)