def Customer(name,*item,discount=0.1):
        print("Name of the Product: ",name )
        print("Items: ",item)
        summ=sum(item)
        print("Total Amount: ",summ)
        print("Discount: 10%")
        print("Amount to be paid: ",summ-(summ*discount))
Customer("Rohit",100,200,300)