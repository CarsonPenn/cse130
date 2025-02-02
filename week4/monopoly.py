# Lab 04: Monopoly
# Author: Carson Smith
# This program determines if a player can build a hotel on Pennsylvania Avenue.

def can_purchase_hotel():
    # Collect user inputs
    owns_all_properties = input("Do you own all the green properties? (y/n) ").strip().lower()
    pacific = int(input("What is on Pacific Avenue? (0-4 Houses, or 5 for a Hotel: "))
    north_carolina = int(input("What is on North Carolina Avenue? (0-4 Houses, or 5 for a Hotel: ) "))
    pennsylvania = int(input("What is on Pennsylvania Avenue? (0-4 Houses, or 5 for a Hotel: ) "))
    cash = int(input("How much cash do you have to spend?: "))
    houses_available = int(input("How many houses are there to purchase?: "))
    hotels_available = int(input("How many hotels are there to purchase?: "))


    # Constants
    HOTEL_COST = 100  
    HOUSE_COST = 50  
    REQUIRED_HOUSES = 4  

    # Decision Making
    if owns_all_properties != "y":
        print("Output: You do not own all the properties.")
        return
    
    if cash < HOTEL_COST:
        print("Output: Not enough cash.")
        return

    if hotels_available < 1:
        print("Output: No hotel available")
        return
# Already own a motel section.
    if pennsylvania == 5:
        print("Decision: You already have a Hotel")
        return

    if pacific == 5:
        print("Output: Swap the hotel on Pacific for the houses on Pennsylvania. ")
        return

    if north_carolina == 5:
        print("Output: Swap the hotel on North Carolina for the houses on Pennsylvania. ")
        return

    if pennsylvania < REQUIRED_HOUSES:
        print("Output: Not enough houses")
        return

    # Calculate cost based on available houses
    if houses_available >= 4:
        price = HOTEL_COST
        print(f"You meet all the criteria to purchase a hotel.\nThis will cost ${price}.\nPurchase 1 hotel.")
    elif houses_available >= 2:
        price = HOTEL_COST + (2 * HOUSE_COST)
        print(f"Out: Purchase B\nThis will cost ${price}.\nPurchase 1 hotel and 2 houses.")
    else:
        print("Out: No Houses")
        return

    print("Put 1 hotel on Pennsylvania and return any houses to the bank.")


# Run the program
if __name__ == "__main__":
    print(can_purchase_hotel())