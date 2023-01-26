from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.btn_const.setGeometry(QtCore.QRect(50, 100, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_const.setFont(font)
        self.btn_const.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_const.setStyleSheet("background-color: rgba(219, 193, 178, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_const.setObjectName("btn_const")
        self.btn_plati = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plati.setEnabled(True)
        self.btn_plati.setGeometry(QtCore.QRect(50, 200, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_plati.setFont(font)
        self.btn_plati.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_plati.setStyleSheet("background-color: rgba(231, 211, 191, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_plati.setObjectName("btn_plati")
        self.btn_program = QtWidgets.QPushButton(self.centralwidget)
        self.btn_program.setEnabled(True)
        self.btn_program.setGeometry(QtCore.QRect(50, 300, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_program.setFont(font)
        self.btn_program.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_program.setStyleSheet("background-color: rgba(252, 240, 229, 255);\n"
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
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 650, 80, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;")
        self.btn_back.setObjectName("btn_back")
        self.btn_model = QtWidgets.QPushButton(self.centralwidget)
        self.btn_model.setEnabled(True)
        self.btn_model.setGeometry(QtCore.QRect(50, 400, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_model.setFont(font)
        self.btn_model.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_model.setStyleSheet("background-color: rgba(236, 222, 205, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_model.setObjectName("btn_model")
        self.text_razrabotka = QtWidgets.QLabel(self.centralwidget)
        self.text_razrabotka.setGeometry(QtCore.QRect(115, 20, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.text_razrabotka.setFont(font)
        self.text_razrabotka.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_razrabotka.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.text_razrabotka.setTextFormat(QtCore.Qt.AutoText)
        self.text_razrabotka.setAlignment(QtCore.Qt.AlignCenter)
        self.text_razrabotka.setWordWrap(True)
        self.text_razrabotka.setObjectName("text_razrabotka")
        self.text_prom_files = QtWidgets.QLabel(self.centralwidget)
        self.text_prom_files.setGeometry(QtCore.QRect(865, 20, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.text_prom_files.setFont(font)
        self.text_prom_files.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_prom_files.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.text_prom_files.setTextFormat(QtCore.Qt.AutoText)
        self.text_prom_files.setAlignment(QtCore.Qt.AlignCenter)
        self.text_prom_files.setWordWrap(True)
        self.text_prom_files.setObjectName("text_prom_files")
        self.btn_const_step = QtWidgets.QPushButton(self.centralwidget)
        self.btn_const_step.setEnabled(True)
        self.btn_const_step.setGeometry(QtCore.QRect(970, 100, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_const_step.setFont(font)
        self.btn_const_step.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_const_step.setStyleSheet("background-color: rgba(219, 193, 178, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_const_step.setObjectName("btn_const_step")
        self.btn_plati_step = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plati_step.setEnabled(True)
        self.btn_plati_step.setGeometry(QtCore.QRect(970, 200, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_plati_step.setFont(font)
        self.btn_plati_step.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_plati_step.setStyleSheet("background-color: rgba(231, 211, 191, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_plati_step.setObjectName("btn_plati_step")
        self.btn_program_step = QtWidgets.QPushButton(self.centralwidget)
        self.btn_program_step.setEnabled(True)
        self.btn_program_step.setGeometry(QtCore.QRect(970, 300, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_program_step.setFont(font)
        self.btn_program_step.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_program_step.setStyleSheet("background-color:rgba(252, 240, 229, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_program_step.setObjectName("btn_program_step")
        self.btn_model_step = QtWidgets.QPushButton(self.centralwidget)
        self.btn_model_step.setEnabled(True)
        self.btn_model_step.setGeometry(QtCore.QRect(970, 400, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_model_step.setFont(font)
        self.btn_model_step.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_model_step.setStyleSheet("background-color: rgba(236, 222, 205, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;\n"
"border: none")
        self.btn_model_step.setObjectName("btn_model_step")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_const.setText(_translate("MainWindow", "КОНСТРУКЦИЯ"))
        self.btn_plati.setText(_translate("MainWindow", "ПЛАТЫ"))
        self.btn_program.setText(_translate("MainWindow", "ПРОГРАММИРОВАНИЕ"))
        self.text_manager.setText(_translate("MainWindow", "manager"))
        self.name_project.setText(_translate("MainWindow", "        Проект 868 «Создание концепции и пилотного образца комплексной системы автоматизированного проектирования (САПР) микроэлектронных и микромодульных устройств с использованием технологий цифровых двойников»"))
        self.btn_back.setText(_translate("MainWindow", "назад"))
        self.btn_model.setText(_translate("MainWindow", "МОДЕЛИРОВАНИЕ"))
        self.text_razrabotka.setText(_translate("MainWindow", "РАЗРАБОТКА"))
        self.text_prom_files.setText(_translate("MainWindow", "ПРОМЕЖУТОЧНЫЕ ФАЙЛЫ"))
        self.btn_const_step.setText(_translate("MainWindow", ".STEP"))
        self.btn_plati_step.setText(_translate("MainWindow", ".STEP"))
        self.btn_program_step.setText(_translate("MainWindow", ".STEP"))
        self.btn_model_step.setText(_translate("MainWindow", ".STEP"))

    def add_functions(self):
        a = ""
        # self.btn_const.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        # self.btn_topology.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        # self.btn_program.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        # self.btn_open_kicad_topology.clicked.connect(self.open_topology)
        # self.btn_open_cube_prog.clicked.connect(self.open_prog)
        # self.btn_open_freecad_const.clicked.connect(self.open_const)
        # self.btn_samba_kicad_topology.clicked.connect(self.open_samba)
        # self.btn_samba_freecad_const.clicked.connect(self.open_samba)
        # self.btn_samba_cube_prog.clicked.connect(self.open_samba)
        # self.btn_files_freecad_const.clicked.connect(self.open_files_const)
        # self.btn_files_kicad_topology.clicked.connect(self.open_files_topology)
        # self.btn_files_cube_prog.clicked.connect(self.open_files_programming)

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
