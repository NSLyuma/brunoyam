data=[2,3,5,4,65]
summa=0
for number in data:
    print(number)
    summa+=number
print(summa)
print(sum(data))

zeros=[0]*30
print(zeros)

print(zeros+data)

# Посчитать количество положительных элементов в списке
data=[-3,9,6,-4,2,-5]

a=0
for number in data:
    if number>0:
        print(number)
        a+=1
print(a)
# Напечатать все чётные элементы из списка

# Напечатать элементы на чётных позициях в списке
for i in range(len(data)):
    if i%2==0:
        print(data[i])
print(data[::2])
# Среднее арифметическое элементов массива
# Напечатать все строки, длина которых больше 5

value='Hello'
print(ord('a'))
print(chr(97))
symbol='b'
upper_symbol=chr(ord(symbol)-32)
print(symbol,'->',upper_symbol)
lower_symbol=chr(ord(upper_symbol)+32)
print(upper_symbol,'->',lower_symbol)
result=''
for symbol in value:
    if symbol<='Z':
        result+=chr(ord(symbol)+32)
    else:
        result+=chr(ord(symbol)-32)
print(result)

value='Hello, world'
print(ord('a'))
print(chr(97))
symbol='b'
upper_symbol=chr(ord(symbol)-32)
print(symbol,'->',upper_symbol)
lower_symbol=chr(ord(upper_symbol)+32)
print(upper_symbol,'->',lower_symbol)
result=''
for symbol in value:
    if 'A'<=symbol<='Z':
        result+=chr(ord(symbol)+32)
    elif 'a'<=symbol<='z':
        result+=chr(ord(symbol)-32)
    else:
        result+=symbol
print(result)

