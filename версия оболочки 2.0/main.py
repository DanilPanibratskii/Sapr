from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from dialog import Ui_Dialog
from main3 import Ui_MainWindow
from dialog2 import Ui_Dialog2
from enter_name import Ui_MainWindow2

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


# def open_first_window():
#     global MainWindow
#     MainWindow = QtWidgets.QMainWindow()
#     ui1 = Ui_MainWindow()
#     ui1.setupUi(MainWindow)
#     Dialog.close()
#     MainWindow.show()
#
#     def return_back():
#         MainWindow.close()
#         Dialog.show()
#
#     ui1.btn_back.clicked.connect(return_back)


def open_enter_name():
    global MainWindow2
    MainWindow2 = QtWidgets.QMainWindow()
    ui3 = Ui_MainWindow2()
    ui3.setupUi(MainWindow2)
    Dialog.close()
    MainWindow2.show()

    def return_back():
        MainWindow2.close()
        Dialog.show()

    def open_main():
        global MainWindow
        MainWindow = QtWidgets.QMainWindow()
        ui1 = Ui_MainWindow()
        ui1.setupUi(MainWindow)
        MainWindow2.close()
        MainWindow.show()

    ui3.btn_create.clicked.connect(open_main)
    ui3.btn_back.clicked.connect(return_back)


def open_second_window():
    global Dialog2
    Dialog2 = QtWidgets.QDialog()
    ui2 = Ui_Dialog2()
    ui2.setupUi(Dialog2)
    Dialog.close()
    Dialog2.show()

    def return_back():
        Dialog2.close()
        Dialog.show()

    ui2.btn_back.clicked.connect(return_back)


ui.btn_create.clicked.connect(open_enter_name)
ui.btn_open.clicked.connect(open_second_window)

sys.exit(app.exec_())

