for i in range(12):
    if(i==10):
        break
    print("5 X",i+1,"=", 5*(i+1))
    # break = Loop ko chodkar nikal jao
    # continue = Iteration ko chodkar nikal jao
for i in range(12):
    if(i==0):
        print("Skip the iteration")
        continue
    print("5 X",i+1,"=", 5*(i+1))
    
for i in range [2,4,5,6,8,0]:
    if(i%2!=0):
        print("I love you")
        continue
    print(i)