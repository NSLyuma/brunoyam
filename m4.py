# Дана строка, поменять в ней первый и последний символ
value='abcdef'
print(value[-1]+value[1:-1]+value[0])

# Проверить симметрию относительно середины строки (палиндром)
value='abcba'
result=True
for i in range(len(value)):
    if value[i]!=value[-i-1]:
        result=False
print(result)
print(value==value[::-1])

# Проверить, что строка сосотоит только из символов 'a', 'b', 'c'
value='aaaabbcbcbbabbc'
result=True
for char in value:
    if char not in 'abc':
        result=False
        break
print(result,value,'consists of abc')

# Сжать строку по правилу: все последовательности повторяющихся символов длины больше 1 заменить на символ +
# количество повторений 'aaabbbb' -> 'a3b4'
# распечатать цепочки повторяющихся символов
value='aaaabbbcc'+'$'
last_change=0
result=''
for i in range(len(value)-1):
    if value[i]!=value[i+1]:
        current_value=(value[last_change:i+1])
        result+=value[i]+str(len(current_value))
        last_change=i+1
print(result)

# Ошибка