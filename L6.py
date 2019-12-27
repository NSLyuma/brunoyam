#Ошибки
data=[1,2,3]
# print(data[3])

# def foo(data):
#     print(data[3])
# foo(data)

# value=1+'123'+2.3

values=dict()
# print(values[1])

# try:
#     a=int(input())
#     b=int(input())
#     print(a+b)
# except ValueError as error:
#     print('Wrong input')
#     print(error)
# finally:
#     print('finally')

file=open('test.txt','r')
for line in file:
    print(line)
file.close()

try:
    file = open('test.txt', 'r')
    for line in file:
        print(line)
except:
    print('Error occured')
finally:
    if file is not None:
        file.close()
        print('File closed')

with open('test.txt','r') as file: #то же самое, что и 'try: file = open('test.txt', 'r')'
    for line in file:
        print(line,end='')

