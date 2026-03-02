import AbstractionByModule
c=AbstractionByModule.SBI()
print(c.get_interest_rate())
print(c.receive())
d =AbstractionByModule.HDFC()
print(d.get_interest_rate())
print(d.receive())
#Second way to import
# from AbstractionByModule import SBI,HDFC
# sbi = SBI()
# print(sbi.get_interest_rate())
# print(sbi.receive())
# hdfc = HDFC()
# print(hdfc.get_interest_rate())
