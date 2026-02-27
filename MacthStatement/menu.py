Choice=input("Enter your choice menu (Please choose between Tea, Coffee, Juice, Snacks): ")
match Choice:
    case "Tea":
        print("You have selected Tea")
    case "Coffee":
        print("You have selected Coffee")
    case "Juice":
        print("You have selected Juice")    
    case "Snacks":
        print("You have selected Snacks")
    case _:
        print("Invalid choice")