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

# 5. Даны фамилия, имя и отчество. Записать их в сокращённом виде
def short_name(name,surname,family_name):
    result=surname+' '+name[0]+'. '+family_name[0]+'.'
    return result
print(short_name('Ivan','Ivanov','Ivanovich'))

# 6. Проверить, что список упорядочен в одну из сторон
def is_sorted(data):
    ordered=sorted(data)
    if ordered==data:
        return True
    ordered.reverse() #либо ordered=reversed(ordered)
    if ordered==data:
        return True
    return False
data=[1,2,3]
print(is_sorted(data))
data.reverse()
print(is_sorted(data))
data[0]=0
print(is_sorted(data))

# 7. Дан список, вернуть список, состоящий только из различных значений (порядок не имеет значения)
def distinct(data):
    elements=set()
    for value in data:
        elements.add(value)
    return list(elements)
print(distinct([1,2,2,3,3,3,3,3,3,33,3,4]))
# можно сделать так:
def distinct(data):
    return list(set(data))
print(distinct([1,2,2,3,3,3,3,3,3,33,3,4]))

# 8. Дана дата в формате "12.04.2019", требуется перевести в запись "12 апреля 2019"
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
def format_date(date):
    parts=date.split('.') #появляется список вида ['12','04','2019']
    changed_month=months.get(int(parts[1]))
    if changed_month is None:
        return 'Not found'
    else:
        return parts[0]+' '+changed_month+' '+parts[2]
print(format_date('27.12.2019'))

# 9. Дан список имён и список телефонов, сформировать словарь вида { имя: телефон }
def form_map(names,phones):
    name_to_phone=dict()
    for i in range(len(names)):
        name_to_phone[names[i]]=phones[i]
    return name_to_phone
names=['Jane','Mary']
phones=[1234,5678]
print(form_map(names,phones))

# 10. Дан список чисел, посчитать количество различных значений в нём
def diff(data):
    return len(set(data))
print(diff([1,2,2,3,3,3,3,3,3,33,3,4]))