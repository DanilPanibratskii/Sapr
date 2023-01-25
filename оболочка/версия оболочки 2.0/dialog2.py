from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 800)
        self.btn_open_cube_prog = QtWidgets.QPushButton(Dialog)
        self.btn_open_cube_prog.setGeometry(QtCore.QRect(100, 50, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_open_cube_prog.setFont(font)
        self.btn_open_cube_prog.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 60px;")
        self.btn_open_cube_prog.setObjectName("btn_open_cube_prog")
        self.btn_open_cube_prog_2 = QtWidgets.QPushButton(Dialog)
        self.btn_open_cube_prog_2.setGeometry(QtCore.QRect(100, 450, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_open_cube_prog_2.setFont(font)
        self.btn_open_cube_prog_2.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 60px;")
        self.btn_open_cube_prog_2.setObjectName("btn_open_cube_prog_2")
        self.btn_open_cube_prog_3 = QtWidgets.QPushButton(Dialog)
        self.btn_open_cube_prog_3.setGeometry(QtCore.QRect(600, 50, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_open_cube_prog_3.setFont(font)
        self.btn_open_cube_prog_3.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 60px;")
        self.btn_open_cube_prog_3.setObjectName("btn_open_cube_prog_3")
        self.btn_open_cube_prog_4 = QtWidgets.QPushButton(Dialog)
        self.btn_open_cube_prog_4.setGeometry(QtCore.QRect(600, 450, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_open_cube_prog_4.setFont(font)
        self.btn_open_cube_prog_4.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 60px;")
        self.btn_open_cube_prog_4.setObjectName("btn_open_cube_prog_4")
        self.btn_back = QtWidgets.QPushButton(Dialog)
        self.btn_back.setGeometry(QtCore.QRect(10, 730, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 30px;")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_open_cube_prog.setText(_translate("Dialog", "КОНСТРУКТОРСКИЙ"))
        self.btn_open_cube_prog_2.setText(_translate("Dialog", "ПРОГРАММИРОВАНИЕ"))
        self.btn_open_cube_prog_3.setText(_translate("Dialog", "ТОПОЛОГИЯ"))
        self.btn_open_cube_prog_4.setText(_translate("Dialog", "?"))
        self.btn_back.setText(_translate("Dialog", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())
