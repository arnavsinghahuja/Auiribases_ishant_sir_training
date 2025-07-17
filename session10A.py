from session10 import Dish
from session10 import Menu
from session10 import Restaurant

dish1= Dish()
dish2= Dish(name='Paneer Tikka', price=200, rating=4.5)
dish3= Dish(name='Noodles', price=150, rating=4.0)

'''lets  break down ehat we ar edoing first a fall we are makin
making some classes that is dish, menu, restaurant in which we have given them value, variables which
and now we will make a list of the dish1,2,3
lets proceed

'''
dishes=[dish1,dish2,dish3]
menu=Menu(name="indian menu",
          dishes=dishes,
          number_of_dishes=len(dishes))

# print(menu)

restaurant=Restaurant(name="johnscafe",
                     phone="+91 82896253",
                     email="kjahd@gamil.com",
                     address="near your stadium",
                     rating=4.5,
                     price_per_person=500,
                     menu=menu)

restaurant.show()
