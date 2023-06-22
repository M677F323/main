""" balance = 0

def main():
    print("balance: ", balance)

if __name__ == "__main__":
    main() """

balance = 0

def main():
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
    main()