#include <ctime>
#include <iostream>
using namespace std;
class ATM {
private:
    int atmPin;
    int initialBalance;
    int currentBalance;

public:
    ATM() {
        atmPin = 12345;
        initialBalance = 60000;
        currentBalance = 20000;
    }

    void displayWelcome() {
        time_t now = time(0);
        char* dt = ctime(&now);
        cout << "\t\t\t\t-------------WELCOME TO ATM-------------------" << endl;
        cout << "" << endl;
        cout << "\t\t\t\t------------------------------" << endl;
        cout << "\n\t\t\tCurrent date:" << dt << endl;
        cout << "\t\t\t\t------------------------------" << endl;
        cout << "\n\t\t\t1. Press 1 and then press Enter to access your account via Pin Number" << endl;
        cout << "\n\t\t\tor" << endl;
        cout << "\n\t\t\tPress 0 and then press Enter to get help" << endl;
    }

    void enterPin() {
        int pin;
        cout << "Enter Your Acc Pin Access Number[Only one attempt is allowed]:";
        cin >> pin;
        if (pin == atmPin) {
            displayMenu();
        }
        else {
            cout << "You had made your attempt which failed!!! No More attempts allowed! Sorry !!" << endl;
        }
    }

void displayMenu() {
    int choice;
    do {
        cout << "\nATM Main Menu Screen" << endl;
        cout << "Enter [1] To Deposit Cash" << endl;
        cout << "Enter [2] To Withdraw cash" << endl;
        cout << "Enter [3] To Balance Inquiry" << endl;
        cout << "Enter [4] to Exit ATM" << endl;
        cout << "PLEASE ENTER A SELECTION AND PRESS RETURN KEY:" << endl;
        cin >> choice;

        switch (choice) {
        case 1:
            deposit();
            break;
        case 2:
            withdraw();
            break;
        case 3:
            checkBalance();
            break;
        case 4:
            cout << "Exiting..." << endl;
            break;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 4);
}


    void deposit() {
    	int amount;
    	cout<<"Present available balance:"<<currentBalance<<endl;
        cout << "Enter the amount to be deposited: ";
        cin >> amount;
        currentBalance += amount;
        cout << "Your new available Balanced Amount is Rs.: " << currentBalance << endl;
        cout<<"Thank You";
    }

   void withdraw() 
   {
    while (true) {
        int amount;
        cout << "\nEnter amount to withdraw: ";
        cin >> amount;
        if (amount > currentBalance) 
		{
            cout << "Insufficient balance." << endl;
            cout<<"Sorry !!";
        } 
		else 
		{
            currentBalance -= amount;
            cout << "Withdrawal successful. Current balance: " << currentBalance << endl;
            break;
        }
    }
}

    void checkBalance() {
    	cout << "Current balance: " << currentBalance << endl;
    }
};

int main() {
    ATM atm;
    atm.displayWelcome();
    atm.enterPin();

    return 0;
};



