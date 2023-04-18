"""! @brief Определяет класс Manager - основное окно приложения."""
##
# @file manager.py
#
# @brief Определяет класс Manager.
#
# @section description_manager Описание
# Определяет создание основного функционального окна приложения - менеджера.
# - Manager
#
# @section libraries_manager Библиотеки/Модули
# - PyQt5
# - subprocess
# - os
# - time
#
#
# @section todo_manager TODO
# - None.
#
# @section author_manager Авторы
# - Создано Шараповым Александром 10/05/2022.
# - Доработано Белоусовым Дмитрием и Шараповым Александром 30/01/2023.
#
# Copyright (c) 

from PyQt5.QtWidgets import QLabel
import subprocess
import os, time

from PyQt5 import QtCore, QtGui, QtWidgets


class Manager(object):
    """! Класс Manager.

    Определяет создание основного окна приложения, a также подключение функционала.
    """

    def __init__(self):
        """! Конструктор класса Manager.

        @return  Создает параметр класса project, используемый в качестве названия проекта.
        """
        self.project = None

    def set_name(self, project):
        """! Функция определения названия проекта.
        
        @param project  Название проекта.
        """
        ## Параметр инициализирующий название проекта в классе
        self.project = project

    def setupUi(self, MainWindow):
        """! Функция определения и оформления основного окна приложения.
        
        @param Mainwindow  Основное окно приложения.
        @return  Объект-макет основного окна приложения.
        """
        ## Описание основного окна приложения.
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

        ## Описание кнопки конструкторского САПР.
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
        self.btn_const.setStyleSheet("background-color: rgba(120, 123, 138, 255);\n"
                                     "color: rgb(1, 1, 1);\n"
                                     "border-radius: 10px;\n"
                                     "border: none")
        self.btn_const.setObjectName("btn_const")

        ## Описание кнопки разработки плат САПР.
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
        self.btn_plati.setStyleSheet("background-color: rgba(69, 196, 176, 255);\n"
                                     "color: rgb(1, 1, 1);\n"
                                     "border-radius: 10px;\n"
                                     "border: none")
        self.btn_plati.setObjectName("btn_plati")

        ## Описание кнопки программисткого САПР.
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
        self.btn_program.setStyleSheet("background-color:rgba(154, 235, 163, 255);\n"
                                       "color: rgb(1, 1, 1);\n"
                                       "border-radius: 10px;\n"
                                       "border: none")
        self.btn_program.setObjectName("btn_program")

        ## Описание виджета manager.
        self.text_manager = QtWidgets.QLabel(self.centralwidget)
        self.text_manager.setGeometry(QtCore.QRect(1070, 650, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(26)
        self.text_manager.setFont(font)
        self.text_manager.setStyleSheet("color: rgb(1, 1, 1);")
        self.text_manager.setTextFormat(QtCore.Qt.AutoText)
        self.text_manager.setObjectName("text_manager")

        ## Описание виджета с названием проекта.
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

        ## Описание кнопки моделирования САПР.
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
        self.btn_model.setStyleSheet("background-color: rgba(218, 253, 186, 255);\n"
                                     "color: rgb(1, 1, 1);\n"
                                     "border-radius: 10px;\n"
                                     "border: none")
        self.btn_model.setObjectName("btn_model")

        ## Описание виджета разработки САПР
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

        ## Описание кнопок с промежуточными файлами
        self.text_prom_files = QtWidgets.QLabel(self.centralwidget)
        self.text_prom_files.setGeometry(QtCore.QRect(860, 20, 300, 50))
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

        ## Описание конпки конструкторского САПР.
        self.btn_const_step = QtWidgets.QPushButton(self.centralwidget)
        self.btn_const_step.setEnabled(False)
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
        self.btn_const_step.setStyleSheet("background-color: rgba(242, 190, 34, 50);\n"
                                          "color: rgb(1, 1, 1);\n"
                                          "border-radius: 10px;\n"
                                          "border: none")
        self.btn_const_step.setObjectName("btn_const_step")

        ## Описание кнопки обновления файлов.
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(940, 520, 141, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
                                      "color: rgb(1, 1, 1);\n"
                                      "border-radius: 10px;")
        self.btn_update.setObjectName("btn_update")

        ## Описание кнопки файлов для платы.
        self.btn_plati_step = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plati_step.setEnabled(False)
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
        self.btn_plati_step.setStyleSheet("background-color: rgba(242, 190, 34, 50);\n"
                                          "color: rgb(1, 1, 1);\n"
                                          "border-radius: 10px;\n"
                                          "border: none")
        self.btn_plati_step.setObjectName("btn_plati_step")

        ## Описание кнопки файла для программистского САПР.
        self.btn_program_step = QtWidgets.QPushButton(self.centralwidget)
        self.btn_program_step.setEnabled(False)
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
        self.btn_program_step.setStyleSheet("background-color: rgba(242, 190, 34, 50);\n"
                                            "color: rgb(1, 1, 1);\n"
                                            "border-radius: 10px;\n"
                                            "border: none")
        self.btn_program_step.setObjectName("btn_program_step")

        ## Описание кнопки для файла моделирования САПР.
        self.btn_model_step = QtWidgets.QPushButton(self.centralwidget)
        self.btn_model_step.setEnabled(False)
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
        self.btn_model_step.setStyleSheet("background-color: rgba(242, 190, 34, 50);\n"
                                          "color: rgb(1, 1, 1);\n"
                                          "border-radius: 10px;\n"
                                          "border: none")
        self.btn_model_step.setObjectName("btn_model_step")
        MainWindow.setCentralWidget(self.centralwidget)

        ## Вызов функции retranslateUi.
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## Вызов функции добавления обработчиков кнопок.
        self.add_functions()

    def retranslateUi(self, MainWindow):
        """! Ретрансляция названий на уже определенные кнопки и виджеты.

        @param MainWindow  Основное окно с подготовленными кнопками.
        @return  Возвращает полученный макет с кнопками и названиями.
        
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_const.setText(_translate("MainWindow", "КОНСТРУКЦИЯ"))
        self.btn_plati.setText(_translate("MainWindow", "ПЛАТЫ"))
        self.btn_program.setText(_translate("MainWindow", "ПРОГРАММИРОВАНИЕ"))
        self.text_manager.setText(_translate("MainWindow", "manager"))
        self.name_project.setText(_translate("MainWindow",
                                             "Проект 868 «Создание концепции и пилотного образца комплексной системы "
                                             "автоматизированного проектирования (САПР) микроэлектронных и "
                                             "микромодульных устройств с использованием технологий цифровых "
                                             "двойников»"))
        self.btn_back.setText(_translate("MainWindow", "назад"))
        self.btn_model.setText(_translate("MainWindow", "МОДЕЛИРОВАНИЕ"))
        self.text_razrabotka.setText(_translate("MainWindow", "РАЗРАБОТКА"))
        self.text_prom_files.setText(_translate("MainWindow", "ПРОМЕЖУТОЧНЫЕ ФАЙЛЫ"))
        self.btn_const_step.setText(_translate("MainWindow", ".STEP"))
        self.btn_update.setText(_translate("MainWindow", "обновить"))
        self.btn_plati_step.setText(_translate("MainWindow", ".STEP"))
        self.btn_program_step.setText(_translate("MainWindow", ".STEP"))
        self.btn_model_step.setText(_translate("MainWindow", ".STEP"))

    def add_functions(self):
        """! Добавляет коннекторы к уже созданным кнопкам приложения."""
        self.btn_const.clicked.connect(lambda: self.open_const())
        self.btn_plati.clicked.connect(lambda: self.open_topology())
        self.btn_program.clicked.connect(lambda: self.open_prog())
        self.btn_model.clicked.connect(lambda: self.open_model())
        self.btn_update.clicked.connect(lambda: self.update())

    def open_const(self):
        """! Открывает соответствующий САПР из выбранного ранее в preferences и запускает его.

        @return  Окно с запущенным приложением для конструкторского САПР.         
        """
        try:
            ## Открытие файла preferences для нахождения нужного конструкторского сапр.
            file_preferences = open(fr"\\172.18.202.140\projects\{self.project}\preferences.txt", 'r')
            const = file_preferences.readline().strip()
            ## Запуск САПР.
            if const == "FREECAD":
                if not os.path.exists(fr"\\172.18.202.140\projects\{self.project}\конструкция\{self.project}.FCStd"):
                    freecad = 'C:/Program Files/FreeCAD 0.20/bin/FreeCAD.exe'
                    subprocess.Popen(freecad)
                else:
                    freecad = fr"\\172.18.202.140\projects\{self.project}\конструкция\{self.project}.FCStd"
                    subprocess.run(["C:/Program Files/FreeCAD 0.20/bin/FreeCAD.exe", freecad])
        except FileNotFoundError:
            self.file_not_found("preferences.txt")

    def open_topology(self):
        """! Открывает соответствующий САПР из выбранного ранее в preferences и запускает его.

        @return  Окно с запущенным приложением для топологического САПР.  
        """
        try:
            ## Открытие файла preferences для нахождения нужного топологического сапр.
            file_preferences = open(fr"\\172.18.202.140\projects\{self.project}\preferences.txt", 'r')
            for i in range(1):
                file_preferences.readline()
            topology = file_preferences.readline().strip()
            ## Запуск САПР.
            if topology == "KICAD":
                if not os.path.exists(fr"\\172.18.202.140\projects\{self.project}\платы\{self.project}.kicad_pro"):
                    kicad = 'C:/Program Files/KiCad/6.0/bin/kicad.exe'
                    subprocess.Popen(kicad)
                else:
                    kicad = fr"\\172.18.202.140\projects\{self.project}\платы\{self.project}.kicad_pro"
                    subprocess.run(["C:/Program Files/KiCad/6.0/bin/kicad.exe", kicad])
        except FileNotFoundError:
            self.file_not_found("preferences.txt")

    def open_prog(self):
        """! Открывает соответствующий САПР из выбранного ранее в preferences и запускает его.

        @return  Окно с запущенным приложением для программсиского САПР.  
        """
        try:
            ## Открытие файла preferences для нахождения нужного программистского сапр.
            file_preferences = open(fr"\\172.18.202.140\projects\{self.project}\preferences.txt", 'r')
            for i in range(2):
                file_preferences.readline()
            prog = file_preferences.readline().strip()
            ## Запуск САПР.
            if prog == "CUBE":
                if not os.path.exists(fr"\\172.18.202.140\projects\{self.project}\программирование\{self.project}.bin"):
                    cube = 'C:\ST\STM32CubeIDE_1.9.0\STM32CubeIDE\stm32cubeide.exe'
                    subprocess.Popen(cube)
                else:
                    cube = fr"\\172.18.202.140\projects\{self.project}\программирование\{self.project}.lnk"
                    subprocess.run(['C:\ST\STM32CubeIDE_1.9.0\STM32CubeIDE\stm32cubeide.exe', cube])
        except FileNotFoundError:
            self.file_not_found("preferences.txt")

    def open_model(self):
        """! Открывает соответствующий САПР из выбранного ранее в preferences и запускает его.

        @return  Окно с запущенным приложением для моделирующего САПР.  
        """
        try:
            ## Открытие файла preferences для нахождения нужного моделирующего сапр.
            file_preferences = open(fr"\\172.18.202.140\projects\{self.project}\preferences.txt", 'r')
            for i in range(3):
                file_preferences.readline()
            model = file_preferences.readline().strip()
            ## Запуск САПР.
            if model == "LTSPICE":
                if not os.path.exists(fr"\\172.18.202.140\projects\{self.project}\моделирование\{self.project}.asc"):
                    spice = 'C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe'
                    subprocess.Popen(spice)
                else:
                    spice = fr"\\172.18.202.140\projects\{self.project}\моделирование\{self.project}.asc"
                    subprocess.run(['C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe', spice])
        except FileNotFoundError:
            self.file_not_found("preferences.txt")

    def update(self):
        """! Проверяет наличие файлов на сервере и перезагружает виджеты с промежуточными файлами"""
        if os.path.exists(
                fr"\\172.18.202.140\projects\{self.project}\конструкция\промежуточные_файлы\{self.project}.step")\
                or os.path.exists(
                fr"\\172.18.202.140\projects\{self.project}\платы\промежуточные_файлы\{self.project}.step")\
                or os.path.exists(
                fr"\\172.18.202.140\projects\{self.project}\программирование\промежуточные_файлы\{self.project}.step") \
                or os.path.exists(
                fr"\\172.18.202.140\projects\{self.project}\моделирование\промежуточные_файлы\{self.project}.step"):
            style = "background-color: rgba(242, 190, 34, 255);"\
                    "color: rgb(1, 1, 1);"\
                    "border-radius: 10px;"\
                    "border: none"
            self.btn_const_step.setEnabled(True)
            self.btn_plati_step.setEnabled(True)
            self.btn_program_step.setEnabled(True)
            self.btn_model_step.setEnabled(True)
            self.btn_const_step.setStyleSheet(style)
            self.btn_plati_step.setStyleSheet(style)
            self.btn_program_step.setStyleSheet(style)
            self.btn_model_step.setStyleSheet(style)

    def file_not_found(self, string):
        """! Выбрасывает виджет при ненахождении файла на сервере.
        
        @param string  Файл, который не удалось найти.
        """
        label = QLabel(f"Can't find {string}")
        label.show()
        time.sleep(5)


# Запуск окна
if __name__ == "__main__":
    import sys
    ## Создание объекта окна приложения
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Manager()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
