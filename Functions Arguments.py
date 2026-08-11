# _________________________________________Functions Arguments________________________________________________________
def average(a, b):           #in this case a, b are the reuired arguments
    print("The average is :",(a+b)/2)
    
average(4, 6)
average(5,6)

def average(a=2, b=4):           #by using default arguments
    print("The average is :",(a+b)/2)
    
average()

def average(a=2, b=4):           #in this case a=2 & b=4 are get ignored and avg(4,6) will display.
    print("The average is :",(a+b)/2)
    
average(4, 6)

def average(a=2, b=4):            
    print("The average is :",(a+b)/2)
    
average(9)                         #in this case I have given the 'a' value.

def average(a=2, b=4):            
    print("The average is :",(a+b)/2)
    
average(b=7)                          #in this case I have given the 'b=7' value.


def name(fname="Dhruv", sname="Sarang", lname="Hendre"):
    print("Hello",fname, sname, lname)
name()

def name(fname="Dhruv", sname="Sarang", lname="Hendre"):
    print("Hello",fname, sname, lname)
name("Aditya","Balu","Mohite")


def average(a=2, b=4):            
    print("The average is :",(a+b)/2)
    
average(b=7, a=56)

# def name(fname, sname, lname):
#     print("Hello",fname, sname, lname)   #This will give me the error because I didnt give the one 'value name' or 'value'
# name("Aditya","Mohite")

def name(fname, sname, lname):
    print("Hello",fname, sname, lname)
name("Aditya","Balu","Mohite")

def average(a, b, c=24):                 #the code is of required argument
    print("The average is :",(a+b-c)/2)
    
average(24,56)

#Variable length argument

# Finding average by using the function.

def average(*numbers):      #(the (*) tells Python:"Accept any number of arguments and store 
                            # them as a tuple.")
    sum=0
    for i in numbers:
        sum=sum+i
        print("The avg of the numbers is : ",sum/len(numbers))
average(23,34,23,56,6,78)

def name(**name):              #for dictionary we use double starr(**)
    # print(type(name))     >>>----->>>     Type =Dictionary
    print("Hello",name["fname"], name["sname"], name["lname"])   #Dictionary
name(fname=234,sname=567,lname=890)