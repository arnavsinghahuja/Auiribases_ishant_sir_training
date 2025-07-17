'''
def fun(*arge,**karge,):
    print(arge)
    print(karge)

fun(10,20,30,name="jhon",age=20,email="afkkjbg")
'''

'''
def print_number(number):
    print (number)
    if number > 1:
        print_number(number=number-1)
        return number

print_number(10)
'''
'''# incomplete
def get_max(data,length):
    #base case
    if len(data)==1:
        return data
    else:
        prev=get_max(data,length)
        current=data[length-1]
number=[10,20,30]
max_in_number=get_max(data=number,length=len(number))
print("max_in_number:",max_in_number)
'''
def add(number1,number2=100,number3=11):
    result=number1+number2+number3
    return result

resultofadd=add(100)
print("resultfrom",resultofadd)