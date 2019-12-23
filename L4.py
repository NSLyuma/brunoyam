# 1
a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
print('Result = ',a+b)

# 2
n=10
for i in range(n):
    a=input('a=')
    if a=='exit':
        break
    a=int(a)
    op=input('operation:')
    if op=='exit':
        break
    b=input('b=')
    if b=='exit':
        break
    b=int(b)
    if op=='+':
        result=a+b
    elif op=='-':
        result = a - b
    elif op=='*':
        result = a * b
    elif op=='/':
        result = a / b
    print('result=',result)

# 3
value=input('Enter expression: ')
print(value.split())

# 4
while True:
    value = input('Enter expression: ').split()
    if 'exit' in value:
        break
    a=int(value[0])
    op=value[1]
    b=int(value[2])
    result=0
    if op=='+':
        result=a+b
    elif op=='-':
        result = a - b
    elif op=='*':
        result = a * b
    elif op=='/':
        result = a / b
    print('result =',result)

# 5. Есть список, мы с ним делаем всякие преобразования
data=[]
while True:
    user_input=input('Enter command: ').split()
    user_command=user_input[0]
    if user_command=='append':
        data+=[int(x) for x in user_input[1:]]
        print(data)
    elif user_command=='max':
        print(max(data))
    elif user_command=='min':
        print(min(data))
    elif user_command=='reverse':
        data.reverse()
        print(data)
    elif user_command=='sort':
        data.sort()
        print(data)
    elif user_command=='second max':
        sorted_data=sorted(data)
        print(sorted_data[-2])

# 6
#сумма цифр числа
number=123
print(sum([int(x) for x in str(number)]))
#то же самое, но по-другому
number=123
summa=0
while number!=0:
    summa+=number%10
    number//=10
print(summa)

#количество делителей числа
number=123
count=0
for i in range(2,number):
    if number%i==0:
        count+=1
        print(i)
print(count)
#то же самое, но по-другому
print(sum([1 if number%x==0 else 0 for x in range(2,number)]))

#количество делителей числа для списка чисел
print('-----')
data=[123,456,789]
for i in data:
    summa=0
    while i!=0:
        summa+=i%10
        i//=10
    print(summa)

# 7. Функции
def sum_of_digits(number):
    return sum([int(x) for x in str(number)])
print(sum_of_digits(1234))
print('-----')