import sys


#account balance 
account_balance = float(500.25)


#<--------functions go here-------------------->
#defining printbalance function
def printbalance(account_balance):
    print("Your current balance : %.2f" % account_balance)

#defining deposit function
def deposit(account_balance):
    deposit_amount = float(input("How much would you like to deposit today?"))
    balance = account_balance + deposit_amount
    print("Deposit was $%.2f, current balance is $%.2f" %(deposit_amount,balance))

#defining withdraw function
def withdraw(account_balance):
    withdraw_amount = float(input("How much would you like to withdraw today?\n"))
    if(withdraw_amount > account_balance):
        print("$%.2f is greater than account balance $%.2f\n" %(withdraw_amount,account_balance))
    else:
        balance = account_balance - withdraw_amount
        print("Withdrawl amount was $%.2f, current balance is $%.2f" % (withdraw_amount, balance))

#if/else conditional statement  based on user input (deposit, withdraw or balance)
userchoice = input ("What would you like to do?\n")

if (userchoice == 'D'):
    deposit (account_balance)
elif userchoice == 'W':
        withdraw(account_balance)
elif userchoice == 'B':
        printbalance(account_balance)
else:
        print("Thank You for banking with us.\n")
        sys.exit()
