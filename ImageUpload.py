# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\Traffic\picupload.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Detection import Detection


class ImageUpload(object):

    def processdef(self):
        try:
            Detection.process()
            file = open("tmp.txt", "r")
            print("")
            self.label.setText(file.read())


        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

            print(e)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 575)
        Dialog.setStyleSheet("background-color: rgb(200, 36, 88);")
        self.detection = QtWidgets.QPushButton(Dialog)
        self.detection.setGeometry(QtCore.QRect(150, 40, 80, 100))
        self.detection.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "border-image: url(traffic-light-icon.png);")
        self.detection.setText("")
        self.detection.setObjectName("detection")

        #################
        self.detection.clicked.connect(self.processdef)
        #################

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(160, 180, 221, 23))
        self.label_5.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 230, 360, 331))
        self.label.setStyleSheet("font: 12pt \"Georgia\";\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Results"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ImageUpload()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

