"""! @brief Определяет класс CadSelection."""
##
# @file cad_selection.py
#
# @brief Определяет класс CadSelection.
#
# @section description_cad_selection Описание
# Определяет создание логгера - дополнительного функционала приложения для отслеживания работы программы.
# - CadSelection (основной класс)
#
# @section libraries_cad_selection Библиотеки/Модули
# - PyQt5
#
#
# @section author_cad_selection Авторы
# - Создано Шараповым Александром 05/08/2022.
# - Доработано Белоусовым Дмитрием и Шараповым Александром 20/12/2022.
#
# Copyright (c).
from PyQt5 import QtCore, QtGui, QtWidgets


class CadSelection(object):
    """! Класс CadSelection определяет окно выбора САПРов.
    
    Окно выбора САПРов появляется при создании нового проекта.
    """
    def __init__(self):
        """! Конструктор класса CadSelection.
        
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
        """! Функция определения и оформления диалогового окна приложения.
        
        @param Dialog  Диалогове окно приложения выбора САПРов.
        @return  Объект-макет диалогового окна приложения.
        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        ## Определение чекбокса для выбора конструкторских САПРов.
        self.comboBox_const = QtWidgets.QComboBox(Dialog)
        self.comboBox_const.setGeometry(QtCore.QRect(330, 30, 250, 40))
        self.comboBox_const.setObjectName("comboBox_const")
        self.comboBox_const.addItem("")
        self.comboBox_const.addItem("")

        ## Определение чекбокса для выбора топологических САПРов.
        self.comboBox_plati = QtWidgets.QComboBox(Dialog)
        self.comboBox_plati.setGeometry(QtCore.QRect(330, 100, 250, 40))
        self.comboBox_plati.setObjectName("comboBox_plati")
        self.comboBox_plati.addItem("")
        self.comboBox_plati.addItem("")

        ## Определение чекбокса для выбора программистских САПРов.
        self.comboBox_program = QtWidgets.QComboBox(Dialog)
        self.comboBox_program.setGeometry(QtCore.QRect(330, 170, 250, 40))
        self.comboBox_program.setObjectName("comboBox_program")
        self.comboBox_program.addItem("")
        self.comboBox_program.addItem("")

        ## Определение чекбокса для выбора моделирующих САПРов.
        self.comboBox_model = QtWidgets.QComboBox(Dialog)
        self.comboBox_model.setGeometry(QtCore.QRect(330, 240, 250, 40))
        self.comboBox_model.setObjectName("comboBox_model")
        self.comboBox_model.addItem("")

        ## Определение кнопки "Далее".
        self.btn_next = QtWidgets.QPushButton(Dialog)
        self.btn_next.setGeometry(QtCore.QRect(510, 330, 80, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        self.btn_next.setFont(font)
        self.btn_next.setStyleSheet("background-color: rgba(217, 217, 217, 255);\n"
"color: rgb(1, 1, 1);\n"
"border-radius: 10px;")
        self.btn_next.setObjectName("btn_next")

        ## Определение текстового виджета с выбором САПРов.
        self.text_sapr = QtWidgets.QLabel(Dialog)
        self.text_sapr.setGeometry(QtCore.QRect(240, 340, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.text_sapr.setFont(font)
        self.text_sapr.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.text_sapr.setTextFormat(QtCore.Qt.AutoText)
        self.text_sapr.setWordWrap(True)
        self.text_sapr.setObjectName("text_sapr")

        ## Определение текстового виджета с выбором конструкторских САПРов.
        self.text_const = QtWidgets.QLabel(Dialog)
        self.text_const.setGeometry(QtCore.QRect(30, 30, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.text_const.setFont(font)
        self.text_const.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.text_const.setTextFormat(QtCore.Qt.AutoText)
        self.text_const.setWordWrap(True)
        self.text_const.setObjectName("text_const")

        ## Определение текстового виджета с выбором топологических САПРов.
        self.text_plati = QtWidgets.QLabel(Dialog)
        self.text_plati.setGeometry(QtCore.QRect(30, 100, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.text_plati.setFont(font)
        self.text_plati.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.text_plati.setTextFormat(QtCore.Qt.AutoText)
        self.text_plati.setWordWrap(True)
        self.text_plati.setObjectName("text_plati")

        ## Определение текстового виджета с выбором программистских САПРов.
        self.text_program = QtWidgets.QLabel(Dialog)
        self.text_program.setGeometry(QtCore.QRect(30, 170, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.text_program.setFont(font)
        self.text_program.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.text_program.setTextFormat(QtCore.Qt.AutoText)
        self.text_program.setWordWrap(True)
        self.text_program.setObjectName("text_program")

        ## Определение текстового виджета с выбором моделирующих САПРов.
        self.text_model = QtWidgets.QLabel(Dialog)
        self.text_model.setGeometry(QtCore.QRect(30, 240, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.text_model.setFont(font)
        self.text_model.setStyleSheet("background-color: rgba(39, 89, 80, 0);\n"
"color: rgb(1, 1, 1);")
        self.text_model.setTextFormat(QtCore.Qt.AutoText)
        self.text_model.setWordWrap(True)
        self.text_model.setObjectName("text_model")

        ## Вызов функции retranslateUi.
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ## Вызов функции добавления обработчиков кнопок.
        self.add_functions()

    def retranslateUi(self, Dialog):
        """! Ретрансляция названий на уже определенные кнопки и виджеты.

        @param Dialog  Диалоговое окно с подготовленными кнопками.
        @return  Возвращает полученный макет с кнопками и названиями.
        
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox_const.setItemText(0, _translate("Dialog", "FREECAD"))
        self.comboBox_const.setItemText(1, _translate("Dialog", "SOLID"))
        self.comboBox_plati.setItemText(0, _translate("Dialog", "KICAD"))
        self.comboBox_plati.setItemText(1, _translate("Dialog", "ALTIUM"))
        self.comboBox_program.setItemText(0, _translate("Dialog", "CUBE"))
        self.comboBox_program.setItemText(1, _translate("Dialog", "QUARTUS"))
        self.comboBox_model.setItemText(0, _translate("Dialog", "LTSPICE"))
        self.btn_next.setText(_translate("Dialog", "далее"))
        self.text_sapr.setText(_translate("Dialog", "Выбор САПР"))
        self.text_const.setText(_translate("Dialog", "КОНСТРУКЦИЯ"))
        self.text_plati.setText(_translate("Dialog", "ПЛАТЫ"))
        self.text_program.setText(_translate("Dialog", "ПРОГРАММИРОВАНИЕ"))
        self.text_model.setText(_translate("Dialog", "МОДЕЛИРОВАНИЕ"))

    def add_functions(self):
        """! Добавляет коннекторы к уже созданным кнопкам приложения."""
        self.btn_next.clicked.connect(lambda: self.save_preferences())

    def save_preferences(self):
        """! Сохраняет выбранные в диалоговом окне САПРы для дальнейшей работы"""
        file_preferences = open(fr"\\172.18.202.140\projects\{self.project}\preferences.txt", 'a')
        file_preferences.write(self.comboBox_const.currentText() + "\n" +
                               self.comboBox_plati.currentText() + "\n" +
                               self.comboBox_program.currentText() + "\n" +
                               self.comboBox_model.currentText() + "\n")
