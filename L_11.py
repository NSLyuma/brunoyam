import re

pattern=re.compile('hello')
value='world, hello some'
print(re.search(pattern,value))

pattern=re.compile('^hello$')
value='world, hello some'
print(re.search(pattern,value))

pattern=re.compile('^world')
value='world, hello some'
print(re.search(pattern,value))

pattern=re.compile('^\w\w\w$')
print(re.search(pattern,'abF'))
print(re.search(pattern,'asdfgh'))

pattern=re.compile('\d\d\d')
print(re.search(pattern,'Hello, 63467'))

pattern=re.compile('^Hello,\s\w\w\w\w!')
print(re.search(pattern,'Hello, Nast!'))

pattern=re.compile('^\d{4}$')
print(re.search(pattern,'1234'))
print(re.search(pattern,'12345'))

pattern=re.compile('^\d{4,10}$')
print(re.search(pattern,'123'))
print(re.search(pattern,'1234'))
print(re.search(pattern,'12345'))

pattern=re.compile('^\d{4,}$')
print(re.search(pattern,'123'))
print(re.search(pattern,'1234'))
print(re.search(pattern,'1234572547427'))

pattern=re.compile('^\d{,}$') # от -бесконечности до +бесконечности
print(re.search(pattern,'12'))
print(re.search(pattern,'1234572547427'))

pattern=re.compile('^[abc]+$')
print(re.search(pattern,'abababccbacbabcab'))
print(re.search(pattern,'abababccbacbabcabe'))

pattern=re.compile('^[0-5]+$')
pattern=re.compile('^[b-z]+$')
print(re.search(pattern,'234bht'))
print(re.search(pattern,'234234234'))

pattern=re.compile('^(hello|world|something)$')

# 1. Дана дата DD.MM.YYYY
# 12.12.1200 - OK
# 45.17.1230 - FAIL
pattern=re.compile('(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[012])\.(\d{4})')
result=re.search(pattern,'17.01.2020')
print(result.groups())
print(result.group(1))
print(result.group(0))

# 2. +7xxx-xxx-xx-xx
# +7999888-77-66 - OK
# +89998887766 - FAIL
pattern=re.compile('\+7-\d{3}-?\d{3}-?\d{2}-?\d{2}')
print(re.search(pattern,'+7-999-888-77-66'))

# 3. Чётное число
pattern=re.compile('[02468]$')
print(re.search(pattern,'3421516'))

# 4. Шестнадцатеричная запись цвета
# #FF42A5 0-9 A-F
# #(\d|[A-F]){6}


pattern=re.compile('hello',re.IGNORECASE)
print(re.search(pattern,'helLO'))
pattern=re.compile('hello',re.IGNORECASE|re.A)
print(re.search(pattern,'helLO'))

print(re.match(pattern,'hello')) # match в отличие от search находит не все, а только первый
print(re.findall(pattern,'hello'))
print(re.sub('\s+',' ','Hello      world,   it\'s me!!')) # первый аргумент - что заменить, второй аргумент - на что заменить