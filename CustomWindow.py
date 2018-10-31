from PySide2 import QtWidgets
from BaseUI import MUIWindow
import os
import maya.cmds as cmds

from . import MatrixCube as MatrixCube


class CustomWindow(MUIWindow.MUIWindow):

    def __init__(self):
        ui_url = os.path.dirname(os.path.abspath(__file__))+'/resource/mui.ui'
        super(CustomWindow,self).__init__(ui_url)

        self.MC= MatrixCube.MatrixCube(int(self.lineEdit.text()), int(self.lineEdit2.text()), float(self.lineEdit4.text()))

        #clean MatrixCube


    # ----------------------------------------------- init UI stuff -----------------------------------------------
    def init_UI(self):
        self.btn = self.getUIElement(QtWidgets.QPushButton,"pushButton")
        self.btn2 = self.getUIElement(QtWidgets.QPushButton,"pushButton_2")
        self.btn3 = self.getUIElement(QtWidgets.QPushButton,"pushButton_3")
        self.btn4 = self.getUIElement(QtWidgets.QPushButton,"pushButton_4")
        self.btn5 = self.getUIElement(QtWidgets.QPushButton,"pushButton_5")


        self.lineEdit = self.getUIElement(QtWidgets.QLineEdit,"lineEdit")
        self.lineEdit2 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_2")
        self.lineEdit3 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_3")
        self.lineEdit4 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_4")
        self.lineEdit5 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_5")

        self.delayFrame = int(self.lineEdit5.text())
        self.dropVertex = int(self.lineEdit3.text())

        self.label = self.getUIElement(QtWidgets.QLabel,"label")

    def SignalSlotLinker(self):

        self.btn.clicked.connect( self.CreateObjects)
        self.btn2.clicked.connect(self.SetKeys)

        self.btn3.clicked.connect(self.PasteKeys)

        self.btn4.clicked.connect(self.Wave)
        self.btn5.clicked.connect(self.Drop)


    def updateValue(self):

        self.btn4.clicked.connect(self.updateMainValue)
        self.btn5.clicked.connect(self.updateMainValue)
        self.btn5.clicked.connect(self.updateDropValue)

    def updateMainValue(self):

        self.delayFrame = int(self.lineEdit5.text())


    def updateDropValue(self):
        self.MC.circleIterateRadius=float(self.lineEdit4.text())
        self.dropVertex = int(self.lineEdit3.text())



    # ----------------------------------------------- slot function -----------------------------------------------

    def CreateObjects(self):
        self.MC= MatrixCube.MatrixCube(int(self.lineEdit.text()), int(self.lineEdit2.text()), float(self.lineEdit4.text()))


        for i in range(0, self.MC.GroupCubeD):
            print("Create Col: "+str(i))
            for j in range(0, self.MC.GroupCubeW):
                cmds.polyCube(w=self.MC.CubeWeight, h=self.MC.CubeHeight, d=self.MC.CubeDepth, n="Cube" + str(i*self.MC.GroupCubeW+j))
                cmds.move(j * (self.MC.CubeWeight + self.MC.space), 0, i * (self.MC.CubeDepth + self.MC.space))


        cubelist = []
        for i in range(0, self.MC.GroupCubeD):
            for j in range(0, self.MC.GroupCubeW):
                cubelist.append("Cube" + str(i*self.MC.GroupCubeW+j))
        print(self.MC.GroupCubeD)
        print(self.MC.GroupCubeW)
        print(cubelist)
        cmds.group(cubelist, n='GroupCube')

    def SetKeys(self):


        cmds.setKeyframe('Cube0', attribute='translateY', t=['1', '40'])
        cmds.setAttr('Cube0.translateY', 5)
        cmds.setKeyframe('Cube0', attribute='translateY', t=['20'])


    def PasteKeys(self):

        cmds.copyKey('Cube0', attribute='translateY')
        for i in range(0, self.MC.GroupCubeD):

            for j in range(0, self.MC.GroupCubeW):
                if i==0 and j==0:
                    continue
                cmds.pasteKey( "Cube" + str(i*self.MC.GroupCubeW+j), attribute='translateY' )

    def Wave(self):

        for i in range(0, self.MC.GroupCubeD):

            for j in range(0, self.MC.GroupCubeW):
                if i == 0 :
                    continue
                cmds.keyframe("Cube" + str(i*self.MC.GroupCubeW+j)+'.translateY', edit=True, iub=True, r=True, o="over", tc=self.delayFrame*i)

    def Drop(self):

        self.MC.drop(self.dropVertex)
        for tmpListIdx, tmpList in enumerate(self.MC.workingList):

            for index in tmpList:
                if tmpListIdx == 0:
                    continue
                cmds.keyframe("Cube" + str(index)+'.translateY', edit=True, iub=True, r=True, o="over", tc=self.delayFrame*tmpListIdx)



#setAttr "Cube00.translateY" 10;
#setKeyframe  "Cube00.translateY";

# currentTime 20 ;
# keyframe -e -iub false -an objects -t "20:21" -r -o over -tc 20 -fc 0.833333 Cube00_translateY ;



#------------------------

"""
currentTime 1 ;
copyKey ;
// Result: 1 // 
selectKey -clear ;
pasteKey -time 1 -float 1 -option merge -copies 1 -connect 0 -timeOffset 0 -floatOffset 0 -valueOffset 0 {"Cube01"};
// Result: 1 // 

"""
# keyframe -e -iub true -r -o over -tc 11 Cube01_translateY ;
