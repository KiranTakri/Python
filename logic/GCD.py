num1=int(input("Enter the first no "))
num2=int(input("Enter the second no "))
gcd=0
for i in range(1,num1+num2):
    if(num1%i==0 and num2%i==0 ):
        gcd=i
print(gcd)