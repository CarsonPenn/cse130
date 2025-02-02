def can_place_hotel(own_green, pac, nc, pa, available_houses, available_hotels, cash_available):
    # Step 1: Check if the player owns all green properties.
    if not own_green:
        return "You must own all the green properties to build a hotel on Pennsylvania Avenue."

    # Step 2: Check if Pennsylvania already has a hotel
    if pa == 5:
        return "You already own a hotel on Pennsylvania Avenue."

    # Step 3: Check for hotel swap scenarios
    if nc == 5:
        return "Swap hotel from North Carolina Avenue for Pennsylvania Avenue."
    if pac == 5:
        return "Swap hotel from Pacific Avenue for Pennsylvania Avenue."

    # Step 4: Calculate houses needed
    needed_PA = max(0, 4 - pa)
    needed_NC = max(0, 4 - nc)
    needed_Pac = max(0, 4 - pac)
    total_houses_needed = needed_PA + needed_NC + needed_Pac
    total_hotels_needed = 1

    # Step 5: Check available houses and hotels
    if available_houses < total_houses_needed:
        return "Not enough houses available."
    if available_hotels < total_hotels_needed:
        return "Not enough hotels available."

    # Step 6: Check if the user has enough money
    house_cost = 200
    hotel_cost = 200
    total_cost = total_houses_needed * house_cost + total_hotels_needed * hotel_cost

    if cash_available < total_cost:
        return "Not enough cash to complete the build."

    # Success case
    return f"Hotel placed on Pennsylvania Avenue! Remaining cash: ${cash_available - total_cost}"


# Test Cases
test_cases = [
    ("1 Does not own enough", False, 0, 0, 0, 10, 10, 1000),
    ("2 Poor", True, 0, 0, 0, 15, 10, 100),
    ("3 No houses", True, 0, 0, 0, 10, 10, 9000),
    ("4 Swap with Pacific", True, 5, 4, 4, 0, 0, 0),
    ("5 Swap with NC", True, 4, 5, 4, 0, 0, 0),
    ("6 Already built", True, 4, 4, 5, 10, 10, 1000),
    ("7 All at once", True, 0, 0, 0, 12, 3, 3000),
    ("8 House and hotel", True, 3, 3, 3, 3, 1, 5000),
]

# Run Test Cases
for name, own_green, pac, nc, pa, houses, hotels, cash in test_cases:
    result = can_place_hotel(own_green, pac, nc, pa, houses, hotels, cash)
    print(f"{name}: {result}")
    print()
