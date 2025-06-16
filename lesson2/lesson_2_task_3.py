import math 


def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area) 
    return area


side = float(input("Введите длину стороны квадрата: "))


result = square(side)


print(f"Площадь квадрата: {result}")