from datetime import date , time, datetime

today = date.today()
now = datetime.now()
dateyear = today.year
print("Today's date:", today)
print("\nCurrent date and time:", now)
print("\nCurrent year:", dateyear)

print("\nDate components: ", today.day, today.month, today.year, today.decade)