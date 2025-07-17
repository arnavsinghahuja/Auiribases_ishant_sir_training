##1
'''
# Create Statement
# MODEL: Container -> Single Value
num1 = 10
# num1: is a reference variable created in STACK of RAM
# 10 gets strored in a Container of type int in HEAP of RAM

# Read Statement
print('num1 is:', num1)
print('type of num1 is:', type(num1))
print('num1 hashcode is:', id(num1))

# Update Statement
num1 = 20

# Read Statement -> VIEW
print('num1 now is:', num1)
print('type of num1 now is:', type(num1))
print('num1 hashcode now is:', id(num1))

# Delete Statement
# Explicit (del statement) or Implicit (Automatic)
del num1

print('num1 now is:', num1)
print('type of num1 now is:', type(num1))
print('num1 hashcode now is:', id(num1))
'''

'''
# Model
# Single Value Container
# Multi Value Container

# Create Statement
instagram_user_name = 'auribises'
# LHS: Reference Variable (Name of Storage Container)
# RHS: Data

# Create Statement
followers = 300
# LHS: Reference Variable (Name of Storage Container)
# RHS: Data

tree_age = 300

# Update Statement
followers = 350

# Read Statements
print('instagram_user_name:', instagram_user_name, id(instagram_user_name), type(instagram_user_name))
print('followers:', followers, id(followers), type(followers))

print('tree_age:', tree_age, id(tree_age), type(tree_age))
'''
#2
'''
johns_age = 25

# Reference Copy Operation
fionnas_age = johns_age

# johns_age = 30

# Delete Statement
del johns_age
del fionnas_age

# print('johns_age:', johns_age, id(johns_age), type(johns_age))
print('fionnas_age:', fionnas_age, id(fionnas_age), type(fionnas_age))
'''
#2-a
'''
#Create Statement
# Multi Value Container
johns_followers = ('fionna', 'kia', 'jim', 'joe', 'jack')# tuple
ipl_player_scores = 90, 50, 30, 20, 65, 37 # tuple
menu = 'dal', 300, 'paneer', 400, 'noodles', 350 #tuple
print('johns_followers')
print('~~~~~~~~~~~~~~~')
print(johns_followers)#will print the tuple johns_followers
print('johns_followers hashcode', id(johns_followers))#will print the tuple ID that is hashcode of johns_followers
print('johns_followers type', type(johns_followers))#will print the tuple type which is tuple of johns_followers
print('~~~~~~~~~~~~~~~')

print()

print('ipl_player_scores')
print('~~~~~~~~~~~~~~~')
print(ipl_player_scores)
print('ipl_player_scores hashcode', id(ipl_player_scores))
print('ipl_player_scores type', type(ipl_player_scores))
print('~~~~~~~~~~~~~~~')

print()

print('menu')
print('~~~~~~~~~~~~~~~')
print(menu)
print('menu hashcode', id(menu))
print('menu type', type(menu))
print('~~~~~~~~~~~~~~~')

print('menu[0]:', menu[0], id(menu[0]), type(menu[0])) # only print dal due [index given]
print('menu[1]:', menu[1], id(menu[1]), type(menu[1]))
print('menu[2]:', menu[2], id(menu[2]), type(menu[2]))
print('menu[3]:', menu[3], id(menu[3]), type(menu[3]))
print('menu[4]:', menu[4], id(menu[4]), type(menu[4]))
print('menu[5]:', menu[5], id(menu[5]), type(menu[5]))
'''
#3-b
'''
restaurant = {
    'name': 'Kylin Experience',
    'description': 'Asian, Chinese, Sushi, Thai, Sichuan, Beverages',
    'address': '312 A, 3rd Floor, Elante Mall, Phase 1, Chandigarh Industrial Area, Chandigarh',
    'operating_hours': '11am to 11:30pm',
    'price_for_two': 1900,
    'phone': '+919501654007',
    'menu': [
        {
            'name': 'Exotic Vegetables Bowl',
            'price': 750,
            'description': 'A vibrant mix of exotic vegetables is stir-fried'
        },
        {
            'name': 'Veg Khow Suey Bowl',
            'price': 650,
            'description': 'Creamy coconut curry poured over noodles with veggies'
        }
    ]

}

print(restaurant)
print(restaurant['name'])
print(restaurant['operating_hours'])
print(restaurant['menu'][0])
'''
#6
'''
print ("numbers")
for index in range(0,6):
    a=int(input("enter data"))
    if a>=6:
        print (index)
        '''
# brick in the wall 
'''
structure ask user for number of bricks 
patter
john 1 brick
jack twice the brick john put
total brcks patter when jhon use five bricks
1,2,2,4,3,6,4,8,5,10
total brick 
1+2+2+4+3+6+4+8+5+10
now do this with loops
lets start
'''
'''
brick_enter_by_user=int(input("enter the value of the total number of the bricks---"))
print("total walls ",brick_enter_by_user)

total_number_of_bricks=0

for bricks in range(1,brick_enter_by_user+1):
    john=bricks
    total_number_of_bricks+=john

    print("last brick is done by john")
    if total_number_of_bricks>=brick_enter_by_user:
        break

jack=john*2
total_bricks += jack

if total_number_of_bricks>brick_enter_by_user:
    
    print ('last brick is done by the jack')
    
        
'''
# session 7

#its a simple function of squaring
'''
def square(number):
    result=number*number
    return result

print ("sqauer of 10-- ",square(10))
result_from_square = square(20)        # 200
print('result_from_square is:', result_from_square)
    
'''


