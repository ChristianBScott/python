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

# creates list of responses for oracle
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
# prints intro to oracle
print("Welcome to the Digital Oracle!")
print("Type quit to exit")

exit = True
# while loop for user to ask yes or no questions
while exit:
    print("Ask any yes or no question and receive insight into the ethereal realm!")
    question = input("")
    # cleans users question and checks for "quit"
    quit_check = question.strip().lower()
    if "quit" in quit_check:
        break
    # prints a random option from RESPONSES list
    print(random.choice(RESPONSES))

print("Thank you for using the Digital Oracle")
