import numpy as np
def get_normal(x1,y1,x2,y2,x,y):
    if x1 == x2:
        return [x1, y]
    if y1 == y2:
        return [x, y1]
    a = (y1-y2)/(x1-x2)
    b = (x1*y2-x2*y1)/(x1-x2)
    print(a, b)
    xn = a*(x+a*y-a*b)/(a**2+1)
    yn = a**2*(x+a*y-a*b)/(a**2+1)+b
    return [xn, yn]
def get_normal_in(x1,y1,x2,y2,x,y):
    pass
print(get_normal(0,0,2,1,1,1))
