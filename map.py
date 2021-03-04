import generator
import math
import numpy as np
class city:
    def __init__(self, seed, x, y, population):
        self.seed = seed
        self.x = x
        self.y = y
        self.population = population
class farm:
    def __init__(self, seed, x, y, type):
        self.seed = seed
        self.x = x
        self.y = y
        self.type = type
class intersection:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
class road:
    def __init__(self, type, start, end, x1, y1, x2, y2):
        self.startx = x1
        self.starty = y1
        self.endx = x2
        self.endy = y2
        self.type = type
        self.start = start
        self.end = end
    def check_intersections(self,road2):
        a1 = (self.startx,self.starty)
        a2 = (self.endx, self.endy)
        b1 = (road2.startx, road2.starty)
        b2 = (road2.endx, road2.endy)
        s = np.vstack([a1, a2, b1, b2])  # s for stacked
        h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
        l1 = np.cross(h[0], h[1])  # get first line
        l2 = np.cross(h[2], h[3])  # get second line
        x, y, z = np.cross(l1, l2)  # point of intersection
        if z == 0:  # lines are parallel
            return False
        if (a1[0] < x / z < a2[0] or a1[0] > x / z > a2[0]) and (
                b1[0] < x / z < b2[0] or b1[0] > x / z > b2[0]) and (
                a1[1] < y / z < a2[1] or a1[1] > y / z > a2[1]) and (
                b1[1] < y / z < b2[1] or b1[1] > y / z > b2[1]):
            return [x / z, y / z]
        return False
class country:
    def __init__(self, seed):
        self.seed = seed
        self.year = 1900
        self.cities = []
        self.farms = []
        self.roads = []
        self.intersections = []
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
                c = city(seed, round(generator.get_number(seed, x, 0, 1000)), round(generator.get_number(seed, y, 0, 1000)), abs(round(generator.get_number(seed, y, 0, 10 ** round(generator.get_number(seed, y, 3, 6))))))
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
        for i in range(len(self.cities)):
            sx = self.cities[i].x
            sy = self.cities[i].y
            typ = "Countyside"
            start = self.cities[i]
            endc = abs(round(generator.get_number(seed, x*i+1, 0, len(self.cities)-1)))
            if endc == i and i>0:
                endc = i - 1
            elif endc == i:
                endc = i + 1
            ex = self.cities[endc].x
            ey = self.cities[endc].y
            end = self.cities[endc]
            r = road(typ, start, end, sx, sy, ex, ey)
            k = 0
            for i1 in self.roads:
                if i1.startx == r.startx and i1.starty == r.starty and i1.endx == r.endx and i1.endy == r.endy:
                    k = k+1
                    break
                self.add_intersection(i1, r)
            if k == 0:
                self.roads.append(r)

    def add_intersection(self, road1, road2):
        xy = road1.check_intersections(road2)
        if xy != False:
            x = round(int(xy[0]))
            y = round(int(xy[1]))
            inter = intersection(x, y, "")
            self.intersections.append(inter)
            r1 = road(road1.type, road1.start, inter, road1.startx, road1.starty, x, y)
            r2 = road(road1.type, inter, road1.end, x, y, road1.endx, road1.endy)
            r3 = road(road2.type, road2.start, inter, road2.startx, road2.starty, x, y)
            r4 = road(road2.type, inter, road2.end, x, y, road2.endx, road2.endy)
            self.roads.append(r1)
            self.roads.append(r2)
            self.roads.append(r3)
            self.roads.append(r4)
            try:
                self.roads.remove(road1)
                self.roads.remove(road2)
            except:
                pass