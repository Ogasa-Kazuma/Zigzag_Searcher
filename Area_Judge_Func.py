

class AreaJudgeFunc:

    def __init__(self, centerAreaWidth):
        self.__centerAreaWidth = centerAreaWidth
        pass


    def func(self, decisionMaterials):

        isCenter = self.__IsCenterArea(decisionMaterials)
        if(isCenter):
            return "center"

        isRight = self.__IsRight(decisionMaterials)
        if(isRight):
            return "right"


        return "left"


    def __IsCenterArea(self, decisionMaterials):
        distanceFromCenter = decisionMaterials.GetDistance()
        isNear = (distanceFromCenter < self.__centerAreaWidth)
        if(isNear):
            return True

        return False


    def __IsRight(self, decisionMaterials):

        deg = decisionMaterials.GetDegreeDiff()
        self.__CheckValueError(deg)

        isRight = (deg < 0)
        if(isRight):
            return True

        return False


    def __CheckValueError(self, deg):
        pass
