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