"""! @brief Определяет класс StartWindow."""
##
# @file start_window.py
#
# @brief Определяет класс StartWindow.
#
# @section description_start_window Описание
# Определяет функционал открытия существующего проекта.
# - StartWindow (основной класс)
#
# @section libraries_start_window Библиотеки/Модули
# - PyQt5
# - os
#
# @section author_start_window Авторы
# - Создано Шараповым Александром 05/08/2022.
# - Доработано Белоусовым Дмитрием и Шараповым Александром 23/12/2022.
#
# Copyright (c).
from PyQt5 import QtCore, QtGui, QtWidgets


class StartWindow(object):
    """! Класс StartWindow определяет стартовое окно приложения.
    
    Стартовое окно приложения появляется при его запуске.
    """
    def setupUi(self, Dialog):
        """! Функция определения и оформления диалогового стартового окна приложения.
        
        @param Dialog  Диалогове окно.
        @return  Объект-макет диалогового окна приложения.
        """
        ## Инициализация диалогового окна
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        Dialog.setStyleSheet("background-color:rgba(255., 255, 255, 255);")

        ## Инициализация кнопки создания проекта.
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

        ## Инициализация виджета с названием "Серапис".
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

        ## Инициализация кнопки открытия проекта.
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

        ## Вызов функции retranslateUi.
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """! Ретрансляция названий на уже определенные кнопки и виджеты.

        @param Dialog  Диалоговое окно с подготовленными кнопками.
        @return  Возвращает полученный макет с кнопками и названиями.
        
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_create.setText(_translate("Dialog", "СОЗДАТЬ"))
        self.label_2.setText(_translate("Dialog", "СЕРАПИС"))
        self.btn_open.setText(_translate("Dialog", "ОТКРЫТЬ"))
