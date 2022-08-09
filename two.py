l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
l_3 = []

for x in l_1:
    l_3.append(x)
    
for x in l_2:
    l_3.append(x)
    
l_3.sort()
print(l_3)
