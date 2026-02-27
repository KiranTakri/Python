list=[]
for i in range(5):
    n=int(input("Enter the number"))
    list.append(n)
print("The list is ",list)
def LargestNo(list):
    max=list[0]
    for i in list:
        if max<i:
            max=i
    return max
LargestNo(list)
def SecondLargestNo(list):
    max=LargestNo(list)
    second_max=list[0]
    for i in list:
        if i<max and i>second_max:
            second_max=i
    return second_max
print("The second largest number is ",SecondLargestNo(list))