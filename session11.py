# oops (object oriented lsngusge)
#HAS-A 1- resturnt has 1 menu
''' ### one of theimportant topic for interview

requriement:
Mr.jhon is my client 
he is running a rsturnt 
he wantsa to build an oline food delivery system

in my application , user should be abel to login
he can select resturnt 
he can view its menu
add dishes to cart and the place an order
      1 menu has many dishes
        many resturnt has many dishes

#is -A
# what to do
1. identify th object , ie think of object
user- name, phone, email gender ,age etc
rsturnt- name , image , phone,email, address,rating,operating hours, price
menu- dishes, category, total dishes
dish-name,imahe, price, rating etc..
order- dishes,user deliveryaddress,resturant ,delivery Agent
what i observe
1 user can place many order
1 resturnt can have many dishes
many user can place many order...

etc etc
'''
'''# 2.creat class for the object
class User:
    def __init__(self):
        print("constructor executed")
        print("self:", self, type(self), id(self))

class Restaurant:
    def __init__(self):
        print("constructor executed")
        print("self:", self, type(self), id(self))


#LHS:jhon is a reference variable
#RHS:user()is creation ofa an object, which automatically executes__init__(co)
jhon=user()
mc_dounlad=resturnt()

print("jhon:",jhon)
    '''
class song:
    def __init__(self):
        print("constructor executed")
        print("self:", self, type(self), id(self))

johns_song=song()
print('johns_song:',johns_song)

print('data in object refered by johns_song')
print(vars(johns_song))
# write data in object
# name , artist, album ,duration
johns_song