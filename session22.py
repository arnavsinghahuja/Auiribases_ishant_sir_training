'''quote="be exceptional "#interview queation
print("----",quote)
new_quote=quote.upper()
print("----",new_quote)

#quote.lower()
print("capatalized",quote.capitalize())
print("titial case",quote.title())
print("swap case",quote.swapcase())


'''
#2 of day
password="pasword123"
new_passwprd=password.strip()
print('password:',password)
print("new_password",new_passwprd)
data="000013130012410000"
print('data',data.strip('0'))
print('data',data.lstrip('0'))
print('data',data.rstrip('0'))
name = "john watson"
new_name = ""

for index in range(len(name)):
    if index % 2 == 0:
        new_name += name[index]
    else:
        new_name += "*"

print(new_name)  


