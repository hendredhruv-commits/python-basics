import time
t= time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour=int(input("Enter the hour:"))
print(hour)
min = int(time.strftime('%M'))
min=int(input("Enter the min:"))
print(min)
sec = int(time.strftime('%S'))
sec = int(input("Enter the sec:"))
print(sec)
if(hour>=0 and hour<12):
    print("Good Morning Sir")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir")
else:
    if(hour>17 and hour<0):
        print("Good Evening")