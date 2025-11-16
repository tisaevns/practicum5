n = int(input())

if n % 10 == 1 and n != 11:
    print(n, "попугай")
elif n % 10 in (2, 3, 4) and not (12 <= n <= 14):
    print(n, "попугая")
else:
    print(n, "попугаев")
