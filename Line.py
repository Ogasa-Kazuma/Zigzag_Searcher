
import math
import importlib
import Point
importlib.reload(Point)
from Point import Point

class Line:

    def __init__(self, startPoint, lastPoint):
        self.__startPoint = startPoint
        self.__lastPoint = lastPoint

    def GetStartPoint(self):
        return self.__startPoint

    def LinePoints(self):
        #2点間の角度計算

        angle = self.__CalcAngle()
        distance = self.__CalcDistance()

        pointCollection = list()
        pointCollection.append(self.__startPoint)

        #2点を結ぶ直線状の座標を全て計算
        for distance_i in range(0, round(distance)):
            x = self.__CalcX(distance_i, angle)
            y = self.__CalcY(distance_i, angle)
            point = Point(x, y)
            pointCollection.append(point)

        pointCollection.append(self.__lastPoint)

        return pointCollection

    def __CalcAngle(self):

        x_diff = (self.__LastX() - self.__StartX())
        y_diff = (self.__LastY() - self.__StartY())

        angle = math.atan2(y_diff, x_diff)

        return angle


    def __CalcDistance(self):

        x_diff = (self.__LastX() - self.__StartX())
        y_diff = (self.__LastY() - self.__StartY())
        distance = math.sqrt(x_diff ** (2) + y_diff ** (2))

        return distance


    def __StartX(self):
        return self.__startPoint.GetX()

    def __StartY(self):
        return self.__startPoint.GetY()

    def __LastX(self):
        return self.__lastPoint.GetX()

    def __LastY(self):
        return self.__lastPoint.GetY()


    def __CalcX(self, distance, angle):
        x = (self.__StartX() + distance * math.cos(angle))
        return x

    def __CalcY(self, distance, angle):
        y = (self.__StartY() + distance * math.sin(angle))
        return y
