from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgba(255, 255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_const = QtWidgets.QPushButton(self.centralwidget)
        self.btn_const.setEnabled(True)
        self.btn_const.setGeometry(QtCore.QRect(5, 45, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_const.setFont(font)
        self.btn_const.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_const.setStyleSheet("background-color: rgba(104, 104, 104, 250);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_const.setObjectName("btn_const")
        self.btn_topology = QtWidgets.QPushButton(self.centralwidget)
        self.btn_topology.setEnabled(True)
        self.btn_topology.setGeometry(QtCore.QRect(5, 130, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_topology.setFont(font)
        self.btn_topology.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_topology.setStyleSheet("background-color: rgba(124, 124,124, 250);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_topology.setObjectName("btn_topology")
        self.btn_program = QtWidgets.QPushButton(self.centralwidget)
        self.btn_program.setEnabled(True)
        self.btn_program.setGeometry(QtCore.QRect(5, 215, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_program.setFont(font)
        self.btn_program.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_program.setStyleSheet("background-color: rgba(144, 144, 144, 250);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_program.setObjectName("btn_program")
        self.text_manager = QtWidgets.QLabel(self.centralwidget)
        self.text_manager.setGeometry(QtCore.QRect(1070, 650, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(26)
        self.text_manager.setFont(font)
        self.text_manager.setStyleSheet("color: rgb(1, 1, 1);")
        self.text_manager.setTextFormat(QtCore.Qt.AutoText)
        self.text_manager.setObjectName("text_manager")
        self.name_project = QtWidgets.QLabel(self.centralwidget)
        self.name_project.setGeometry(QtCore.QRect(340, 600, 1001, 91))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.name_project.setFont(font)
        self.name_project.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.name_project.setTextFormat(QtCore.Qt.AutoText)
        self.name_project.setWordWrap(True)
        self.name_project.setObjectName("name_project")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(310, 45, 965, 540))
        self.stackedWidget.setStyleSheet("background-color: rgba(166, 166, 166, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("background-color: rgba(104, 104, 104, 250);\n"
"border-radius: 10px;\n"
"border: none")
        self.page.setObjectName("page")
        self.wall_background_freecad_const = QtWidgets.QLabel(self.page)
        self.wall_background_freecad_const.setGeometry(QtCore.QRect(70, 30, 800, 120))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.wall_background_freecad_const.setFont(font)
        self.wall_background_freecad_const.setStyleSheet("background-color: rgba(217, 217, 217, 200);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: none")
        self.wall_background_freecad_const.setText("")
        self.wall_background_freecad_const.setObjectName("wall_background_freecad_const")
        self.btn_samba_freecad_const = QtWidgets.QPushButton(self.page)
        self.btn_samba_freecad_const.setGeometry(QtCore.QRect(600, 60, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_samba_freecad_const.setFont(font)
        self.btn_samba_freecad_const.setStyleSheet("background-color: rgba(255, 255, 255, 200);\n"
"color: rgb(1, 1, 1);")
        self.btn_samba_freecad_const.setObjectName("btn_samba_freecad_const")
        self.btn_open_freecad_const = QtWidgets.QPushButton(self.page)
        self.btn_open_freecad_const.setGeometry(QtCore.QRect(10, 30, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_open_freecad_const.setFont(font)
        self.btn_open_freecad_const.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 60px;")
        self.btn_open_freecad_const.setObjectName("btn_open_freecad_const")
        self.btn_files_freecad_const = QtWidgets.QPushButton(self.page)
        self.btn_files_freecad_const.setGeometry(QtCore.QRect(350, 60, 150, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_files_freecad_const.setFont(font)
        self.btn_files_freecad_const.setStyleSheet("background-color: rgba(255, 255, 255, 200);\n"
"color: rgb(1, 1, 1);")
        self.btn_files_freecad_const.setObjectName("btn_files_freecad_const")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("background-color: rgba(124, 124,124, 250);\n"
"border-radius: 10px;\n"
"border: none")
        self.page_2.setObjectName("page_2")
        self.btn_files_kicad_topology = QtWidgets.QPushButton(self.page_2)
        self.btn_files_kicad_topology.setGeometry(QtCore.QRect(350, 60, 150, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_files_kicad_topology.setFont(font)
        self.btn_files_kicad_topology.setStyleSheet("background-color: rgba(255, 255, 255, 200);\n"
"color: rgb(1, 1, 1);")
        self.btn_files_kicad_topology.setObjectName("btn_files_kicad_topology")
        self.wall_background_kicad_topology = QtWidgets.QLabel(self.page_2)
        self.wall_background_kicad_topology.setGeometry(QtCore.QRect(70, 30, 800, 120))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.wall_background_kicad_topology.setFont(font)
        self.wall_background_kicad_topology.setStyleSheet("background-color: rgba(217, 217, 217, 200);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: none")
        self.wall_background_kicad_topology.setText("")
        self.wall_background_kicad_topology.setObjectName("wall_background_kicad_topology")
        self.btn_open_kicad_topology = QtWidgets.QPushButton(self.page_2)
        self.btn_open_kicad_topology.setGeometry(QtCore.QRect(10, 30, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_open_kicad_topology.setFont(font)
        self.btn_open_kicad_topology.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 60px;")
        self.btn_open_kicad_topology.setObjectName("btn_open_kicad_topology")
        self.btn_samba_kicad_topology = QtWidgets.QPushButton(self.page_2)
        self.btn_samba_kicad_topology.setGeometry(QtCore.QRect(600, 60, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_samba_kicad_topology.setFont(font)
        self.btn_samba_kicad_topology.setStyleSheet("background-color: rgba(255, 255, 255, 200);\n"
"color: rgb(1, 1, 1);")
        self.btn_samba_kicad_topology.setObjectName("btn_samba_kicad_topology")
        self.wall_background_kicad_topology.raise_()
        self.btn_files_kicad_topology.raise_()
        self.btn_open_kicad_topology.raise_()
        self.btn_samba_kicad_topology.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("background-color: rgba(144, 144, 144, 250);\n"
"border-radius: 10px;\n"
"border: none")
        self.page_3.setObjectName("page_3")
        self.wall_background_cube_prog = QtWidgets.QLabel(self.page_3)
        self.wall_background_cube_prog.setGeometry(QtCore.QRect(70, 30, 800, 120))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.wall_background_cube_prog.setFont(font)
        self.wall_background_cube_prog.setStyleSheet("background-color: rgba(217, 217, 217, 200);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: none")
        self.wall_background_cube_prog.setText("")
        self.wall_background_cube_prog.setObjectName("wall_background_cube_prog")
        self.btn_samba_cube_prog = QtWidgets.QPushButton(self.page_3)
        self.btn_samba_cube_prog.setGeometry(QtCore.QRect(600, 60, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_samba_cube_prog.setFont(font)
        self.btn_samba_cube_prog.setStyleSheet("background-color: rgba(255, 255, 255, 200);\n"
"color: rgb(1, 1, 1);")
        self.btn_samba_cube_prog.setObjectName("btn_samba_cube_prog")
        self.btn_files_cube_prog = QtWidgets.QPushButton(self.page_3)
        self.btn_files_cube_prog.setGeometry(QtCore.QRect(350, 60, 150, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_files_cube_prog.setFont(font)
        self.btn_files_cube_prog.setStyleSheet("background-color: rgba(255, 255, 255, 200);\n"
"color: rgb(1, 1, 1);")
        self.btn_files_cube_prog.setObjectName("btn_files_cube_prog")
        self.btn_open_cube_prog = QtWidgets.QPushButton(self.page_3)
        self.btn_open_cube_prog.setGeometry(QtCore.QRect(10, 30, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_open_cube_prog.setFont(font)
        self.btn_open_cube_prog.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 60px;")
        self.btn_open_cube_prog.setObjectName("btn_open_cube_prog")
        self.stackedWidget.addWidget(self.page_3)
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 650, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 30px;")
        self.btn_back.setObjectName("btn_back")
        self.stackedWidget.raise_()
        self.btn_const.raise_()
        self.btn_topology.raise_()
        self.btn_program.raise_()
        self.text_manager.raise_()
        self.name_project.raise_()
        self.btn_back.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_const.setText(_translate("MainWindow", "КОНСТРУКТОРСКИЙ"))
        self.btn_topology.setText(_translate("MainWindow", "ТОПОЛОГИЯ"))
        self.btn_program.setText(_translate("MainWindow", "ПРОГРАММИРОВАНИЕ"))
        self.text_manager.setText(_translate("MainWindow", "manager"))
        self.name_project.setText(_translate("MainWindow", "        Проект 868 «Создание концепции и пилотного образца комплексной системы автоматизированного проектирования (САПР) микроэлектронных и микромодульных устройств с использованием технологий цифровых двойников»"))
        self.btn_samba_freecad_const.setText(_translate("MainWindow", "ОБЩИЕ ФАЙЛЫ"))
        self.btn_open_freecad_const.setText(_translate("MainWindow", "FREECAD"))
        self.btn_files_freecad_const.setText(_translate("MainWindow", "ФАЙЛЫ"))
        self.btn_files_kicad_topology.setText(_translate("MainWindow", "ФАЙЛЫ"))
        self.btn_open_kicad_topology.setText(_translate("MainWindow", "KICAD"))
        self.btn_samba_kicad_topology.setText(_translate("MainWindow", "ОБЩИЕ ФАЙЛЫ"))
        self.btn_samba_cube_prog.setText(_translate("MainWindow", "ОБЩИЕ ФАЙЛЫ"))
        self.btn_files_cube_prog.setText(_translate("MainWindow", "ФАЙЛЫ"))
        self.btn_open_cube_prog.setText(_translate("MainWindow", "CUBE"))
        self.btn_back.setText(_translate("MainWindow", "back"))

    def add_functions(self):
        self.btn_const.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.btn_topology.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_program.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_open_kicad_topology.clicked.connect(self.open_topology)
        self.btn_open_cube_prog.clicked.connect(self.open_prog)
        self.btn_open_freecad_const.clicked.connect(self.open_const)
        self.btn_samba_kicad_topology.clicked.connect(self.open_samba)
        self.btn_samba_freecad_const.clicked.connect(self.open_samba)
        self.btn_samba_cube_prog.clicked.connect(self.open_samba)
        self.btn_files_freecad_const.clicked.connect(self.open_files_const)
        self.btn_files_kicad_topology.clicked.connect(self.open_files_topology)
        self.btn_files_cube_prog.clicked.connect(self.open_files_programming)

    @staticmethod
    def open_const():
        freecad = 'C:/Program Files/FreeCAD 0.20/bin/FreeCAD.exe'
        subprocess.Popen(freecad)

    @staticmethod
    def open_prog():
        cube = 'C:/Program Files/STMicroelectronics/STM32Cube/STM32CubeProgrammer/bin/STM32CubeProgrammer.exe'
        subprocess.Popen(cube)

    @staticmethod
    def open_topology():
        kicad = 'C:/Program Files/KiCad/6.0/bin/kicad.exe'
        subprocess.Popen(kicad)

    @staticmethod
    def open_samba():
        os.startfile(r"\\172.18.202.140\projects\samba")

    @staticmethod
    def open_files_const():
        os.startfile(r"\\172.18.202.140\projects\construction\file")

    @staticmethod
    def open_files_topology():
        os.startfile(r"\\172.18.202.140\projects\topology\file")

    @staticmethod
    def open_files_programming():
        os.startfile(r"\\172.18.202.140\projects\programming\file")

    @staticmethod
    def create_folder():
        path = r"\\172.18.202.140\projects\project"
        os.mkdir(r"\\172.18.202.140\projects\programming\file")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
