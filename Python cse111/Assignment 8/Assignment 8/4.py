class Account:
    def __init__(self,balance):
        self._balance = balance
    def getBalance(self):
        return self._balance

class CheckingAccount(Account):
    numberOfAccount = str(0)
    def __init__(self,a=0.0):
        self._balance = str(a)
        CheckingAccount.numberOfAccount=str(int(CheckingAccount.numberOfAccount)+1)
    def __str__ (self):
        return 'Account Balance: '+self._balance






print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)
