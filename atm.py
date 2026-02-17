"""
Write atm.py and follow these requirements carefully:

Structure: Use match-case for the main menu.
Input Validation: Use .isdigit() or similar logic to prevent crashes if the user types text instead of numbers (since we are not using try-except yet).
Math Safety: No overdrafts (withdrawing more than you have) and no negative deposits.
Formatting: All currency must use :.2f.
"""

balance = float(1000.00)
exit = True


print(
    "Options: 1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit"
)  # lists all options for user

while exit:  # repeating loop to allow multiple uses
    choice = input("Please select an option: ")
    match choice:  # match case code to allow multiple choice
        case "1":  # prints current balance
            print(f"Current balance: ${balance:.2f}")
        case "2":  # deposits cash
            deposit = input("Please enter deposit amount: $")
            # prevents user from entering invalid inputs
            while deposit.isdigit() == False:
                deposit = input("Please enter a valid deposit amount: $")
            while float(deposit) < 0:
                print("ERROR: Number cannot be less than 0. ")
                deposit = input("Please enter deposit amount: $")

            balance = balance + float(deposit)  # calculates balance
        case "3":  # withdraws cash
            error = False

            while error == False:  # while loop to ensure valid answers
                withdrawal = input("Please enter withdrawal amount: $")
                if withdrawal.isdigit() == False:
                    print(
                        "Please enter a valid withdrawal amount. For example 5 instead of five."
                    )
                elif float(withdrawal) < 0:
                    print("Please enter a number greater than $0")
                elif float(withdrawal) > balance:
                    print("Withdrawal amount cannot be greater than current balance.")
                else:
                    error = True
            balance = balance - float(withdrawal)  # calculates balance
        case "4":
            error = False
            # while loop to prevents invalid answers
            while error == False:
                transfer = input("Please enter transfer amount: $")
                if transfer.isdigit() == False:
                    print(
                        "Please enter a valid transfer amount. For example 5 instead of five."
                    )
                elif float(transfer) < 0:
                    print("Please enter a valid number greater than $0")
                elif float(transfer) > balance:
                    print("Transfer amount cannot be greater than current balance.")
                else:
                    error = True
            balance = balance - float(transfer)  # calculates balance

        case "5":  # exits program
            print("Goodbye. Please have a nice day.")
            exit = False
        case _:  # catch all for when user inputs invalid match case answer
            print("That is not a valid number")
