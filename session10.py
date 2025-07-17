class Dish:

    # Constructor - It is used to create an object
    # it is a function
    # self is the first input, and it holds the hashcode of current object
    def __init__(self, name='NA', price=0, rating=0):
        # LHS self.name -> in the object we will create an attribute name
        # RHS name (this is the input which we can pass in the constructor as value)
        self.name = name
        self.price = price
        self.rating = rating

    # self will always be available as 1st input
    # in all the functions, created inside the class
    def show(self):
        print("------------DISH------------")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Rating:", self.rating)
        print("------------DISH------------")
        print()

class Menu:

    def __init__(self, name='NA', dishes=[], number_of_dishes=0):
        self.name = name
        self.dishes = dishes
        self.number_of_dishes = number_of_dishes

    def show(self):
        print("~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~")
        print("Name:", self.name)
        # print("Dishes:", self.dishes)
        
        print("Dishes")
        for index in range(len(self.dishes)):
            self.dishes[index].show()

        print("number_of_dishes:", self.number_of_dishes)
        print("~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~")


class Restaurant:

    def __init__(self, name='NA', phone='NA', email='NA', 
                 address='NA', rating=0, price_per_person=0, menu=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.rating = rating
        self.price_per_person = price_per_person
        self.menu = menu

    def show(self):
        print("^^^^^^^^^^^RESTURANT^^^^^^^^^^^^")
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Address:", self.address)
        print("Rating:", self.rating)
        print("Price_per_person:", self.price_per_person)
        # print("Menu:", self.menu)
        print("Menu")
        self.menu.show()
        print("^^^^^^^^^^^RESTURANT^^^^^^^^^^^^")
        