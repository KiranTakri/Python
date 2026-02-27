num=int(input("Enter a number: "))
num1=0
for i in range(2,num+1):
    if num%i==0:
        num1=num1+1
if num1==1:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")