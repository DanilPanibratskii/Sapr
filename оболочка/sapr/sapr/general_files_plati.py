"""! @brief Определяет класс GeneralFilesPlati - всплывающее окно для открытия промежуточных файлов через
САПР топологии. """
##
# @file general_files_plati.py
#
# @brief Определяет класс GeneralFilesPlati.
#
# @section description_general_files_plati Описание
# Определяет создание функционального окна приложения, предназначенного для открытия промежуточных файлов через
# САПР топологии.
# - GeneralFilesPlati
#
# @section libraries_general_files_plati Библиотеки/Модули
# - PyQt5
# - subprocess
# - os
#
#
# @section todo_general_files_plati TODO
# - None.
#
# @section author_general_files_plati Авторы
# - Создано Шараповым Александром 10/05/2022.
# - Доработано Белоусовым Дмитрием и Шараповым Александром 30/01/2023.
#
# Copyright (c)

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os


class GeneralFilesPlati(object):
    """! Класс GeneralFilesPlati.

    Определяет создание окна приложения, в котором есть возможность открыть .step файлы через САПР топологии.
    """

    def __init__(self):
        """! Конструктор класса GeneralFilesPlati.

        @return  Создает параметр класса project, используемый в качестве названия проекта.
        """
        self.project = None

    def set_name(self, project):
        """! Функция определения названия проекта.

        @param project  Название проекта.
        """
        ## Параметр инициализирующий название проекта в классе
        self.project = project

    def setupUi(self, Dialog):
        """! Функция определения и оформления основного окна приложения.

        @param Dialog  Диалоговое окно приложения.
        @return  Объект-макет диалогового окна приложения.
        """
        ## Описание диалогового окна приложения.
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setStyleSheet("background-color: rgba(255, 255, 255, 255)")

        ## Описание кнопки для открытия промежуточного конструкторского файла.
        self.btn_const_step = QtWidgets.QPushButton(Dialog)
        self.btn_const_step.setEnabled(False)
        self.btn_const_step.setGeometry(QtCore.QRect(50, 210, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_const_step.setFont(font)
        self.btn_const_step.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_const_step.setStyleSheet("background-color: rgba(120, 123, 138, 50);\n"
                                          "color: rgb(1, 1, 1);\n"
                                          "border-radius: 10px;\n"
                                          "border: none")
        self.btn_const_step.setObjectName("btn_const_step")

        ## Описание кнопки для открытия промежуточного файла топологии.
        self.btn_plati_step = QtWidgets.QPushButton(Dialog)
        self.btn_plati_step.setEnabled(False)
        self.btn_plati_step.setGeometry(QtCore.QRect(190, 210, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_plati_step.setFont(font)
        self.btn_plati_step.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_plati_step.setStyleSheet("background-color: rgba(69, 196, 176, 50);\n"
                                          "color: rgb(1, 1, 1);\n"
                                          "border-radius: 10px;\n"
                                          "border: none")
        self.btn_plati_step.setObjectName("btn_plati_step")

        ## Описание кнопки для открытия промежуточного программного файла.
        self.btn_program_step = QtWidgets.QPushButton(Dialog)
        self.btn_program_step.setEnabled(False)
        self.btn_program_step.setGeometry(QtCore.QRect(330, 210, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_program_step.setFont(font)
        self.btn_program_step.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_program_step.setStyleSheet("background-color:rgba(154, 235, 163, 50);\n"
                                            "color: rgb(1, 1, 1);\n"
                                            "border-radius: 10px;\n"
                                            "border: none")
        self.btn_program_step.setObjectName("btn_program_step")

        ## Описание кнопки для открытия промежуточного файла моделирования.
        self.btn_model_step = QtWidgets.QPushButton(Dialog)
        self.btn_model_step.setEnabled(False)
        self.btn_model_step.setGeometry(QtCore.QRect(470, 210, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_model_step.setFont(font)
        self.btn_model_step.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_model_step.setStyleSheet("background-color: rgba(218, 253, 186, 50);\n"
                                          "color: rgb(1, 1, 1);\n"
                                          "border-radius: 10px;\n"
                                          "border: none")
        self.btn_model_step.setObjectName("btn_model_step")

        ## Описание виджета названия окна GeneralFilesPlati.
        self.text_name_const = QtWidgets.QLabel(Dialog)
        self.text_name_const.setGeometry(QtCore.QRect(100, 40, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(20)
        self.text_name_const.setFont(font)
        self.text_name_const.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_name_const.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
                                           "color: rgb(1, 1, 1);")
        self.text_name_const.setTextFormat(QtCore.Qt.AutoText)
        self.text_name_const.setAlignment(QtCore.Qt.AlignCenter)
        self.text_name_const.setWordWrap(True)
        self.text_name_const.setObjectName("text_name_const")

        ## Описание виджета названия конструкторского модуля промежуточного файла.
        self.text_const = QtWidgets.QLabel(Dialog)
        self.text_const.setGeometry(QtCore.QRect(30, 160, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(8)
        self.text_const.setFont(font)
        self.text_const.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_const.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
                                      "color: rgb(1, 1, 1);")
        self.text_const.setTextFormat(QtCore.Qt.AutoText)
        self.text_const.setAlignment(QtCore.Qt.AlignCenter)
        self.text_const.setWordWrap(True)
        self.text_const.setObjectName("text_const")

        ## Описание виджета названия модуля топологии промежуточного файла.
        self.text_plati = QtWidgets.QLabel(Dialog)
        self.text_plati.setGeometry(QtCore.QRect(170, 290, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(8)
        self.text_plati.setFont(font)
        self.text_plati.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_plati.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
                                      "color: rgb(1, 1, 1);")
        self.text_plati.setTextFormat(QtCore.Qt.AutoText)
        self.text_plati.setAlignment(QtCore.Qt.AlignCenter)
        self.text_plati.setWordWrap(True)
        self.text_plati.setObjectName("text_plati")

        ## Описание виджета названия программного модуля промежуточного файла.
        self.text_program = QtWidgets.QLabel(Dialog)
        self.text_program.setGeometry(QtCore.QRect(280, 160, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(8)
        self.text_program.setFont(font)
        self.text_program.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_program.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
                                        "color: rgb(1, 1, 1);")
        self.text_program.setTextFormat(QtCore.Qt.AutoText)
        self.text_program.setAlignment(QtCore.Qt.AlignCenter)
        self.text_program.setWordWrap(True)
        self.text_program.setObjectName("text_program")

        ## Описание виджета названия модуля моделирования промежуточного файла.
        self.text_model = QtWidgets.QLabel(Dialog)
        self.text_model.setGeometry(QtCore.QRect(420, 290, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(8)
        self.text_model.setFont(font)
        self.text_model.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_model.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
                                      "color: rgb(1, 1, 1);")
        self.text_model.setTextFormat(QtCore.Qt.AutoText)
        self.text_model.setAlignment(QtCore.Qt.AlignCenter)
        self.text_model.setWordWrap(True)
        self.text_model.setObjectName("text_model")

        ## Вызов функции retranslateUi.
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ## Вызов функции update.
        self.update()

        ## Вызов функции добавления обработчиков кнопок.
        self.add_functions()

    def retranslateUi(self, Dialog):
        """! Ретрансляция названий на уже определенные кнопки и виджеты.

        @param MainWindow  Основное окно с подготовленными кнопками.
        @return  Возвращает полученный макет с кнопками и названиями.

        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_const_step.setText(_translate("Dialog", ".STEP"))
        self.btn_plati_step.setText(_translate("Dialog", ".STEP"))
        self.btn_program_step.setText(_translate("Dialog", ".STEP"))
        self.btn_model_step.setText(_translate("Dialog", ".STEP"))
        self.text_name_const.setText(_translate("Dialog", "ПЛАТЫ"))
        self.text_const.setText(_translate("Dialog", "КОНСТРУКЦИЯ"))
        self.text_plati.setText(_translate("Dialog", "ПЛАТЫ"))
        self.text_program.setText(_translate("Dialog", "ПРОГРАММИРОВАНИЕ"))
        self.text_model.setText(_translate("Dialog", "МОДЕЛИРОВАНИЕ"))

    def add_functions(self):
        """! Добавляет коннекторы к уже созданным кнопкам приложения."""
        module_const = "конструкция"
        self.btn_const_step.clicked.connect(lambda: self.open_step(module_const))
        module_plati = "платы"
        self.btn_plati_step.clicked.connect(lambda: self.open_step(module_plati))
        module_program = "программирование"
        self.btn_program_step.clicked.connect(lambda: self.open_step(module_program))
        module_model = "моделирование"
        self.btn_model_step.clicked.connect(lambda: self.open_step(module_model))

    def open_step(self, module):
        """! Открывает промежуточный файл поданного на вход модуля через топологический САПР.

        @return  Окно с запущенным приложением топологического САПР, открывающим заданный промежуточный файл.
        """

        ## Открытие файла preferences для нахождения нужного топологического сапр.
        file_preferences = open(fr"\\172.18.202.140\projects\{self.project}\preferences.txt", 'r')
        for i in range(1):
            file_preferences.readline()
        topology = file_preferences.readline().strip()

        ## Запуск топологического САПР
        if topology == "KICAD":
            kicad = fr"\\172.18.202.140\projects\{self.project}\{module}\промежуточные_файлы\{self.project}.step"
            if os.path.exists(kicad):
                subprocess.run(["C:/Program Files/KiCad/6.0/bin/kicad.exe", kicad])

    def update(self):
        """! Проверяет наличие файлов на сервере и перезагружает виджеты с промежуточными файлами"""

        ## Описание стиля кнопок
        style_const = "background-color: rgba(120, 123, 138, 255);" \
                      "color: rgb(1, 1, 1);" \
                      "border-radius: 10px;" \
                      "border: none"
        style_plati = "background-color: rgba(69, 196, 176, 255);" \
                      "color: rgb(1, 1, 1);" \
                      "border-radius: 10px;" \
                      "border: none"
        style_program = "background-color:rgba(154, 235, 163, 255);" \
                        "color: rgb(1, 1, 1);" \
                        "border-radius: 10px;" \
                        "border: none"
        style_model = "background-color: rgba(218, 253, 186, 255);" \
                      "color: rgb(1, 1, 1);" \
                      "border-radius: 10px;" \
                      "border: none"

        ## Изменения режима и стиля кнопок
        if os.path.exists(
                fr"\\172.18.202.140\projects\{self.project}\конструкция\промежуточные_файлы\{self.project}.step"):
            self.btn_const_step.setEnabled(True)
            self.btn_const_step.setStyleSheet(style_const)
        if os.path.exists(
                fr"\\172.18.202.140\projects\{self.project}\платы\промежуточные_файлы\{self.project}.step"):
            self.btn_plati_step.setEnabled(True)
            self.btn_plati_step.setStyleSheet(style_plati)
        if os.path.exists(
                fr"\\172.18.202.140\projects\{self.project}\программирование\промежуточные_файлы\{self.project}.step"):
            self.btn_program_step.setEnabled(True)
            self.btn_program_step.setStyleSheet(style_program)
        if os.path.exists(
                fr"\\172.18.202.140\projects\{self.project}\моделирование\промежуточные_файлы\{self.project}.step"):
            self.btn_model_step.setEnabled(True)
            self.btn_model_step.setStyleSheet(style_model)
