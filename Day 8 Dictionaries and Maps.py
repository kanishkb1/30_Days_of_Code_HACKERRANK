#Step-1: Setting data
n = int(input())
phone_book = {}
#Step-2: Input
for i in range(0,n):
    entry= str(input()).split()
    name=entry[0]
    phone=int(entry[1])
    phone_book[name] = phone
    
for j in range(0,n):
    name = str(input())

#Step-3: Set output
    if name in phone_book:
        phone = phone_book[name]
        print(name+"="+str(phone))
    else:
        print("Not found")
