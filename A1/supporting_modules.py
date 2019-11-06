from math import sqrt

EPSILON = 0.001


def pp(x):
    """Returns a pretty-print string representation of a number.
       A float number is represented by an integer, if it is whole,
       and up to two decimal places if it isn't
    """
    if isinstance(x, float):
        return "{0:.2f}".format(x)

class point(object):
    """A point in a two dimensional space"""
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return '(' + pp(self.x) + ', ' + pp(self.y) + ')'


class line(object):
    """A line between two points"""
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __repr__(self):
        return '['+ str(self.src) + '-->' + str(self.dst) + ']'

def intersect (l1, l2):
    """Returns a point at which two lines intersect"""
    x1, y1 = l1.src.x, l1.src.y
    x2, y2 = l1.dst.x, l1.dst.y

    x3, y3 = l2.src.x, l2.src.y
    x4, y4 = l2.dst.x, l2.dst.y

    xdiff = (x1 - x2, x3 - x4)
    ydiff = (y1 - y2, y3 - y4)
    
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return point(0, 0)

    d = (det([x1,y1],[x2,y2]), det([x3,y3],[x4,y4]))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return point(x, y)


def slope(a,b):
    x1 = a.x
    x2 = b.x
    y1 = a.y
    y2 = b.y
    if x2 == x1:
        return 1
    m = (y2-y1)/(x2-x1)
    return m


def distance(a,b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def is_between(self, c):
        a, b = self.a, self.b  
        crossproduct = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)

        # compare versus epsilon for floating point values, or != 0 if using integers
        if abs(crossproduct) > EPSILON:
            return False

        dotproduct = (c.x - a.x) * (b.x - a.x) + (c.y - a.y)*(b.y - a.y)
        if dotproduct < 0:
            return False

        squaredlengthba = (b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)
        if dotproduct > squaredlengthba:
            return False

        return True


def hasIntersect(l1,l2):
    if(Segment(l1.src, l1.dst).is_between(l2.src) or Segment(l1.src, l1.dst).is_between(l2.dst)):
        return True
    return False


def isSameLine(l1,l2):
    if(slope(l1.src,l1.dst) == slope(l2.src,l2.dst) and hasIntersect(l1,l2)):
        return True
    return False						  


if __name__ == '__main__':
    pass
