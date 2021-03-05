import numpy as np
def get_intersect(a1, a2, b1, b2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return False
    if (a1[0] <= x/z <= a2[0] or a1[0] >= x/z >= a2[0]) and (b1[0] <= x/z <= b2[0] or b1[0] >= x/z >= b2[0]) and (a1[1] <= y/z <= a2[1] or a1[1] >= y/z >= a2[1]) and (b1[1] <= y/z <= b2[1] or b1[1] >= y/z >= b2[1]):
        return (x/z, y/z)
    return False
def get_normal(x1,y1,x2,y2,x,y):
    if x1 == x2:
        return [x1, y]
    if y1 == y2:
        return [x, y1]
    a = (y1-y2)/(x1-x2)
    b = (x1*y2-x2*y1)/(x1-x2)
    print(a, b)
    an = -1/a
    bn = x/a+y
    g = get_intersect([x1,y1], [x2, y2], [0, bn], [10, 10*an+bn])
    if g!=False:
        return g
    else:
        return False
print(get_normal(0,0,2,1,1,1))
