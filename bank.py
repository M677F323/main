""" balance = 0

def main():
    print("balance: ", balance)

if __name__ == "__main__":
    main() """

balance = 0
#here if we assgign it as  global thats the corner case then it will be assigned as zero

""" def main():
    deposit(100)
    withdraw(50)
    print("balance :" ,balance)

def deposit(n):
    global balance #This is for modifiying the global variable 
    #without this global varibale in local we cannt update the balanace which is  outside
    balance += n

def withdraw(n):
    global balance#This is for modifiying the global variable 
    #without this global varibale in local we cannt update the balanace which is  outside
    balance -= n

if __name__ == "__main__":
    main() """


#by using class

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self,n):
        self._balance += n
    def withdraw(self,n):
        self._balance -= n

def main():
        account = Account()
        account.deposit(100)
        account.withdraw(50)
        print("balance:", account.balance)

    
if __name__ == "__main__":
    main()

