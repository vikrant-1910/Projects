import datetime

class ATM:
    def __init__(self):
        self.atm_pin = 12345
        self.initial_balance = 60000
        self.current_balance = 20000

    def display_welcome(self):
        now = datetime.datetime.now()
        print("\t\t\t\t-------------WELCOME TO ATM-------------------")
        print("\n\t\t\tCurrent date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
        print("\n\t\t\t1. Press 1 to access your account via PIN number")
        print("\n\t\t\tor")
        print("\n\t\t\tPress 0 to get help")

    def enter_pin(self):
        pin = int(input("Enter Your Acc PIN Access Number [Only one attempt is allowed]: "))
        if pin == self.atm_pin:
            self.display_menu()
        else:
            print("You had made your attempt which failed!!! No More attempts allowed! Sorry !!")

    def display_menu(self):
        while True:
            print("\nATM Main Menu Screen")
            print("Enter [1] To Deposit Cash")
            print("Enter [2] To Withdraw cash")
            print("Enter [3] To Balance Inquiry")
            print("Enter [4] to Exit ATM")
            choice = int(input("PLEASE ENTER A SELECTION AND PRESS RETURN KEY: "))

            if choice == 1:
                self.deposit()
            elif choice == 2:
                self.withdraw()
            elif choice == 3:
                self.check_balance()
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def deposit(self):
        amount = int(input(f"Present available balance: {self.current_balance}\nEnter the amount to be deposited: "))
        self.current_balance += amount
        print(f"Your new available Balanced Amount is Rs.: {self.current_balance}\nThank You")

    def withdraw(self):
        while True:
            amount = int(input(f"Present available balance: {self.current_balance}\nEnter amount to withdraw: "))
            if amount > self.current_balance:
                print("Insufficient balance. Sorry !!")
            else:
                self.current_balance -= amount
                print(f"Withdrawal successful. Current balance: {self.current_balance}")
                break

    def check_balance(self):
        print(f"Current balance: {self.current_balance}")

if __name__ == "__main__":
    atm = ATM()
    atm.display_welcome()
    atm.enter_pin()
