class BankClient():
    min_life=15*12

    def __init__(self,name,age,inc,status):
        self.name=name
        self.age=age
        self.inc=inc
        self.status=status

    def get_month_inc(self):
        return self.inc/12

    def accept_credit(self,value):
        pay_time=70-self.age
        if (self.inc-value/pay_time-self.min_life>0) & (pay_time>0):
            return True
        else:
            return False

max=BankClient('Max',69,1000,'investor')
print(max.age)
print(max.get_month_inc())
print(max.accept_credit(1000))

# Коти
class Cat():

    def __init__(self,name,color,weight,age):
        self.name=name
        self.color=color
        self.weight=weight
        self.age=age

    def is_healthy(self):
        if self.age==1 & 3<=self.weight<=4:
            return True
        elif self.age==2 & 3.5<=self.weight<=4.5:
            return True
        elif 3<=self.age<=25 & 4<=self.weight<=5:
            return True
        else:
            return False

    def meow(self):
        return 'meow'

proxy=Cat('Proxy','grey',3,1)
print(proxy.name)
print(proxy.color)
print(proxy.weight)
print(proxy.age)
print(proxy.is_healthy())
print(proxy.meow())