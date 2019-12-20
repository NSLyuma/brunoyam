print('hello')

a=123
b=2323
c=a+b
b=b-10
print(c)
name='Petr'
print(name)
c=a+b
print(c)
b*=10
print(b)
a=12.87
c=b/a
print(c)

a=12.2
a=int(a)
print(a)

a='123'
b='12'
a=int(a)

year=1995
value='I was born in '+str(year)
print(value)
print('I was born in', year)

a=7
b=2
c=5
d=(a+b+c)/3
print(d)
d=int(d)
print(d)


a=4
b=7
if a>b:
    print(a)
    print('a wins')
else:
    print(b)
    print('b wins')

value=0
if value<-10:
    print ('left')
else:
    if value>10:
        print('right')
    else:
        print('center')

if value<-10:
    print('left')
elif value>10:
    print ('right')
else:
    print('center')

if value<-10:
    print('left')
if value>10:
    print('right')
if -10 <= value <= 10:
    print('center')

a=28
b=2
if a%b<=0:
    print('0')
else:
    if a%b>=1:
        print('1')

a=548
b=565
c=264
if a>b:
    tmp=b
    b=a
    a=tmp
if b>c:
    tmp=c
    c=b
    b=tmp
if a>b:
    tmp=b
    b=a
    a=tmp

    print(b)

name='Nastya'
print(name[0])
print(type(name[3]))

subname=name[1:3:1]
print(subname)

subname=name[1:]
print(subname)

subname=name[:4]
print(subname)

print(name[ : :2])

print(name[-1])

print(name[ : :-1])

value='abcdef'
symbol='e'
count=0
for char in value:
    if char==symbol:
        count+=1
print('number of elements',count, count/len(value)*100)
count=0
for i in range(len(value)):
    char=value[i]
    print(i,value[i])
    if value[i]==symbol:
        count+=1
print('number of elements',count, count/len(value)*100)

value='aaaabbcbcbbabbc'
result=True
for char in value:
    if char not in 'abc':
        result=False
        break
print(result,value,'consists of abc')