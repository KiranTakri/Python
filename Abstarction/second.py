from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass
    def receive(self):
        print("Payment received.")
class SBI(Bank):
    def get_interest_rate(self):
        return 7.5
class HDFC(Bank):
    def get_interest_rate(self):
        return 8.0
sbi = SBI()
sbi.get_interest_rate()
print(sbi.get_interest_rate())
sbi.receive()
hdfc = HDFC()
print(hdfc.get_interest_rate())
hdfc.receive()
