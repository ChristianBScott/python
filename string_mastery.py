"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: [Christian Scott]
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR 🎸 ---
instrument = "Acoustic Guitar"
# Prints the length of 'instrument'
length = len(instrument)
print(f"Instrument Length: {length}")
# Prints the first and last letter of 'instrument'
first_letter = instrument[0]
last_letter = instrument[-1]
print(f"First Letter : {first_letter} Last Letter : {last_letter}")
# Uses min() and max() to find and print the lowest and highest ASCII characters
min_letter = min(instrument)
print(f"Lowest ASCII character: {min_letter} ")
print("Note: the lowest ASCII character is an invisible space")
max_letter = max(instrument)
print(f"Highest ASCII character: {max_letter}")

# --- TASK 2: THE CLEANUP CREW 🧵 ---
messy_input = "   vOLUME_knob_11   "
# takes messy input and cleans by removing spaces, capitalizing, and swapping _ with spaces
clean_input = messy_input.strip().upper().replace("_", " ")
print(f"\nold messy input: {messy_input}")
print(f"beautified input: {clean_input}")


# --- TASK 3: THE VALIDATOR 🔍 ---
serial_number = "90210"
print(f"\nserial number: {serial_number}")
# checks if serial number is number and prints appropriate response
if serial_number.isdigit() == True:
    print("Valid Serial")
else:
    print("Invalid Serial")


# --- TASK 4: THE DUCK BRIDGE 🦆🎵 ---
# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list
name_string = "DUCKY"
# converts all letters in DUCKY into a list
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")
# a for loop to go through all letters in Ducky
for char in name_string:
    current_name = " ".join(duck_letters)
    print("There was a teacher who had a duck and Ducky was his Name-o")
    print(f"({current_name}) \n" * 3)
    print("and Ducky was his Name-o!\n")
    # changes current letter in list to duck emoji
    duck_letters[count] = "🦆"
    count += 1

# final version with all duck emojis
final_name = " ".join(duck_letters)
print(f"({final_name}) \n" * 3)
print("and Ducky was his Name-o!\n")
