#multi value container-can hold lot of data 
# these are objects-tuple, list
'''
single value conatiner (hold up to 1 value)

int ,float,bool
multivalue container

objects-> tuple, list,string,set,dictionary


sequence-
 tuple
 lists




'''


#list
#1-D
my_data=(10,20,30)
print("mydata[0]",my_data[0])
#list of list
#2-D
numbers=[
    [10,20,30],
    [40,50,60],
    [70,80,90,100]

]
print(numbers)
print(len(numbers))

numbers=[
   [ [10,20,30],
    [40,50,60],
    [70,80,90,100]
    ],
    [ [10,20,30],
    [40,50,60],
    [70,80,90,100]
    ],
    [ [10,20,30],
    [40,50,60],
    [70,80,90,100]
    ]
]
message='''
this my life and it make 
me feel lot of emotions
 at once
'''

print("message")
print(message)
print("length of message",len(message))
print("message[1]",message[1])
print("message[-4]",message[-4])
print()

'''
indexes = list(range(0,10,1))
email="john@example.com"
name=email[0:5] #john
domain=email[6:]
print('name',name)
print("domain",domain)

'''
'''
data1=[10,20,30]
data2={40,50,60}

data3=data1*3           
print("data-----",data3)
print("meassage----", 'life' in message)
'''
#set

'''data={10,20,30,40,50}
#dictionary
student={
'roll number':1,
'name':'jhon',
'age':20,
'gender':'male',
'address':'redwood shores'
}

print('20 in data---', 20 in data )
print("roll_number in student :", 'roll_number' in student)
#
# 
# '''
