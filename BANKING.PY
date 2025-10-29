class Banking:
    def __init__(self, name, balance, pin, acno):
        self.name = name
        self.balance = balance
        self.__pin = pin
        self.acno = acno
        self.is_frozen = False
    
    def savingsaccount(self):
        return f"Account holder name is {self.name} and balance is {self.balance} - Savings Account"
    
    def currentaccount(self):
        return f"Account holder name is {self.name} and balance is {self.balance} - Current Account"
    
    def checkbalance(self, enteredpin):
        if enteredpin == self.__pin:
            return f"Your balance is {self.balance}"
        else:
            return "Wrong PIN"
    
    def freezeaccount(self, enteredpin):
        if enteredpin == self.__pin:
            self.is_frozen = True
            return "Your account has been frozen"
        else:
            return "Wrong PIN - Cannot freeze account"
    
    def unfreezeaccount(self, enteredpin):
        if enteredpin == self.__pin:
            self.is_frozen = False
            return "Your account has been unfrozen"
        else:
            return "Wrong PIN - Cannot unfreeze account"
    
    def deposit(self, amount):
        if self.is_frozen:
            return "Account is frozen - Cannot deposit"
        if amount <= 0:
            return "Deposit amount must be positive"
        self.balance = self.balance + amount
        return f"Your account is credited with {amount}. New balance: {self.balance}"
    
    def withdraw(self, amount, enteredpin):
        if enteredpin != self.__pin:
            return "Wrong PIN"
        if self.is_frozen:
            return "Account is frozen - Cannot withdraw"
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self.balance:
            return "Insufficient balance"
        
        self.balance = self.balance - amount
        return f"Your account is debited with {amount}. New balance: {self.balance}"

print("=== TESTING BANKING SYSTEM ===")

customer1 = Banking("SAITEJA NAYUDU", 5000000000, 1234, "HDFC001234")

print("\n1. Account Creation:")
print(customer1.savingsaccount())

print("\n2. Check Balance:")
print("With correct PIN:", customer1.checkbalance(1234))
print("With wrong PIN:", customer1.checkbalance(9999))

print("\n3. Deposit:")
print(customer1.deposit(10000000))

print("\n4. Withdraw:")
print("With correct PIN:", customer1.withdraw(100000, 1234))
print("With wrong PIN:", customer1.withdraw(100000, 9999))
print("Insufficient balance test:", customer1.withdraw(10000, 1234))

print("\n5. Freeze Account:")
print(customer1.freezeaccount(1234))
print("Try withdraw after freeze:", customer1.withdraw(500, 1234))
print("Try deposit after freeze:", customer1.deposit(1000))

print("\n6. Unfreeze Account:")
print(customer1.unfreezeaccount(1234))
print("After unfreeze - Deposit:", customer1.deposit(1000))
print("After unfreeze - Withdraw:", customer1.withdraw(500, 1234))

print("\n7. Final Balance:")
print(customer1.checkbalance(1234))