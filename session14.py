#now normal swap

'''a=10
b=20
temp=a
a=b
b=temp
print("a:",a)
print("b:",b)
#now bubble sort
numbers=[10,30,50,20,40]
for outer in range (len(numbers) - 1):
    for inner in range (len(numbers)-outer-1):
        if numbers[inner]>numbers[inner+1]:
           temp=numbers[inner]
           numbers[inner]=numbers[inner+1]
           numbers[inner+1]=temp

print("numbers>>>",numbers)'''
# I know whats happing lets write
"""
numbers: [10, 30, 50, 20, 40]

outer  : 0, 1, 2, 3
outer  : 0
numbers: 10, 30, 50, 20, 40
----------
inner  : 5-0-1 -> 4, 
inner  : 0 to 3

inner  : 0, 10 > 30 ?
         10, 30, 50, 20, 40
inner  : 1, 30 > 50 ?
         10, 30, 50, 20, 40
inner  : 2, 50 > 20 ?
         10, 30, 20, 50, 40
inner  : 3, 50 > 40 ?
         10, 30, 20, 40, 50

----------
outer  : 1
numbers: 10, 30, 20, 40, 50
inner  : 5-1-1 -> 3, 
inner  : 0 to 2
inner  : 0, 10 > 30 ?
         10, 30, 20, 40, 50
inner  : 1, 30 > 20 ?
         10, 30, 20, 40, 50
         10, 20, 30, 40, 50
inner  : 2, 30 > 40 ?
         10, 20, 30, 40, 50

----------
outer  : 2
numbers: 10, 20, 30, 40, 50
inner  : 5-2-1 -> 2, 
inner  : 0, 10 > 20
         10, 20, 30, 40, 50
inner  : 1, 20 > 30
         10, 20, 30, 40, 50

----------
outer  : 3
numbers: 10, 20, 30, 40, 50
inner  : 5-3-1 -> 1,
inner  : 0, 10 > 20
numbers: 10, 20, 30, 40, 50

"""
#now next,
# make functions of factorial:

#my code and its wrong 
'''
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
print(factorial(4))'''
#HW print fibonachi series 
# 

#car: name, brand,price,range,hp

class car:
    def __init__(self,name,brand,price,range,hp):
        self.name=name
        self.brand=brand
        self.price=price
        self.range=range
        self.hp=hp
        self.next=None
        self.prev=None

    def __str__(self):
        return"car name:{} " \
        "                car brand{}".format(self.name,self.brand)
             
Car=car(name="harrier-",brand="tata",price=33,range=650,hp=390)
print("Car details- ",Car)