t1=(2,4,3,5,7,6,8,9,1,12)

l1=list(t1)
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
t1=tuple(l2)
print(t1)
