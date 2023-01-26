from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_create = QtWidgets.QPushButton(Dialog)
        self.btn_create.setEnabled(True)
        self.btn_create.setGeometry(QtCore.QRect(150, 280, 300, 80))
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
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 500, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 350, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
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
        self.btn_back = QtWidgets.QPushButton(Dialog)
        self.btn_back.setGeometry(QtCore.QRect(10, 330, 80, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.add_functions()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_create.setText(_translate("Dialog", "СОЗДАТЬ"))
        self.label_2.setText(_translate("Dialog", "Введите название проекта:"))
        self.btn_back.setText(_translate("Dialog", "назад"))

    def add_functions(self):
        self.btn_create.clicked.connect(lambda: self.save_text(self.lineEdit.text()))

    def save_text(self, project):
        with open(r'C:\Users\shwep\PycharmProjects\pyqt5\test.txt', 'a') as f:
            f.write(project + "\n")
        os.mkdir(fr"\\172.18.202.140\projects\{project}")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\конструкция")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\программирование")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\моделирование")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\платы")
