list=[10,20,30,5,15]
max=list[0]
min=list[0]
for i in list:
    if max<i:
        max=i
    if min>i:
        min=i
print("The maximum is ",max)
print("The minimum is ",min)
