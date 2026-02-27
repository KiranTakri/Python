class Book:
    def __init__(self,name,price,author):
        self.name=name
        self.price=price
        self.author=author
    def vender(self):
        print("Name of the book : ",self.name)
        print("Price of the book : ",self.price)
        print("Author of the book : ",self.author)
b=Book("2_State",100,"Chaitan Bhagat")
b.vender()
