tup=(1, 3, 5, "dhruv", False)
print(tup[0:4])
print(type(tup), tup)      #it cant change

print(tup[0])
print(tup[-1])
print(tup[2])
# tup=[1, 3, 5]
# tup[0]=90
# print(type(tup), tup)
if "dhruv" in tup:
    print("Yes it is present")
    
if 5 in tup:
    print("Yes it is present")
    
if 434 in tup:
    print("Yes it is present")

tup2 = tup[1:4]
print(tup2)
