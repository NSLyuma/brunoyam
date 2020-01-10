class Car:
    # model='' этот кусок был нужен, когда не было def __init__(self,model,color,horses):
    # color=''
    # horses=0
    velocity=0

    def __init__(self,model,color,horses):
        self.model=model
        self.color=color
        self.horses=horses

    def speedUp(self,vel):
        self.velocity+=vel

    def __str__(self):
        return self.model+' '+self.color

bmw=Car('BMW','red',300)
# bmw.strange_field='hello' так не надо делать
# bmw.break_car=lambda: print('car is broken')
# bmw.model='BMW' эти строки (ниже) были бы нужны, если бы мы не написали def __init__(self,model,color,horses):
# bmw.color='red'
# bmw.horses=300
bmw.speedUp(10)
print(bmw.velocity)

audi=Car('Audi','blue',315)
# audi.model='Audi'
# audi.color='blue'
# audi.horses=315

print(bmw.model,audi.model)
print(bmw.color,audi.color)

str_bmw=str(bmw)
print(bmw)
print(bmw.__dict__)



class Fraction:

    def __init__(self,delim,denom):
        self.delim=delim
        self.denom=denom

    def plus(self,other):
        a=self.delim
        b=self.denom
        c=other.delim
        d=other.denom
        return Fraction(a*d+b*c,b*d)

    def minus(self):
        a=self.delim
        b=self.denom
        c=other.delim
        d=other.denom
        return Fraction(a*d-b*c,b*d)

    def mul(self):
        a=self.delim
        b=self.denom
        c=other.delim
        d=other.denom
        return Fraction(a*c,b*d)

    def div(self):
        a=self.delim
        b=self.denom
        c=other.delim
        d=other.denom
        return Fraction(a*d,b*c)

    def to_float(self):
        return self.delim/self.denom

    def __str__(self):
        return str(self.delim)+'/'+str(self.denom)

one_half=Fraction(1,2)
one_quarter=Fraction(1,4)
three_quarter=Fraction(3,4)
three_quarter=one_half.plus(one_quarter)
print(one_half,',',one_quarter,',',three_quarter)
print(one_half.to_float(),',',one_quarter.to_float(),',',three_quarter.to_float())

a=Fraction(5,7)
b=Fraction(9,7)
c=Fraction(1,2)
d=a.plus(b)
print(d)



