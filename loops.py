"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# defines variable for while loop
destination = True
# Repeats question until user inputs yes
while destination:
    answer = input("Are we there yet? ")
    if answer == "yes":
        destination = False
print("Finally! That took forever!")

# range( start, stop, step)
# counts down in intervals of 1 and prints statement
for number in range(99, 0, -1):
    print(f"{number} bottles of beer on the wall!")
print("No more bottles of beer on the wall!")
