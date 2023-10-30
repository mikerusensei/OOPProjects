from abc import ABC, abstractmethod

class InterfaceAccount(ABC):
    @property
    @abstractmethod
    def get_id(self):
        pass

    @property
    @abstractmethod
    def get_accountType(self):
        pass

    @property
    @abstractmethod
    def get_accountHolders(self):
        pass

    @property
    @abstractmethod
    def get_accountBalance(self):
        pass

class AbstractAccount(InterfaceAccount):
    def __init__(self, id, accountType) -> None:
        self.__id = id
        self.__accountType = accountType
        self.__account_holders = []
        self.__account_balance = 0

    @property
    def get_id(self):
        return self.__id
    
    @property
    def get_accountType(self):
        return self.__accountType
    
    @property
    def get_accountHolders(self):
        return self.__account_holders
    
    @property
    def get_accountBalance(self):
        return self.__account_balance
    
    @get_accountBalance.setter
    def set_accountBalance(self, balance):
        self.__account_balance = balance

class SavingsAccount(AbstractAccount):
    def __init__(self, id) -> None:
        super().__init__(id, "Savings Account")

class CheckingAccount(AbstractAccount):
    def __init__(self, id) -> None:
        super().__init__(id, "Checking Account")
        