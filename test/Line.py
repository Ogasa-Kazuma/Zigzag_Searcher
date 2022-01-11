
import importlib
import Line
importlib.reload(Line)
from Line import Line
import Point
importlib.reload(Point)
from Point import Point





point = Point(6, 9)
print(point.GetY())


point2 = Point(6, 9)
print(point2.GetY())

line = Line(point, point2)
print(line.LinePoints())
