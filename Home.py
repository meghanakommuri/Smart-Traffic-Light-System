# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\Traffic\home2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ImageUpload import ImageUpload

class Home(object):


    def uploadpic(self):
        try:
            self.Dialog2 = QtWidgets.QDialog()
            self.ui2 = ImageUpload()
            self.ui2.setupUi(self.Dialog2)
            self.Dialog2.show()

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(759, 547)
        Dialog.setStyleSheet("background-color: rgb(200, 12, 72);")
        self.toolBox = QtWidgets.QToolBox(Dialog)
        self.toolBox.setGeometry(QtCore.QRect(90, 110, 581, 361))
        self.toolBox.setStyleSheet("font: 12pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 581, 291))
        self.page.setObjectName("page")
        self.tableView = QtWidgets.QTableView(self.page)
        self.tableView.setGeometry(QtCore.QRect(50, 20, 491, 271))
        self.tableView.setStyleSheet("border-image: url(IowaDOT.jpg);")
        self.tableView.setObjectName("tableView")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 581, 291))
        self.page_2.setObjectName("page_2")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(150, 30, 250, 200))
        self.pushButton.setStyleSheet("border-image: url(upload-icon-19.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        #####################
        self.pushButton.clicked.connect(self.uploadpic)
        #####################

        self.toolBox.addItem(self.page_2, "")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 591, 51))
        self.label_2.setStyleSheet("font: 16pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "Welcome"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "Traffic Detection"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Traffic Analysis Using Canny Edge</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
