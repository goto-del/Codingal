def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost
spending_money = 600
def trip_cost(city, days):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


print("Cost of the car rental is: ", rental_car_cost(5))

print("Cost of plane ride is: ", plane_ride_cost("Charlotte"))

print("Cost of the hotel is: ", hotel_cost(2))

print("Total cost of the trip is: ", trip_cost("Los Angeles", 7))

print(trip_cost("Charlotte", 2))