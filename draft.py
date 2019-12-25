# 5. Дана дата в формате "12.04.2019", требуется перевести в запись "12 апреля 2019"

# def change_date(data):
#     change_date('12','.',)



def my_join(*args):
    print(args[0])
    print(args[1])
my_join('Hello','world')
my_join('a','b','c','d')

def my_join(*args):
    return ' '.join(args)
print(my_join('Hello','world'))
print(my_join('a','b','c','d'))

def my_join(*args,delimiter=' '):
    return delimiter.join(args)
print(my_join('Hello','world'))
print(my_join('a','b','c','d'))

print('hello','world','!',sep=',',end='!!!\n')

def most_common_function(*args,**kwargs):
    print(args)
    print(kwargs)
most_common_function('hello','world','!',sep=',',end='!!!')