bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}

'''
Name: print_welcome
Task: Prints a welcome message to the user.
Input: None
Side Effects : Welcome Message
Return: None
'''
def print_welcome():
    print("Welcome to Berklee Bank!)")


'''
Name: get_username
Task: Prompts the user for their name.
Input: None
Side Effects: Prompts "What is your name?"
Return: Return the username 
'''
def get_username():
    name = input("What is your name?")
    return name
'''


Name: check_pin
Task: Prompts the user for the pin
Input: None
Side Effects: Prompts "What is your pin?"
Return: Return the pin
'''
def get_pin():
    pin = input("What is your pin?")
    return pin


'''
Name: verify_identity
Task: Take the name and pin and see if there's a valid user in the system. If so, get their data. IF not, fail.
Inpu: username and pin
Side Effects: If they don't exist, it says"Access Denied"
Return: True if user exists, False if not
'''
def verify_identity(username, pin):
    if bank_dict.get(username): 
        user_values = bank_dict.get(username)
        if pin == user_values.get("pin"):
            return True
        print("Access Denied for ", username, "with pin", pin)
        return False

'''
Name: check_balance
Task: print the user's balance
Input: None
Side Effects: Prints the user's balance
Return: None
'''
def get_balance(username):
    if bank_dict.get(username):
        users_values = bank_dict.get("balance")
        print("Your Balance is: ", balance)

    Return None

'''
Name: withdraw
Task: Ask the user how much they want to withdraw. If they have enough, reduce balance, If not, Tell them.
Input: username 
Side Effects: Prompts user for input and print the new balance
Return: None
'''
def withdraw_money(username):
    withdraw_amount = int(input("How much would you like to withdraw? "))
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        previous_bal = users_values.get ("balance")
        new_bal = previoius_bal - withdraw_amount
        if new_bal < 0:
            print("Insufficient funds...")
        else:
            users_values.update({"balance": new_bal})
    
'''
Name: depodepsit_money
Task: Ask user how much they want to deposit then add that tp the balance
Input: username
Side Effect: Prompts user for the input and print the new balance
Return: None
'''
def deposit_money(username):
    deposit_amount = int(input("How much would you like to deposit? "))
    if bank_dict.get(username):
        user_values = bank_dict.get(username)
        previous_bal = users_values.get("balance"
        new_bal = previous_bal + deposit_money
        users_values.update({"balance": newbal})

    return None
'''
Name: get_menu_choice
Task: Print the functionality of the bank (the commands they can do) to the terminal
Input: None
Side Effects: Do you wanna deposit, withdraew, get balance, quit (they type the command)
Return: the string the user typed in
'''
def get_menu_choice():
    input("Do you want to deposit, withdraw, get balance or quit?")
    return choice
'''
Name: quit
Task: Logs the user out of the system
Input: None
Side Effects: Prints a goodbye message
'''

def run_tes():
    withdraw("Priya")
    withdraw("Priya")
    deposit("Priya")
    check_balance("Priya") #Print $100
    verify_identity("Priya", "4821") #Success
    verify_identity("Priya", "0000") #Fail
    print_welcome()#expecting print welcome 
    check_pin() #Expecting to prompt for pin

def main():
    print_welcome()
    name = get_username()
    pin = get_pin()
    valid = verify_identity(name, pin)
    if not valid:
        print("Access Denied")
        return
    while True:
        choice = get_menu_choice()
        if users_choice == "balance":
            get_balance(name)

        elif users_choice == "withdraw":
            withdrawe_money(name)

        elif users_choice == "deposit":
            deposit_money(name)
        
        elif users_choice == "quit":
            break

        else:
            print("You can't choose that...")
