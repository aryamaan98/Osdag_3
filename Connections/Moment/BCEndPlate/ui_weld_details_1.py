# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_weld_details_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Weld_Details_1(object):
    def setupUi(self, Weld_Details_1):
        Weld_Details_1.setObjectName("Weld_Details_1")
        Weld_Details_1.resize(811, 323)
        self.scrollArea = QtWidgets.QScrollArea(Weld_Details_1)
        self.scrollArea.setGeometry(QtCore.QRect(9, 9, 791, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 789, 239))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_picture_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_picture_1.setGeometry(QtCore.QRect(0, 0, 391, 241))
        self.label_picture_1.setText("")
        self.label_picture_1.setPixmap(QtGui.QPixmap("ResourceFiles/images/nopreview.png"))
        self.label_picture_1.setObjectName("label_picture_1")
        self.label_picture_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_picture_2.setGeometry(QtCore.QRect(400, 0, 391, 241))
        self.label_picture_2.setText("")
        self.label_picture_2.setObjectName("label_picture_2")
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(380, 0, 31, 241))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_note_1 = QtWidgets.QLabel(Weld_Details_1)
        self.label_note_1.setGeometry(QtCore.QRect(10, 260, 791, 20))
        self.label_note_1.setObjectName("label_note_1")
        self.label_note_2 = QtWidgets.QLabel(Weld_Details_1)
        self.label_note_2.setGeometry(QtCore.QRect(10, 280, 791, 20))
        self.label_note_2.setObjectName("label_note_2")
        self.label_note_3 = QtWidgets.QLabel(Weld_Details_1)
        self.label_note_3.setGeometry(QtCore.QRect(10, 300, 791, 20))
        self.label_note_3.setObjectName("label_note_3")

        self.retranslateUi(Weld_Details_1)
        QtCore.QMetaObject.connectSlotsByName(Weld_Details_1)

    def retranslateUi(self, Weld_Details_1):
        _translate = QtCore.QCoreApplication.translate
        Weld_Details_1.setWindowTitle(_translate("Weld_Details_1", "Typical Butt Weld Details"))
        self.label_note_1.setText(_translate("Weld_Details_1", "Note1"))
        self.label_note_2.setText(_translate("Weld_Details_1", "Note2"))
        self.label_note_3.setText(_translate("Weld_Details_1", "Note3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Weld_Details_1 = QtWidgets.QDialog()
    ui = Ui_Weld_Details_1()
    ui.setupUi(Weld_Details_1)
    Weld_Details_1.show()
    sys.exit(app.exec_())

