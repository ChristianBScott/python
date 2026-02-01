"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# asks user for income and multiple monthly expenses
income = float(input("Please enter your monthly income: $"))
rent = float(input("Please enter your monthly rent: $"))
utilities = float(input("Please enter your monthly utility bill: $"))
groceries = float(input("Please enter your monthly groceries bill: $"))
gas = float(input("Please enter your monthly gas: $"))
healthcare = float(input("Please enter your monthly healthcare bill: $"))

# adds all monthly expenses and determines remaining balance
expenses = rent + utilities + groceries + gas + healthcare
balance = income - expenses

# calculates percent of income spent
income_spent = expenses / income

# prints remaining balance and percent of income spent
print(f"Remaining Balance:         ${balance:,.2f}")
print(f"Percent Income Spent:      {income_spent:,.2%}")
