from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,id,name,initial_amount):
        self.account_no = id
        self.account_no = name
        self.balance = initial_amount
        @abstractmethod
        def calc_interest(self):
            pass

        class SBAccount(Account):
            def __init__(self,id,name,initial_amount):
                super().__init__(id,name,initial_amount)



