alist = [1,11,14,5,8,9]
new_list = []
for x in alist:
    if x < 10:
        new_list.append(x)
print(new_list)

# do this with comprehension too
        
comp_list = [x for x in alist if x < 10]
print(comp_list)