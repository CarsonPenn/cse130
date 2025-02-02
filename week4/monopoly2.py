def main():
    # 
    own_green = input("Do you own all the green properties? (y/n): ").strip().lower()
    if own_green != 'y':
        print("You must own all the green properties to build a hotel on Pennsylvania Avenue.")
        return  

    # Step 2 PA?
    try:
        pa = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 5.")
        return
    if pa == 5:
        print("You already own a hotel on Pennsylvania Avenue.")
        return

    # Step 3 NC?
    try:
        nc = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 5.")
        return
    if nc == 5:
        print("You need to swap the hotel from North Carolina Avenue for Pennsylvania Avenue.")
        return

    # Step 4 PAC?
    try:
        pac = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 5.")
        return
    if pac == 5:
        print("You need to swap the hotel from Pacific Avenue for Pennsylvania Avenue.")
        return    
    # Step 5 Available houses 
    try:
        available_houses = int(input("How many houses are there to purchase? "))
    except ValueError:
        print("Invalid input for houses.")
        return

    # Step 6 Prompt for available houses
    try:
        available_hotels = int(input("How many hotels are there to purchase? "))
    except ValueError:
        print("Invalid input for hotels.")
        return

    # Step 7 User $$$
    try:
        cash_available = int(input("How much cash do you have to spend? "))
    except ValueError:
        print("Invalid input for cash.")
        return

    # Step 8: Calculate how many houses are needed on each property.
    # Received help from chatgpt on this section
    needed_PA = max(0, 4 - pa)
    needed_NC = max(0, 4 - nc)
    needed_PAC = max(0, 4 - pac)
    total_houses_needed = needed_PA + needed_NC + needed_PAC
    # Onle need one hotel
    total_hotels_needed = 1  

    # Print statements of which property(s) need houses.
    if total_houses_needed != 0:
        print("\nHouses needed to bring each property to four houses:")
    if needed_PA > 0:
        print(f"  Pennsylvania Avenue needs: {needed_PA} house(s)")
    if needed_NC > 0:
        print(f"  North Carolina Avenue needs: {needed_NC} house(s)")
    if needed_PAC > 0:
        print(f"  Pacific Avenue needs: {needed_PAC} house(s)")

    # Step 9 Comparaisns to see if there are enough hotels and houses
    if available_houses < total_houses_needed:
        print("There are not enough houses available to complete the build.")
        return
    if available_hotels < total_hotels_needed:
        print("There are not enough hotels available to complete the build.")
        return

    # Step 10 Display of how may houses and if a hotel is needed
    print(f"\nTotal houses needed: {total_houses_needed}")
    print(f"Total hotels needed: {total_hotels_needed}")

    # Step 11 calculate the cost and then print how much will be needed
    house_cost = 50
    hotel_cost = 100
    total_cost = total_houses_needed * house_cost + total_hotels_needed * hotel_cost
    print(f"\nTotal cost to build: ${total_cost}")

    # Step 12 check if user's cash is enough to buy the houses and hotel
    if cash_available <= total_cost:
        print("You do not have enough cash to complete the build.")
        return
    remaining_cash = cash_available - total_cost
    print("\nPurchase successful!")
    print(f"Bought {total_houses_needed} house(s) and {total_hotels_needed} hotel.")
    print(f"Remaining cash: ${remaining_cash}")

#  :)
if __name__ == "__main__":
    main()
