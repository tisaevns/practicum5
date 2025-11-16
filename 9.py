a, b, c = map(float, input().split())

if a >= b and a >= c:
    if b >= c:
        print(round(a), round(b), round(c))
    else:
        print(round(a), round(c), round(b))
elif b >= a and b >= c:
    if a >= c:
        print(round(b), round(a), round(c))
    else:
        print(round(b), round(c), round(a))
else:
    if a >= b:
        print(round(c), round(a), round(b))
    else:
        print(round(c), round(b), round(a))
