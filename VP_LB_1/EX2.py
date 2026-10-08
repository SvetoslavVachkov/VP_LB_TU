import math

r = float(input("Въведете радиус r: "))

area = math.pi * r * r
perimeter = 2 * math.pi * r

print(f"Лице на окръжността: {area:.3f}")
print(f"Периметър на окръжността: {perimeter:.20f}")