'''

databases helper class
which will have crud operation for the object
1. create connection
2.create  curser from connection
3. prepare  SQL statement to be executed


'''
'''#-- my won't work as there is noo daabases 
import mysql.connector as db


class DBhelper:
    def __init__(self):
        # 1. Create Connection
    self.connection  = db.connect(
    user='root',
    password='',
    host='127.0.0.1',
    database='gw2025'
)
print("[DB helper] connection cerated...")
#2 create curser from connection
self.cursor =self.connection.cursor()
print("[DB helper] connection cerated...")
#3
'''


"""
    DoctorsApp
"""

# View + Controller

import datetime
from session19A import Patient

class DoctorsApp:

    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Welcome to Doctors App')
        print('App Started at: ', datetime.datetime.now())
        print('~~~~~~~~~~~~~~~~~~~~~~~~~')


    def show_main_menu(self):

        while True:

            print('Main Menu: ')
            print('1: Patient')
            print('2: Consulatation')
            print('3: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                self.show_patient_menu()
            elif choice == 2:
                self.show_consultation_menu()
            elif choice == 3:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Thank You for using Doctors App')
                print('App Closed at: ', datetime.datetime.now())
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('Enter Suitable Menu Option...')


    def show_patient_menu(self):

        print('~~~~~~~~~~~~~~~~~~~~~~')
        print('Patient Menu Opened')
        print('~~~~~~~~~~~~~~~~~~~~~~')

        while True:
            print('Patient Menu: ')
            print('1: Add New Patient')
            print('2: Update Existing Patient')
            print('3: Delete Existing Patient')
            print('4: Fetch All Patients')
            print('5: Fetch Patient by Phone Number')
            print('6: Fetch Male Patients')
            print('7: Fetch Female Patients')
            print('8: Fetch Patients by Created On Date (Sort)')
            print('9: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                patient=Patient()
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 9:
                print('~~~~~~~~~~~~~~~~~~~~~~')
                print('Patient Menu Closed')
                print('~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('Enter Suitable Menu Option...')

    def show_consultation_menu(self):

        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Consultation Menu Opened')
        print('~~~~~~~~~~~~~~~~~~~~~~~~')

        while True:
            print('Consultation Menu: ')
            print('1: Add New Consultation')
            print('2: Update Existing Consultation')
            print('3: Delete Existing Consultation')
            print('4: Fetch All Consultation')
            print('5: Fetch Consultation of a Patient')
            print('6: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 6:
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Consultation Menu Opened')
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('Enter Suitable Menu Option...')