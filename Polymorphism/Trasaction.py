class payment:
    def pay(self):
        pass
class UPI(payment):
    def pay(self):
        print("Payment done through UPI")
class PhonePe(payment):
    def pay(self):
        print("Payment done through PhonePe")
class GooglePay(payment):
    def pay(self):
        print("Payment done through Google Pay")
c=[UPI(),PhonePe(),GooglePay()]
for i in c:
    i.pay()