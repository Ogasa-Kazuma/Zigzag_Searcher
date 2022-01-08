
import math

class StraightLineMaker:

    def __init__(self):
        pass

    def Make(self, x1, x2, y1, y2):

        #2点間の角度計算
        angle = math.atan2((y2 - y1), (x2 - x1))
        distance = math.sqrt((x2 - x1) ** (2) + (y2 - y1) ** (2))

        x, y = list(), list()

        #2点を結ぶ直線状の座標を全て計算
        for distance_i in range(0, round(distance)):
            x.append(x1 + distance_i * math.cos(angle))
            y.append(y1 + distance_i * math.sin(angle))

        return x, y
