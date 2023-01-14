class Country:
    def __init__(self, population):
        self.population = population

    def get_population(self):
        return f"Население:{self.population}"

    def set_population(self, population):
        self.population = population
        return population


class Russia(Country):
    pass


class Germany(Country):
    pass


class Canada(Country):
    pass


A = Russia(1000000)
print(A.get_population())
A.set_population(10000)
print(A.get_population())
B = Germany(200000)
print(B.get_population())
B.set_population(10000)
print(B.get_population())
C = Canada(300000)
print(C.get_population())
C.set_population(10000)
print(C.get_population())
