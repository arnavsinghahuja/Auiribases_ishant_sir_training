'''
print("hello word")
#recurtion how function works
#magic variable or dunders
#print("_name_is:",__name__)
#introduction to function have 3 components
#creaate statament and make function in memory
def f(a,b): # 1st component : name and input
    print(a) # 2nd component : defination(means instruction)
    print(b) 
    a+=b
    result=a*2
    print ("result",result)
    #
 '''
'''
#2 of day
def Square(number):
    result= number*number
    return result
print("-----")
print("square is",Square)


def Square(number1,number2):
    result= number1*number2
    return result
print("         ------")
print("Square now is",Square)
print("----")
#Sqaure(10) will give error
Square(10,20)
print(Square(10,20))
'''

#3
'''
def Square(number):
    print("1,number is",number)
    number= number*number
    print("2.number is :",number)
    
number=10
print("3.number is",number)
print("-----")
Square(number)
print("4.number is",number)
list=[10,223,34,434,43,24,24]
print(len(list))
'''

