"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Assignment Name, Date, File Name).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# gets info from user for Fantasy Creature
print("Fantasy Creature Creator")
name = input("Please enter your name: ")
animal = input("What fantasy creature are you?:")
gender = input("What gender are you?: ")
color = input("What color are you?:")
size = input("What size are you?:")

# Print Creature Description
print(f"\n\nYou have made a very {size} {color} {gender} {animal} named {name}")

# Prints beginning of adventure for your fantasy creature
print(f"\n\nYou are a {gender} {animal} standing on a hill")
print(f"You're very {color} and somewhat {size}")
print(f"It's time for {name} the {animal} to go out and explore!")
print(f"\nCongratulations!")
