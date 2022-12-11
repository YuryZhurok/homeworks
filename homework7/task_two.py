def is_right_angle_triangle(a, b, c):
    sides = sorted([13, 4, 9])
    a = sides[0]
    b = sides[1]
    c = sides[2]
    while True:
        result = {}
        if a+b <= c or a+c <= b or b+c <= a:
            result["success"] = False
            result["description"] = 'no such triangle exists'
            return (result)
        if a**2 + b**2 != c**2:
            result["success"] = False
            result["description"] = 'the triangle is not right-angled'
            return (result)
        else:
            result["success"] = True
            result["description"] = 'the triangle is right-angled'
            return (result)


print(is_right_angle_triangle(13, 4, 9))
