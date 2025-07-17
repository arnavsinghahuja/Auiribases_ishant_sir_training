
#write professionaly a solution with file handling
#using oops
#MYSQL Databases
#

'''
import datetime
date_time_stamp=datetime.datetime.now()
print(date_time_stamp,"type of date time",type(date_time_stamp))
'''
#think ofa n object
"""
visitor:-serial_no,datetilestamp,name,phoneNO,place,purpose,who
customer:name,phone,address,email,
patent:name,phone,address,email,weight,height,bphigh,bplow,sugar


"""
import datetime

class Visitor:
    def __init__(self, serialno=0, name="none", phone="none",
                 address="none", whomeToMeet="none", purpose="none"):
        self.serialno = serialno
        self.name = name
        self.phone = phone
        self.address = address
        self.whomeToMeet = whomeToMeet
        self.purpose = purpose
        self.date_time_stamp = str(datetime.datetime.now())

    def input_visitor_details(self):
        self.name = input("Enter your name: ")
        self.phone = input("Enter your phone: ")
        self.address = input("Enter your address: ")
        self.whomeToMeet = input("Whom do you want to meet: ")
        self.purpose = input("Purpose of visit: ")

    def show_details(self):
        print("Serial No:", self.serialno)
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Address:", self.address)
        print("Whom to Meet:", self.whomeToMeet)
        print("Purpose:", self.purpose)
        print("Time:", self.date_time_stamp)
    
    def __str__(self):
        # CSV String -> Comma Separated Value
        # Format for excel
        return '{},{},{},{},{},{},{}\n'.format(self.serial_no,
                                            self.date_time_stamp,
                                            self.name,
                                            self.phone,
                                            self.address,
                                            self.whomeToMeet,
                                            self.purpose
                                            )


# Utilitly class, where we will have file IO operations
# IO -> Input (reading data from file into program)
#       Output (writing data into file from program)

import os # operating system

# Controller using OOPS
class FileHelper:
    
    def __init__(self):
        
        visitor_file_path = 'visitor-log.csv'

        if os.path.exists(visitor_file_path):
            print('FileHelper Initialized')
        else:
            file = open('visitor-log.csv', 'a')
            headers = 'serial_no,date_time_stamp,name,phone,address,whome_to_meet,purpose\n'
            file.write(headers)
            print('FileHelper Initialized for the First Time')

    def write_in_file(self, content):
        file = open('visitor-log.csv', 'a')
        file.write(content)
        print('Content:', content, 'Saved in File')

    def read_file(self):
        file = open('visitor-log.csv', 'r')
        lines = file.readlines()
        print('Reading Data From File. Total Lines:', len(lines))
        for line in lines:
            print(line)

    def file_size(self):
        file = open('visitor-log.csv', 'r')
        data = file.read()
        return len(data)
    
    def lines_in_file(self):
        file = open('visitor-log.csv', 'r')
        lines = file.readlines()
        return len(lines)
    

"""
Application
"""

# Model
#from Session18 import Visitor

# Controller
#from Session18 import FileHelper

# View + Controller
class VisitorApp:

    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("Welcome to Visitor Log Book App")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        # Create a File Helper Object, which is an attribute of VistorApp
        # Has-A Relationship
        self.file_helper = FileHelper()
        print('File Size:', self.file_helper.file_size(), 'bytes')

    def show_menu(self):
        
        while True:
            print('~~~~~~~~~~Select Option~~~~~~~~~~')
            print("1: Log a Visit")
            print("2: View Visit Log Book")
            print("3: Quit")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            choice = int(input('Enter Your Choice: '))

            if choice == 1:
                self.add_visitor()
            elif choice == 2:
                '''print ('password--')
                password=input()
                if password==123456'''
                self.view_all_visitors()
            elif choice == 3:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Thank You for Using Visitor App')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print("Invalid Menu Option")

    def add_visitor(self):
        # 1. Create an Empty Visitor Object
        visitor = Visitor()
        # 2. Take Input
        visitor.input_visitor_details()
        # 3. Save Visitor in File
        visitor.serial_no = self.file_helper.lines_in_file()
        self.file_helper.write_in_file(content=str(visitor))

    def view_all_visitors(self):
        self.file_helper.read_file()
