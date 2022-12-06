from math import sqrt


def count_distance(a, b):
    (Xa, Ya) = a
    (Xb, Yb) = b
    sum = sqrt((Xb - Xa)**2 + (Yb - Ya)**2)
    return sum


def distance(*args):
    distance = 0
    for points in range(len(args) - 1):
        new_distance = count_distance(args[points], args[points+1])
        distance += new_distance
    return distance


print(distance)
