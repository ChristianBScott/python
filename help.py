# Store the menu data
menu_dict = {}

while True:
    category = input("Enter a category (or 'quit' to stop): ")
    if category.lower() == "quit":
        break

    items_str = input(f"Enter {category} items separated by commas: ")

    # Convert string to list and store in dictionary
    items_list = [item.strip() for item in items_str.split(",")]
    menu_dict[category] = items_list

# Setup a clean file with 'w' write mode once the loop finishes
with open("menu.txt", "w") as file:
    # Loop through the dictionary and write each section
    for category_name, items in menu_dict.items():
        file.write(f"--- {category_name.upper()} ---\n")

        # Loop through the item list
        for food in items:
            file.write(f" - {food}\n")

        # Add a blank line between categories
        file.write("\n")
