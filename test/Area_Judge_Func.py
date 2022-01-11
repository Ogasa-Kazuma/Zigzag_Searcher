

import importlib
import Area_Judge_Func

importlib.reload(Area_Judge_Func)


class DecisionMaterials:

    def __init__(self, distance, deg_diff):
        self.__distance = distance
        self.__deg_diff = deg_diff

    def GetDistance(self):
        return self.__distance

    def GetDegreeDiff(self):
        return self.__deg_diff


def main():

    decisionMaterials = DecisionMaterials(distance = 1, deg_diff = -30)
    judger = Area_Judge_Func.AreaJudgeFunc(centerAreaWidth = 0)
    print(judger.func(decisionMaterials))


if __name__ == "__main__":
    main()
