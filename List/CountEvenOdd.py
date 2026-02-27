list=[2,5,4,3,7,6,8,9,1,0]
even_count=0
odd_count=0
for i in list:
    if i%2==0:
        even_count+=1
    else:   
        odd_count+=1
print("Count of even numbers:", even_count) 
print("Count of odd numbers:", odd_count)