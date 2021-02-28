import generator
import math
class city:
    def __init__(self, seed, x, y):
        self.seed = seed
        self.x = x
        self.y = y
class farm:
    def __init__(self, seed, x, y, type):
        self.seed = seed
        self.x = x
        self.y = y
        self.type = type
class country:
    def __init__(self, seed):
        self.seed = seed
        self.year = 1900
        self.cities = []
        self.farms = []
        x = 554
        y = 123
        while True:
            x = x + 3
            y = y + 1
            is_ok = True
            for i in range(len(self.cities)):
                if abs(generator.get_number(seed, x, 0, 1000) - self.cities[i].x) < 200 and abs(generator.get_number(seed, y, 0, 1000) - self.cities[i].y) < 200:
                    is_ok = False
                    break
            if is_ok:
                c = city(seed, round(generator.get_number(seed, x, 0, 1000)), round(generator.get_number(seed, y, 0, 1000)))
                self.cities.append(c)
            if len(self.cities) == 5:
                break
        x = 745
        y = 323
        z = 3456
        farms = {0: "Молочная ферма", 1: "Металлообрабатывающий завод", 2: "Хлебобулочный завод", 3: "Машиностроительный завод", 4: "Фармацептический завод"}
        while True:
            x = x + 21
            y = y + 2
            z = z + 3
            is_ok = True
            for i in range(len(self.cities)):
                if abs(generator.get_number(seed, x, 0, 1000) - self.cities[i].x) < 50 and abs(generator.get_number(seed, y, 0, 1000) - self.cities[i].y) < 50:
                    is_ok = False
                    break
            for i in range(len(self.farms)):
                if abs(generator.get_number(seed, x, 0, 1000) - self.farms[i].x) < 50 and abs(generator.get_number(seed, y, 0, 1000) - self.farms[i].y) < 50:
                    is_ok = False
                    break
            if is_ok:
                f = farm(seed, round(generator.get_number(seed, x, 0, 1000)), round(generator.get_number(seed, y, 0, 1000)), farms[round(generator.get_number(seed, y, 0, len(farms)-1))])
                self.farms.append(f)
            if len(self.farms) == 10:
                break
