num1=float(input("Enter first number: "))       
num2=float(input("Enter second number: "))
calculator=input("Enter an operator (+, -, *, /): ")
match calculator:
    case "+":  
        result=num1+num2
        print(f"{num1} + {num2} = {result}")
    case "-":
        result=num1-num2
        print(f"{num1} - {num2} = {result}")
    case "*":
        result=num1*num2
        print(f"{num1} * {num2} = {result}")
    case "/":
        if num2!=0:
            result=num1/num2
            print(f"{num1} / {num2} = {result}") 
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator")