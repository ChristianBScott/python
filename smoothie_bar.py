"""
Christian Scott

-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------


"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# Sets price for size of smoothie
def get_price(size):
    if size == "Small":
        return 1.00
    elif size == "Medium":
        return 1.50
    else:
        return 2.00


# Defines blend and prints user selections
def smoothie_blend(size, base, fruit, scoops):
    print("/n--- Smoothie Blend ---")
    print(f"Size: {size}")
    print(f"base: {base} with {fruit}")
    print(f"Scoops: {scoops}")


# Defines primary code base main()
def main():
    print("Welcome to our smoothie bar")
    # asks user to make smoothie selections
    choice_size = input("Size (Small/Medium/Large)").title().strip()
    choice_base = input("Select Base: ")
    choice_fruit = input("Select Fruit: ")
    try:
        choice_scoops = int(input("How many scoops? "))
    except ValueError:
        print("Invalid entry. Defaulting to 1.")
        choice_scoops = 1

    cost = get_price(choice_size)

    smoothie_blend(choice_size, choice_base, choice_fruit, choice_scoops)
    # prints cost
    print(f"Total Bill: ${cost:.2f}")


# runs program through main()
main()
