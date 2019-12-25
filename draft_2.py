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

#hash
