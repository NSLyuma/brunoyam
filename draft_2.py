#функция, которая преобразует номер месяца в количество дней
def number_of_days(month_number):
    if month_number==1: #feb
        return 28
    else:
        if month_number<7:
            return 30 if month_number%2==1 else 31 #jan-jul
        else:
            return 31 if month_number%2==1 else 30 #aug-dec
print(number_of_days(9))

#словарь
weather=dict()
months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
for i in range(len(months)):
    current_month=months[i]
    weather[current_month]=[0]*number_of_days(i)
print(weather)

#добавляет температуру в каждый день месяца
with open('data_one_year.txt','r') as data:
    for month in months:
        current_days=weather[month]
        for i in range(len(current_days)):
            current_days[i]=int(data.readline())
print(weather)
print(weather['may'][7])

#функция, которая разбирается с командой average
def process_average (user_input):
    if len(user_input) > 2:
        first = user_input[1]
        second = user_input[2]
    elif user_input[1]=='year':
        summa = 0
        for month in weather:
            summa += sum(weather[month])
        print(summa / 365)
    else:
        days = weather[user_input[1]]
        print(sum(days)/len(days))

def process_command(user_input,year_process,month_process,range_process):
    if len(user_input)>2:
        range_process()
    elif user_input[1]=='year':
        year_process
    else:
        month_process

def year_process_average(user_input):
    first = user_input[1]
    second = user_input[2]

def month_process_average(user_input):

def

while True:
    try:
        user_input=input().split()
        command=user_input[0]
        if command=='temp':
            month=user_input[1]
            day=int(user_input[2])
            print(weather[month][day])
        elif command=='average':
            if len(user_input)>2:
                first=user_input[1]
                second=user_input[2]
            elif user_input[1]=='year':
                summa=0
                for month in weather:
                    summa+=sum(weather[month])
                print(summa/365)
            else:
                days=weather[user_input[1]
                ]




        if command=='a_m':
            month=user_input[1]
            print(sum(weather[month])/len(weather[month]))
        if command=='a_y':
            print(sum(weather)/365)
    except:
        print('Wrong command')