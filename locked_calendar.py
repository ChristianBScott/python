"""
Christian Scott
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""

# Creates immutable list of months
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
# loop to print all months in list MONTHS
for m in MONTHS:
    print(f"{m}")

print("Attempting to add fake month")
# Program attempts to edit list MONTHS
try:
    MONTHS[0] = "Fune"
except TypeError:
    print("Error! Fake month cannot be added to constants")
# Tuples are locked and cannot be modified. Attempting to change them creates a TypeError
