"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

seats = list(range(1, 21))  # Creates list of seats 0-20

while quit:  # looping prompt that asks user to pick seats
    print(f"Available seats: {seats}")
    choice = int(input("Which seat would you like? "))

    #   adds two break conditions to end loop
    if choice == 0:
        break
    if len(seats) == 1:
        print("All seats have been taken!")
        break

    # removes chosen seats from list and informs user if seat is invalid
    if choice in seats:
        seats.remove(choice)
    else:
        print("Sorry! That seat is taken or doesn't exist")
        print("Please choose a different seat or type 0 to exit.")


print("Thank you! Please come again!")
