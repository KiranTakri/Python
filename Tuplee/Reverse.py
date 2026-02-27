t1=(2,4,3,5,7,6,8,9,1,12)
l1=list(t1)
i=0
j=len(l1)-1
while j>i:
    temp=l1[i]
    l1[i]=l1[j]
    l1[j]=temp
    i+=1
    j-=1
t1=tuple(l1)
print(t1)