l1=[2,4,6,8,10]
l2=[1,3,5,7,9,2,4]
common_elements=[]

for i in l1:
    if i in l2:
        common_elements.append(i)
print("Common elements are:", common_elements)