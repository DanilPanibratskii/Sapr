from PyQt5 import QtCore, QtGui, QtWidgets
from main3 import Ui_MainWindow
import os


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 330, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 30px;")
        self.btn_back.setObjectName("btn_back")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 500, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
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
        self.btn_create = QtWidgets.QPushButton(self.centralwidget)
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
        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

        self.add_functions()

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow2", "back"))
        self.label_2.setText(_translate("MainWindow2", "?????????????? ???????????????? ??????????????:"))
        self.btn_create.setText(_translate("MainWindow2", "??????????????"))

    def add_functions(self):
        self.btn_create.clicked.connect(lambda: self.save_text(self.lineEdit.text()))


    def save_text(self, project):
        with open(r'C:\Users\shwep\PycharmProjects\pyqt5\test.txt', 'a') as f:
            f.write(project + "\n")
        print("very sad")
        os.mkdir(fr"\\172.18.202.140\projects\{project}")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\construction")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\programming")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\samba")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\topology")


# def open_next_window():
#     global MainWindow
#     MainWindow = QtWidgets.QMainWindow()
#     ui1 = Ui_MainWindow()
#     ui1.setupUi(MainWindow)
#     MainWindow2.close()
#     MainWindow.show()
    # def return_back():
    #     MainWindow.close()
    #     Ui_Dialog.show()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow2 = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow2()
#     ui.setupUi(MainWindow2)
#     MainWindow2.show()
#     sys.exit(app.exec_())
