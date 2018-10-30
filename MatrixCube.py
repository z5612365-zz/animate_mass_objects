import math
class Cube():
    def __init__(self, idxw, idxh, w, h):

        self.vertexD = idxw
        self.vertexW = idxh
        self.check(w, h)

    def check(self, w, h):
        if self.vertexD<0 or self.vertexD>=w or self.vertexW<0 or self.vertexW>=h:
            self.vertexD=-1
            self.vertexW=-1





"""
-1 is none

"""

"""
        h
 +-------------
 |      W
 |
w|D
 |
 |

"""
class MatrixCube():


    def __init__(self, GroupCubeD, GroupCubeW, circleIterateRadius):

        self.GroupCubeD = GroupCubeD
        self.GroupCubeW = GroupCubeW

        self.CubeWeight = 1
        self.CubeHeight = 0.05
        self.CubeDepth = 1
        self.space = 0.1

        # =============================================

        self.circleIterateRadius=circleIterateRadius
        self.defaultVertexDistance=1


        # =============================================

        self.iterateCount=0
        self.workingList=[]

        self.Matrix = [[0 for x in range(self.GroupCubeW)] for y in range(self.GroupCubeD)]

        self.traveledVertexMatrix = [[0 for x in range(self.GroupCubeW)] for y in range(self.GroupCubeD)]

        for i in range(self.GroupCubeD):
            for j in range(self.GroupCubeW):
                self.Matrix[i][j] = i * self.GroupCubeD + j

        for i in range(self.GroupCubeD):
            for j in range(self.GroupCubeW):
                self.traveledVertexMatrix[i][j] = -1


    # =============================================
    def indexToMatrixDW(self, index):
        return Cube(index / self.GroupCubeW, index % self.GroupCubeW, self.GroupCubeD, self.GroupCubeW)

    def matrixDWToIndex(self, cube):
        index=cube.vertexD*self.GroupCubeW+cube.vertexW


        if index < 0:
            index=-1
        else:
            index = index


        return index


    def isInCircle(self, vertexTarget, vertexTarget2):

        if self.getObjectsDistance(vertexTarget,vertexTarget2) <= self.iterateCount * self.circleIterateRadius:
            return True
        else:
            return False

    def getObjectsDistance(self, vertexTarget1, vertexTarget2):
        distanceTmp=math.pow((vertexTarget2.vertexD-vertexTarget1.vertexD)*self.defaultVertexDistance, 2)\
                    +math.pow((vertexTarget2.vertexW-vertexTarget1.vertexW)*self.defaultVertexDistance, 2)

        distance=math.sqrt(distanceTmp)
        return distance



    def printCube(self, cube):
        print(cube.vertexD, cube.vertexW)



    def drop(self, index):

        while not self.isTraveledAllVertex():
            self.AddTraveledVertexIterate(index)
            self.iterateCount += 1

        print(self.workingList)



    def AddTraveledVertexIterate(self, index):

        TmpList=[]

        vertexTarget = self.indexToMatrixDW(index)


        for i in range(self.GroupCubeD):
            for j in range(self.GroupCubeW):
                vertexTarget2 = Cube(i, j, self.GroupCubeD, self.GroupCubeW)

                if self.traveledVertexMatrix[i][j] == -1 and self.isInCircle(vertexTarget, vertexTarget2):
                    vertexTarget2Idx=self.matrixDWToIndex(vertexTarget2)
                    TmpList.append(vertexTarget2Idx)
                    self.traveledVertexMatrix[vertexTarget2.vertexD][vertexTarget2.vertexW] = self.iterateCount

        self.workingList.append(TmpList)





    def isTraveledVertex(self, index):

        vertexTarget = self.indexToMatrixDW(index)

        if self.traveledVertexMatrix[vertexTarget.vertexD][vertexTarget.vertexW]==-1:
            return False
        else:
            return True

    def isTraveledAllVertex(self):

        for i in range(self.GroupCubeD):
            for j in range(self.GroupCubeW):
                if self.traveledVertexMatrix[i][j] == -1:
                    return False
        return True

"""
if __name__ == '__main__':

    MC=MatrixCube(20,20)
    MC.drop(150)
    #MC.getAroundObjects(150)
    
"""