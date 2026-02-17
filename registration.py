"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# Asks user for full name. Cannot be blank
print(
    "Thank you for taking the time to register! Please fill out the details below. :) "
)
first_name = input("Please enter your first name: ")
while first_name == "":  # loop to prevent blank answer
    print("ERROR: Name cannot be blank. ")
    first_name = input("Please enter your first name: ")

last_name = input("Please enter your last name: ")
while last_name == "":  # loop to prevent blank answer
    print("ERROR: cannot be blank. ")
    last_name = input("Please enter your last name: ")

# Validate chaperone status. Must be Y or N

chaperone = input("Parent volunteering to chaperone? (Y/N):  ").upper()
while chaperone != "Y" and chaperone != "N":  # loop to prevent invalid answer
    print("ERROR: Please enter only Y or N. Thank you: ")
    chaperone = input("Parent volunteering to chaperone? (Y/N):  ").upper()


phone_number = input("Please enter your phone number: ")
while phone_number == "":  # loop to prevent blank answer
    print("ERROR: Number cannot be blank. ")
    phone_number = input("Please enter your phone number: ")


tickets = 0
while True:
    try:
        tickets = int(input("How many tickets? "))
        if tickets > 0:
            break  # Ends loop when valid number entered
        print("ERROR: Must be at least 1 ticket.")
    except ValueError:
        print("ERROR: Please enter a number (e.g., 5, not 'five).")

print(f"Thank you for registering {first_name}!")
