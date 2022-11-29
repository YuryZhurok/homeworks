import random
list = random.sample(range(-100, 100), 10)
print(list)
list[2] = random.randint(-100, 100)
del list[6]
print(list)
