# WE DEVELOP A LOGIC AND SEPERATE OUT WITH THE FUNCTION.
a1=9
b1=7
geometric_mean=(a1*b1)/(a1+b1)
print("geometric_mean : ",geometric_mean)
c1=4
d1=6
geometric_mean2=(c1*d1)/(c1+d1)
print("geometric_mean2 : ",geometric_mean2)

def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
    
a=9
b=7
calculateGmean(a,b)
c=4
d=6
calculateGmean(a,b)

q=34
w=23
if(q>w):
    print("q is greater")
else:
    print("w is greater no. or equal to q")
    
z=12
x=45
if(z>x):
    print("First number is greater")
else:
    print("x is greater no. or equal to z")
    
def isGreater(q, w):
    q=34
    w=23
    if(q>w):
        print("First no. is greater than second")
    else:
        print("Second no. is greater than first")
z=12
x=45
isGreater(z, x)