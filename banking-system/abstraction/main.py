from bank import Bank
from account import SavingsAccount, CheckingAccount
from person import Customer
from loan import Loan

if __name__ == '__main__':
    bank = Bank("00001", "BDO", "BDO Network Bank", "Pandi, Bulacan")

    person = Customer("1", "Michael Ponce", "09123456789", "Pandi, Bulacan")
    person2 = Customer("2", "Allyana Sarmiento", "09987654321", "Pandi, Bulacan")

    savings = SavingsAccount("01")
    checking = CheckingAccount("01")
    loan = Loan("0001", "Car Loan", "500000")

    person.openAccount(checking, bank)
    person.withdraw(100, checking)
    person.deposit(100, savings)

    balance = checking.get_accountBalance
    print(balance)