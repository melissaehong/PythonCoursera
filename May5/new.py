
def computepay():
    enter_hours = float(input("Enter hours: "))
    rate_per_hour = float(input("Rate per hour: "))
    total = ''
    if enter_hours < 40:
        total = enter_hours*rate_per_hour
        return total
    else:
        total = (40*rate_per_hour) + (enter_hours-40)*(1.5*rate_per_hour)
        return total

print(computepay())
