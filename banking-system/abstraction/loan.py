from abc import ABC, abstractmethod

class AbstractLoan(ABC):
    def __init__(self, id:str, name:str, amount:int) -> None:
        self.__id = id
        self.__name = name
        self.__amount = amount
        self.__accountHolders = []
    
    @abstractmethod
    def get_name(self):
        pass
    

class Loan(AbstractLoan):
    def __init__(self, id: str, name: str, amount: int) -> None:
        super().__init__(id, name, amount)

    def get_name(self):
        return self.__name