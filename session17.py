#1-A
#empty data structure
#empty tuple
#my_tuple=()
my_tuple=tuple()

print("mylist",)


#2-A
#explore dictionary data structure
#in dictionary keys are either number
#value can be any data
'''In Dictionary keys are either number( int) or text(string)
value can be any data
Dictionary --
Keys cannot be duplicated. They are unique
—> But value can be duplicated'''

my_data={
   101:'john',
   201:'jennie',
202:'jenn',
203:'jennya',
204:'jennko',
205:'jenna',

}
print('my_data----',)
#list of month
monthlist=[
    'jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec'
]
college_attendence={}.fromkeys(monthlist,100)
print("college_attendence")
print(college_attendence)

college_attendence["jan"] -= 5

print ("college_attendence")
print (college_attendence)