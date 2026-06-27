class ATM:
    def __init__(self, name , mobile, pin, balance):
        self.user_info = {
            "Name": name,
            "Mobile Number": mobile,
            "ATM PIN": pin,
            "Balance": balance,
            "Transaction History": []
        }
        self.remaining_attempts = 3

    def validate_pin(self):
        while self.remaining_attempts > 0:
            user_pin = input("Enter 4 digit PIN: ")
            if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
                print("Welcome to the ATM")
                return True
            else:
                self.remaining_attempts -= 1
                if self.remaining_attempts > 0:
                    print(f" Invalid PIN. Attempts left: {self.remaining_attempts}")
                else:
                    print(" Card blocked. Please contact customer service.")
                    return False

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        if amount >= 1000 and amount % 100 == 0:
            self.user_info["Balance"] += amount
            self.user_info["Transaction History"].append(f"Deposited: {amount}")
            print(" Amount deposited successfully")
        else:
            print(" Minimum deposit is 1000 and multiples of 100 only")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= self.user_info["Balance"] and amount % 100 == 0:
            self.user_info["Balance"] -= amount
            self.user_info["Transaction History"].append(f"Withdrawn: {amount}")
            print(" Please collect your cash")
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        print(f"💰 Current Balance: {self.user_info['Balance']}")

    def change_pin(self):
        old_pin = input("Enter old PIN: ")
        if old_pin == self.user_info["ATM PIN"]:
            new_pin = input("Enter new 4 digit PIN: ")
            if len(new_pin) == 4:
                self.user_info["ATM PIN"] = new_pin
                print("PIN changed successfully")
            else:
                print(" PIN must be 4 digits")
        else:
            print(" Incorrect old PIN")

    def transaction_history(self):
        if self.user_info["Transaction History"]:
            print(" Transaction History:")
            for txn in self.user_info["Transaction History"]:
                print(txn)
        else:
            print("No transactions found")

    def menu(self):
        while True:
            choice = int(input("\n1.Deposit \n2.Withdraw \n3.Check Balance \n4.Change PIN \n5.Transaction History \n6.Exit \nEnter choice: "))
            if choice == 1:
                self.deposit()
            elif choice == 2:
                self.withdraw()
            elif choice == 3:
                self.check_balance()
            elif choice == 4:
                self.change_pin()
            elif choice == 5:
                self.transaction_history()
            elif choice == 6:
                print("Thank you for using our ATM")
                break
            else:
                print("Invalid option")

#--------- MAIN PROGRAM ---------
print("💳 Please insert your ATM card")

atm = ATM(
    name="koushik_varma",
    mobile="",
    pin="6600",
    balance=47238
)

if atm.validate_pin():
    atm.menu()


