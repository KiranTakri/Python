list=[4,3,2,1,5,6]
i=0
j=len(list)-1
while i<j:
    temp=list[i]
    list[i]=list[j]
    list[j]=temp
    i+=1
    j-=1
print("Reversed list is:",list)