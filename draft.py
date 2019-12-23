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
    elif user_command=='max digits sum':
    elif user_command=='count divisors':
    elif user_command=='print digits sum':