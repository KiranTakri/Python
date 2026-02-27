data=input("Enter a color name (Red, Green, Blue, Yellow, Black): ")
match data:
    case "Red" |"1"|"2"|"3":
        print("You have selected Red color")
    case "Green" |"4"|"5"|"6":
        print("You have selected Green color")
    case "Blue" |"7"|"8"|"9":
        print("You have selected Blue color")   
    case "Yellow" |"10"|"11"|"12":
        print("You have selected Yellow color")
    case "Black" |"13"|"14"|"15":
        print("You have selected Black color")
    case _:
        print("Invalid color")
