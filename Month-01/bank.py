from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

account = {"owner": "Hamam", "balance": 1000.0, "transactions": []}
def deposit(account):
    
    amount =  get_amount("Enter the amount you want to deposit: ")
    account["balance"] += amount
    print(f"Your current balance is: {account["balance"]:.2f}\n")
    print("Added successfully")
    account["transactions"].append({
        "type": "Deposit",  
        "amount": amount,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })

    return 
        

def withraw(account):
    
    amount =  get_amount("How much do you want to withdraw? ")
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"The amount was withdrawn successfully.{amount:.2f}")
        print(f"Your current balance is: {account["balance"]:.2f}")
        account["transactions"].append({
            "type": "Withdraw",  # أو  أو Transfer to {user}
            "amount": amount,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

        return 
    else:
        print("Sorry, your balance is less than this amount.")
        
def cheak_balance(account):
    print(f"Your balance is: {account["balance"]:.2f}")

def transfer(account):
    
    while True:
        user = input("Name of the person you want to transfer the money to: ").strip()
        if user.replace(" ", "").isalpha() and len(user) >= 3:
            break
        else:
            print("❌ Invalid name! Please use letters only (at least 2 characters)\n")
            
    tron = get_amount("How much do you want to transfer? ")
    
    if tron <= account["balance"]:
        account["balance"] -= tron
        print(f"The transfer was successful to: {user}\nand the transfer amount was: {tron:.2f}")
        print(f"Your current balance is: {account["balance"]:.2f}")
        account["transactions"].append({
            "type": "Transfer",  
            "amount": tron,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
    else:
        print("Sorry, your balance is insufficient.")

def show_transactions(account):
    if not account["transactions"]:
        print("No transactions yet.")
        return

    print("--- Transaction History ---")
    for t in account["transactions"]:
        print(f"[{t['time']}] {t['type']}: {t['amount']:.2f}")

def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            else:
                print("Please enter an amount greater than 0.")
        except ValueError:
            print("Please enter a number")
            print("*******************\n")


def main():
    while True:
        print("1.deposit\n2.withraw\n3.cheak balance\n4.Transfer money\n5.Transaction History\n6.Exit")
        choose = input("Choose a number: ").strip()
        if choose == "6":
            print("I hope you enjoyed this experience")
            print("\n****** THANK YOU ******")
            break
        else:
            if choose == "1":
                deposit(account)
            elif choose == "2":
                withraw(account)
            elif choose == "3":
                cheak_balance(account)
            elif choose == "4":
                transfer(account)
            elif choose == "5":
                show_transactions(account)
            else:
                print("Please choose a number from the list in front of you\n")
        print("*****************************\n")
main()
