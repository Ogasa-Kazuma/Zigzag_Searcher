
import importlib
import Straight_Line_Maker
import math

importlib.reload(Straight_Line_Maker)


straightLineMaker = Straight_Line_Maker.StraightLineMaker()
xPositions, yPositions = straightLineMaker.Make(x1 = 5, x2 = 10, y1 = 0, y2 = 10)
print(xPositions)
print(yPositions)
print(360 + math.degrees(math.atan2(4 - 5, 4 -5 )))
print(360 + math.degrees(math.atan2(4 - 5 , 3 - 5)))
print("a")
