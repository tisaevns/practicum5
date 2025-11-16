year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("366 дней")
else:
    print("365 дней")
