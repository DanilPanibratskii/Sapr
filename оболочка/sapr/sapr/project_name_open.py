"""! @brief Определяет класс ProjectNameOpen."""
##
# @file project_name_open.py
#
# @brief Определяет класс ProjectNameOpen.
#
# @section description_project_name_open Описание
# Определяет функционал создания нового проекта.
# - ProjectNameOpen (основной класс)
#
# @section libraries_project_name_open Библиотеки/Модули
# - PyQt5
# - os
#
# @section author_project_name_open Авторы
# - Создано Шараповым Александром 05/08/2022.
# - Доработано Белоусовым Дмитрием и Шараповым Александром 23/12/2022.
#
# Copyright (c).
from PyQt5 import QtCore, QtGui, QtWidgets
import logging


class ProjectNameOpen(object):
    """! Класс ProjectNameOpen определяет окно открытия существующего проекта.
    
    Окно открытия проекта появляется при выборе опции "Открыть проект".
    """
    def __init__(self):
        """! Конструктор класса ProjectNameOpen.
        
        @return  Создает объект класса Logger, используемый для логгирования.
        """
        self.logger = logging.getLogger("Serapis")

    def setupUi(self, Dialog):
        """! Функция определения и оформления диалогового окна приложения для открытия проекта.
        
        @param Dialog  Диалогове окно открытия проекта.
        @return  Объект-макет диалогового окна приложения.
        """
        ## Инициализация диалогового окна.
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        self.enter_name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.enter_name_lineEdit.setGeometry(QtCore.QRect(50, 100, 500, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.enter_name_lineEdit.setFont(font)
        self.enter_name_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.enter_name_lineEdit.setObjectName("enter_name_lineEdit")

        ## Инициализация кнопки открытия проекта.
        self.btn_open = QtWidgets.QPushButton(Dialog)
        self.btn_open.setEnabled(True)
        self.btn_open.setGeometry(QtCore.QRect(150, 280, 300, 80))
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

        ## Инициализация виджета с надписью названия проекта.
        self.enter_name = QtWidgets.QLabel(Dialog)
        self.enter_name.setGeometry(QtCore.QRect(50, 50, 350, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_name.sizePolicy().hasHeightForWidth())
        self.enter_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.enter_name.setFont(font)
        self.enter_name.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.enter_name.setTextFormat(QtCore.Qt.AutoText)
        self.enter_name.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_name.setWordWrap(True)
        self.enter_name.setObjectName("enter_name")

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

    def retranslateUi(self, Dialog):
        """! Ретрансляция названий на уже определенные кнопки и виджеты.

        @param Dialog  Диалоговое окно с подготовленными кнопками.
        @return  Возвращает полученный макет с кнопками и названиями.
        
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_open.setText(_translate("Dialog", "ОТКРЫТЬ"))
        self.enter_name.setText(_translate("Dialog", "Введите название проекта:"))
        self.btn_back.setText(_translate("Dialog", "Назад"))

## Запуск окна
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ProjectNameOpen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
