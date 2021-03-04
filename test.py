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

if __name__ == "__main__":
    print (get_intersect((0, 1), (0, 2), (1, 10), (1, 9))  )# parallel  lines
    print (get_intersect((0, 1), (0, 2), (1, 10), (2, 10))) # vertical and horizontal lines
    print(get_intersect((0, 0), (0, 2), (1, 1), (-1, 1)))
    print (get_intersect((0, 1), (1, 2), (0, 10), (1, 9)) )