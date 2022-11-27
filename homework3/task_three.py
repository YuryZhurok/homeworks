import random
spisok = random.sample(range(-100, 100), 10)
print(spisok)
spisok[2] = random.randint(-100, 100)
del spisok[6]
print(spisok)
