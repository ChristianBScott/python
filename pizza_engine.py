"""
Christian Scott
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS
PIZZA_TOPPINGS = ("Pepperoni", "Sausage", "Mushrooms", "Pineapple")
PIZZA_SIZE = ("Small", "Medium", "Large", "Extra Large")


# prints ticket from user input
def make_pizza(customer, size, topping, is_delivery):
    """Processes inbound data and local logic."""
    print(f"\n--- OFFICIAL TICKET: {customer.upper()} ---")
    print(f"{size} Pizza with {topping}.")
    print(f"Delivery: {is_delivery}")


# main function
def main():
    # user inputs information and selects pizza options
    user = input("Name: ").title()
    print(f"Options: {PIZZA_TOPPINGS}")  # Accessing Global Scope
    choice = input("Select topping: ")

    print(f"Options: {PIZZA_SIZE}")
    pizza_size = input("Select size: ")

    delivery = False
    try:
        bool(delivery) == input("Delivery?: True/False ")
    except ValueError:
        print("Invalid input. Defaulting to False.")
        delivery = False

    # Keyword Handoff
    make_pizza(customer=user, topping=choice, size=pizza_size, is_delivery=delivery)


main()
