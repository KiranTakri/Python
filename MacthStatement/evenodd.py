num=int(input("Enter a number: "))
match num % 2:
    case 0: 
        print(f"{num} is even.")
    case 1:
        print(f"{num} is odd.")
    