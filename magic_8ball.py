"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------

Christian Scott
"""

import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Probably",
    "Probably not",
    "Definitely",
    "Not Happening",
)

print("Welcome to the Digital Oracle!")
print("Type quit to exit")

exit = True
while exit:
    print("Ask any yes or no question and receive insight into the ethereal realm!")
    question = input("")
    quit_check = question.strip().lower()
    if "quit" in quit_check:
        break
    print(random.choice(RESPONSES))

print("Thank you for using the Digital Oracle")
# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop
