"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Asks user to input 2 numbers
print("Please Enter 2 numbers of your choice.")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

if num1 > 0 and num2 > 0:
    print("Both numbers are bigger than 0. Fantastic!")
if num1 > 100 and num2 > 100:
    print("Both numbers are bigger than 100. Wow!")
if num1 < 100 or num2 < 100:
    print("At least 1 number is less than 100. Superb!")
if num1 % 2 == 0 or num2 % 2 == 0:
    print("At least 1 number is even. Awesome!")
if num1 == num2:
    print("Both numbers are the same. Incredible!")
if not (num1 == 0 and num2 == 0):
    print("At least 1 number is not 0. Phenomenal!")

if num1 > 0:
    print("The first number is positive. Spectacular!")
elif num1 < 0:
    print("The first number is negative. Outstanding!")
else:
    print("The first number is 0. Remarkable!")
