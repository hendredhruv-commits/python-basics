
import os #import os in Python imports the built-in os module, which lets your program 
          #interact with the operating system. It provides functions for working with files, folders,
          # environment variables, and system commands.
          
print("Hello world from...")
os.system("python --version")

x=4
# x is the variable to match :
match x:
    #if xi 0
    case 0:
        print("x is zero")
        # Case with if condition
    case 2:
        print("x%2==0 and case is 2")
        # empty Case with if-condition
case  if x<10:
            print("x is <10 ")
        # default case(will only be matchesd if the above cases were not matched)
        # so it is basically just an else:
        case_:
print(x)   
        