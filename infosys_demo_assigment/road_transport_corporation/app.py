def cal(number_passengers, distance):
    price_fuel = 70
    price_ticket = 80
    mileage = 10
    profit = (price_ticket*number_passengers) - (price_fuel*(distance/mileage))
    if profit > 0:
        return profit
    else:
        return -1


number_passengers = 50
distance = 500
print(cal(number_passengers, distance))
