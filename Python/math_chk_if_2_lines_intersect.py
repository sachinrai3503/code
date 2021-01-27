# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
"""
Note - In above article a different approach is discussed.

Below implementation is based on slope and geting the intersection points.

Given 2 points - (x1, y1) & (x2, y2)

Slope = (y2-y1)/(x2-x1)

If both lines are each given by two points, 
first line points:  (x1 , y1) , (x2 , y2) 
second line points: (x3 , y3) , (x4 , y4)

Intersection point (x,y) is given as below.

x = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
y = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))

If two line have equal slope they are parallel ==> Won't intersect or are same line.
else if: lines have diff. slopes with a potential intersection point but they actually 
         don't intersect.
else if: line intersect beyond the limit of 2D graph

If all above FALSE then line intersect at (x,y)

"""

from sys import maxsize

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'x = ' + str(self.x) + " y = " + str(self.y)
    
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

class Grid:
    def __init__(self, top_left_point, bottom_right_point):
        self.top_left_point = top_left_point
        self.bottom_right_point = bottom_right_point

def get_slope(line):
    point1, point2 = line.point1, line.point2
    try:
        slope = (point2.y-point1.y)/(point2.x-point1.x)
    except ZeroDivisionError:
        return maxsize
    return slope

def is_point_on_line(line, point):
    """
    It assumes that point is the potential intersection point of the 2 line.
    """
    if point.x>=line.point1.x and point.x<=line.point2.x:
        if point.y>=line.point1.y and point.y<=line.point2.y:
            return True
    return False

def is_point_in_grid(grid, point):
    if point.x>=grid.top_left_point.x and point.x<=grid.bottom_right_point.x:
        if point.y<=grid.top_left_point.y and point.y>=grid.bottom_right_point.y:
            return True
    return False

def get_intersection_point(line1, line2):
    x1, y1, x2, y2 = line1.point1.x, line1.point1.y, line1.point2.x, line1.point2.y
    x3, y3, x4, y4 = line2.point1.x, line2.point1.y, line2.point2.x, line2.point2.y
    x = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    y = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    return Point(x,y)

def find_intersection_point(grid, line1, line2):
    m1 = get_slope(line1)
    m2 = get_slope(line2)
    print('slope1 =',m1)
    print('slope2 =',m2)
    if (m1==m2):
        print('Line are parallel or same.')
        return None
    inter_point = get_intersection_point(line1, line2)
    if not is_point_in_grid(grid, inter_point):
        print('Line intersect beyond the grid')
        return inter_point
    if not is_point_on_line(line1, inter_point) or not is_point_on_line(line2, inter_point):
        print("Line don't actually intersect")
        return inter_point
    return inter_point

def main():
    top_left_point = Point(2,200)
    bottom_right_point = Point(20,10)
    grid = Grid(top_left_point, bottom_right_point)
    x1, y1, x2, y2 = 4, 15, 4, 20
    x3, y3, x4, y4 = 5, 17, 19, 20
    line1 = Line(Point(x1,y1), Point(x2,y2))
    line2 = Line(Point(x3,y3), Point(x4,y4))
    inter_point = find_intersection_point(grid, line1, line2)
    print(inter_point)

if __name__ == '__main__':
    main()