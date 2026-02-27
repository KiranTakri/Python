balance=10000
def deposit(amount):
    global balance
    balance+=amount
    print("Balance after deposit: ",balance)
def withdraw(amount):
    global balance
    if amount>balance:
        print("Insufficient balance")
    else:
        balance-=amount
        print("Balance after withdrawal: ",balance)
deposit(5000)
withdraw(2000)