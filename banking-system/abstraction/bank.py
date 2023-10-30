from abc import ABC, abstractmethod

class Interfacebank(ABC):
    @property
    @abstractmethod
    def get_id(self):
        pass

    @property
    @abstractmethod
    def get_code(self):
        pass

    @property
    @abstractmethod
    def get_name(self):
        pass

    @property
    @abstractmethod
    def get_location(self):
        pass

    @property
    @abstractmethod
    def get_list_of_customers(self):
        pass


class AbstractBank(Interfacebank):
    def __init__(self, id:str, code:str, name:str, location:str):
        self.__id = id
        self.__code = code
        self.__name = name
        self.__location = location
        self.__list_of_customers = []

    @property
    def get_id(self):
        return self.__id
    
    @property
    def get_code(self):
        return self.__code
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_location(self):
        return self.__location
    
    @property
    def get_list_of_customers(self):
        return self.__list_of_customers        

class Bank(AbstractBank):
    def __init__(self, id, code, name, location):
        super().__init__(id, code, name, location)
