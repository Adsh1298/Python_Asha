#Inheritance
class BaseClass:
    def base_func(self):
        print("Base class Function")

class DerivedClass(BaseClass):
    def derived_func(self):
        print("Derived class Function")

obj=DerivedClass()
obj.base_func()
obj.derived_func()
class Account:
 def __init__(self, holder, initialAmount):
     self.account_holder = holder
     self.balance = initialAmount
class SBAccount(Account):
    def __init__(self,name,amount):
        super().__init__(name,amount)
        print("SB Account created")
        print(self)

    def calc_interest(self):
        interest=self.balance*(6.5/100)*0.25
        self.balance+=interest
acc=SBAccount('asha',1000)
acc.calc_interest()
print(acc.balance)

