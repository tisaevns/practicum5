pin = input()

if len(pin) != 4 or not pin.isdigit():
    print("ERROR")
else:
    if len(set(pin)) != 4:
        print("ERROR")
    else:
        year = int(pin)
        if 1900 <= year <= 2050:
            print("ERROR")
        else:
            print("OK")
