from abc import ABC, abstractmethod

class InterfacePerson(ABC):
    @property
    @abstractmethod
    def get_id(self):
        pass

    @property
    @abstractmethod
    def get_name(self):
        pass
    
    @property
    @abstractmethod
    def get_contact(self):
        pass

    @abstractmethod
    def set_contact(self, contact):
        pass

    @property
    @abstractmethod
    def get_address(self):
        pass

    @abstractmethod
    def set_address(self, address):
        pass

    @abstractmethod
    def openAccount(self, account):
        pass

    @abstractmethod
    def openLoan(self, bank):
        pass

    @abstractmethod
    def enrollHolder(self, customer, bank):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class AbstractPerson(InterfacePerson):
    def __init__(self, id:str, name:str, contact:str, address:str) -> None:
        self.__id = id
        self.__name = name
        self.__contact = contact
        self.__address = address
    
    @property
    def get_id(self):
        return self.__id
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_contact(self):
        return self.__contact
    
    @get_contact.setter
    def set_contact(self, contact):
        self.__contact = contact

    @property
    def get_address(self):
        return self.__address
    
    @get_address.setter
    def set_address(self, address):
        self.__address = address

class Customer(AbstractPerson):
    def __init__(self, id:str, name:str, contact:str, address:str) -> None:
        super().__init__(id, name, contact, address)
        self.__list_of_accounts = []

    def openAccount(self, account, bank):
        self.__list_of_accounts.append(account.get_accountType)
        account.get_accountHolders.append(self.get_name)
        bank.get_list_of_customers.append(self.get_name)

    def openLoan(self, loan, bank):
        if not self.get_name in bank.get_list_of_customers:
            print("Can't open a loan!")
        else:
            print("Loan Accepted!")
            self.__list_of_accounts.append(loan.get_name)

    def enrollHolder(self, account, customer, bank):
        self.__list_of_accounts.append(account)
        account.get_accountHolders.append(customer.get_name)
        bank.get_list_of_customers.append(self.get_name)
        
    def deposit(self, amount, account):
        account.set_accountBalance = account.get_accountBalance + amount

    def withdraw(self, amount, account):
        if account.get_accountType == "Savings Account":
            if account.get_accountBalance < amount:
                print("Insufficient Balance!")
            else:
                account.set_accountBalance = account.get_accountBalance - amount
        else:
            print(f"Withdraw amount of {amount}")
            account.set_accountBalance = account.get_accountBalance - amount