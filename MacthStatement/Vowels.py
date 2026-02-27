alpha=input("Enter a single alphabet: ")
match alpha:
    case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
        print(f"{alpha} is a vowel")
    case _:
        print(f"{alpha} is not a vowel")