import math

xc = float(input("xc: "))
yc = float(input("yc: "))
r = float(input("r: "))
x = float(input("x: "))
y = float(input("y: "))

distance = math.sqrt((x - xc)**2 + (y - yc)**2)

if distance < r:
    print("Точка внутри окружности.")
elif distance == r:
    print("Точка на окружности.")
else:
    print("Точка вне окружности.")
