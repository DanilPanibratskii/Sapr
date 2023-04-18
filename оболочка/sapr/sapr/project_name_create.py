"""! @brief Определяет класс ProjectNameCreate."""
##
# @file project_name_create.py
#
# @brief Определяет класс ProjectNameCreate.
#
# @section description_project_name_create Описание
# Определяет функционал открытия существующего проекта.
# - ProjectNameCreate (основной класс)
#
# @section libraries_project_name_create Библиотеки/Модули
# - PyQt5
# - os
#
# @section author_project_name_create Авторы
# - Создано Шараповым Александром 05/08/2022.
# - Доработано Белоусовым Дмитрием и Шараповым Александром 23/12/2022.
#
# Copyright (c).
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class ProjectNameCreate(object):
    """! Класс ProjectNameCreate определяет окно создания проекта.
    
    Окно создания проекта появляется при выборе опции "Создать проект".
    """
    def setupUi(self, Dialog):
        """! Функция определения и оформления диалогового окна приложения для создания проекта.
        
        @param Dialog  Диалогове окно создания проекта.
        @return  Объект-макет диалогового окна приложения.
        """
        ## Инициализация диалогового окна.
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setStyleSheet("color: rgb(255, 255, 255);")

        ## Инициализация кнопки создания проекта.
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

        ## Инициализация виджета с надписью названия проекта.
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

        ## Инициализация кнопки "Назад".
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

        ## Вызов функции retranslateUi.
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ## Вызов функции add_functions.
        self.add_functions()

    def retranslateUi(self, Dialog):
        """! Ретрансляция названий на уже определенные кнопки и виджеты.

        @param Dialog  Диалоговое окно с подготовленными кнопками.
        @return  Возвращает полученный макет с кнопками и названиями.
        
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_create.setText(_translate("Dialog", "СОЗДАТЬ"))
        self.label_2.setText(_translate("Dialog", "Введите название проекта:"))
        self.btn_back.setText(_translate("Dialog", "назад"))

    def add_functions(self):
        """! Добавляет коннекторы к уже созданным кнопкам приложения."""
        self.btn_create.clicked.connect(lambda: self.save_text(self.lineEdit.text()))

    def save_text(self, project):
        """! Сохраняет выбранное в диалоговом окне название проекта для дальнейшей работы"""
        with open(fr"\\172.18.202.140\projects\projects.txt", 'a') as f:
            f.write(project + "\n")
        os.mkdir(fr"\\172.18.202.140\projects\{project}")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\конструкция")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\конструкция\промежуточные_файлы")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\программирование")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\программирование\промежуточные_файлы")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\моделирование")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\моделирование\промежуточные_файлы")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\платы")
        os.mkdir(fr"\\172.18.202.140\projects\{project}\платы\промежуточные_файлы")
