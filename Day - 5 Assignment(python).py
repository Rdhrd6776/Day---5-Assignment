class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return "Account owner: Pavan \nAccount balance: 100"
    def deposit(self, dep_amt):
        #amount=float(input("Enter amount to be Deposited: "))
        #print("\n Amount Deposited:",amount)
        self.balance += dep_amt
        print("Deposit Accepted")
    def widthraw(self, wd_amt):
        try:
            if self.balance >= wd_amt:
                self.balance -= wd_amt
                print("Withdrwal accepted")
            else:
                print("Funds unavailable")
        except ValueError:
            print("valueerror for fund")



# 1. Instantiate the class

obj=Account(100)

# 2. Print the object

print(obj)


# 3. Show the account owner attribute

print(obj)

# 4. Show the account balance attribute

print("This account have balance amount :- ",obj.owner)


# 5. Make a series of deposits and withdrawals

obj.deposit(1000)



# 6. Make a withdrawal that exceeds the available balanced

obj.widthraw(100)

