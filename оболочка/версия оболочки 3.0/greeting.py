# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        Dialog.setStyleSheet("background-color:rgba(255., 255, 255, 255);")
        self.btn_create = QtWidgets.QPushButton(Dialog)
        self.btn_create.setEnabled(True)
        self.btn_create.setGeometry(QtCore.QRect(350, 300, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_create.setStyleSheet("background-color: rgba(89, 89, 89, 150);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_create.setObjectName("btn_create")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 600, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.btn_open = QtWidgets.QPushButton(Dialog)
        self.btn_open.setEnabled(True)
        self.btn_open.setGeometry(QtCore.QRect(350, 450, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_open.setFont(font)
        self.btn_open.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_open.setStyleSheet("background-color: rgba(89, 89, 89, 150);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_open.setObjectName("btn_open")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_create.setText(_translate("Dialog", "??????????????"))
        self.label_2.setText(_translate("Dialog", "??????????????"))
        self.btn_open.setText(_translate("Dialog", "??????????????"))
