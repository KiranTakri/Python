l=[1,2,3,4,5]
l2=[]
for i in l:
    if i%2==0:
        l2.append("even")
    else:
        l2.append("odd")
print(l2)
l3=["even" if i%2==0 else "odd" for i in l]
print(l3)