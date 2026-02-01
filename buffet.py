"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

# Asks user for age
age = int(input("Please enter your age: "))

# Uses if/else statements to determine price for buffet and prints statement

if age < 1:
    price = float(0)
    print(f"Free!         ${price:,.2f}")
elif age <= 11:
    price = float(age)
    print(f"You're total is ${age:,.2f} (Child Discount)")
elif age <= 64:
    price = float(16.95)
    print(f"You're total is ${price:,.2f} (Standard Adult)")
else:
    price = float(12.95)
    print(f"You're total is ${price:.2f} (Senior Discount)   ")
