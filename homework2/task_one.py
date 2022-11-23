from math import sqrt
coordinate_x = float(input("Введите координату x: "))
coordinate_y = float(input("Введите координату y: "))
coordinate_x1 = float(input("Введите координату x1: "))
coordinate_y1 = float(input("Введите координату y1: "))
distance = sqrt(
    (coordinate_x1 - coordinate_x)**2 + (coordinate_y1 - coordinate_y)**2
    )
print(f"Расстояние между точками: {distance}")
