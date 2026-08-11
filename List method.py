l=[12,43,57,65,89,13,100]

l.append(45)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.index(43)
print(l)
print(l.count(12))

l.copy()
print(l)
l.insert(1,456)
print(l)
m=[900,1000,1100]
k=m+l
print(k)
l.extend(m)
print(l)