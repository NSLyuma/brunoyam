# 7. Функции
def sum_of_digits(number):
    return sum([int(x) for x in str(number)])
print(sum_of_digits(1234))
print('-----')


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