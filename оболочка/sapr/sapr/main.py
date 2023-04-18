"""! @brief Проект по созданию платформы автоматизирования работы c САПР"""

##
# @mainpage Проект 868
#
# @section description_main Описание
# Проект 868 «Создание концепции и пилотного образца комплексной системы
# автоматизированного проектирования (САПР) микроэлектронных и 
# микромодульных устройств с использованием технологий цифровых двойников»
#
# Copyright (c)


##
# @file main.py
#
# @brief Основной файл, выполняющий вызов всех классов и функий программы
#
# @section libraries_main Библиотеки/Модули
# - PyQt5
# - logging
# - argparse
#
# @section author_main Авторы
# - Создано Шараповым Александром 20/05/2022
# - Доработано Белоусовым Дмитрием и Шараповым Александром 15/02/2023
#
# Copyright (c)


# Импортирование
from PyQt5 import QtWidgets
from logger import Logger
import sys
import argparse
from start_window import StartWindow
from manager import Manager
from project_name_create import ProjectNameCreate
from cad_selection import CadSelection
from general_files_const import GeneralFilesConst
from general_files_plati import GeneralFilesPlati
from general_files_program import GeneralFilesProgram
from general_files_model import GeneralFilesModel
from project_name_open import ProjectNameOpen

"""
Функционал, позволяющий запускать программу 
main.py в двух режимах логирования (сами режимы
описываются в классе Logger файла logger.py)
Первый режим - INFO, в этом режиме логи, создаваемые
c выполнением программного кода, записываются в файл
log.log, второй DEBUG, позволяющий видеть логи в 
консоли для более скорой возможности отладки
"""
# Создание логгера
## Парсер для сбора информации из консоли
parser = argparse.ArgumentParser()
## Аргумент debug для запуска в режиме отладки
parser.add_argument("--debug", action="store_true", required=False)
args = vars(parser.parse_args())
level = args['debug']
## Создание объекта логгер класса Logger
logger = Logger("app", level)


# Создание объекта Qt
## Создание Qt приложения
app = QtWidgets.QApplication(sys.argv)
## Создание GUI интерфейса приложения
StartWindowDialog = QtWidgets.QDialog()
start_window_ui = StartWindow()
start_window_ui.setupUi(StartWindowDialog)
StartWindowDialog.show()
logger.info("APP STARTED")

# Functions
def open_project_name_create():
    """Создает новый проект для САПР"""
    ## Создание нового окна для наименования проекта
    global ProjectNameCreateDialog
    ProjectNameCreateDialog = QtWidgets.QDialog()
    project_name_create_ui = ProjectNameCreate()
    project_name_create_ui.setupUi(ProjectNameCreateDialog)
    StartWindowDialog.close()
    ProjectNameCreateDialog.show()
    logger.info("Выбран вариант СОЗДАТЬ ПРОЕКТ")

    def return_back():
        ProjectNameCreateDialog.close()
        StartWindowDialog.show()

    def open_cad_selection():
        """Позволяет выбрать САПРЫ под каждую задачу"""
        ## Создание окна для выбора приложений
        global CadSelectionDialog
        CadSelectionDialog = QtWidgets.QDialog()
        cad_selection_ui = CadSelection()
        cad_selection_ui.set_name(project_name_create_ui.lineEdit.text())
        cad_selection_ui.setupUi(CadSelectionDialog)
        ProjectNameCreateDialog.close()
        CadSelectionDialog.show()
        logger.info("Запущено окно выбора сапров")

        def open_manager():
            """Запускает основное окно оболочки"""
            ## Создание окна с основным функционалом оболочки
            global ManagerWindow
            ManagerWindow = QtWidgets.QMainWindow()
            manager_ui = Manager()
            manager_ui.set_name(project_name_create_ui.lineEdit.text())
            manager_ui.setupUi(ManagerWindow)
            CadSelectionDialog.close()
            ManagerWindow.show()
            logger.info("Запущен основной модуль")

            def return_back():
                ManagerWindow.close()
                StartWindowDialog.show()

            manager_ui.btn_back.clicked.connect(return_back)

            def open_general_files_const():
                """Запуск окна для работы c конструкторским САПР"""
                global GeneralFilesConstDialog
                GeneralFilesConstDialog = QtWidgets.QDialog()
                general_files_const_ui = GeneralFilesConst()
                general_files_const_ui.set_name(project_name_create_ui.lineEdit.text())
                general_files_const_ui.setupUi(GeneralFilesConstDialog)
                GeneralFilesConstDialog.show()
                logger.info("Запущено окно промежуточных данных для конструкторского сапра")

            manager_ui.btn_const_step.clicked.connect(open_general_files_const)

            def open_general_files_plati():
                """Запуск окна для работы c топологическим САПР"""
                global GeneralFilesPlatiDialog
                GeneralFilesPlatiDialog = QtWidgets.QDialog()
                general_files_plati_ui = GeneralFilesPlati()
                general_files_plati_ui.set_name(project_name_create_ui.lineEdit.text())
                general_files_plati_ui.setupUi(GeneralFilesPlatiDialog)
                GeneralFilesPlatiDialog.show()
                logger.info("Запущено окно промежуточных данных для топологического сапра")

            manager_ui.btn_plati_step.clicked.connect(open_general_files_plati)

            def open_general_files_program():
                """Запуск окна для работы c программным САПР"""
                global GeneralFilesProgramDialog
                GeneralFilesProgramDialog = QtWidgets.QDialog()
                general_files_program_ui = GeneralFilesProgram()
                general_files_program_ui.set_name(project_name_create_ui.lineEdit.text())
                general_files_program_ui.setupUi(GeneralFilesProgramDialog)
                GeneralFilesProgramDialog.show()
                logger.info("Запущено окно промежуточных данных для программного сапра")

            manager_ui.btn_program_step.clicked.connect(open_general_files_program)

            def open_general_files_model():
                """Запуск окна для работы c САПР для моделирования"""
                global GeneralFilesModelDialog
                GeneralFilesModelDialog = QtWidgets.QDialog()
                general_files_model_ui = GeneralFilesModel()
                general_files_model_ui.set_name(project_name_create_ui.lineEdit.text())
                general_files_model_ui.setupUi(GeneralFilesModelDialog)
                GeneralFilesModelDialog.show()
                logger.info("Запущено окно промежуточных данных для сапра моделирования")

            manager_ui.btn_model_step.clicked.connect(open_general_files_model)
        ## Запуск управляющего окна
        cad_selection_ui.btn_next.clicked.connect(open_manager)
    ## Запуск окна с выбором САПР
    project_name_create_ui.btn_create.clicked.connect(open_cad_selection)
    project_name_create_ui.btn_back.clicked.connect(return_back)


def open_project_name_open():
    """Открывает уже существующий проект для САПР"""
    ## Создание нового окна для нахождения проекта
    global ProjectNameOpenDialog
    ProjectNameOpenDialog = QtWidgets.QDialog()
    project_name_open_ui = ProjectNameOpen()
    project_name_open_ui.setupUi(ProjectNameOpenDialog)
    StartWindowDialog.close()
    ProjectNameOpenDialog.show()
    logger.info("Выбран вариант ОТКРЫТЬ ПРОЕКТ")

    def return_back():
        ProjectNameOpenDialog.close()
        StartWindowDialog.show()

    def open_main():
        """Создание основного окна оболочки в случае нахождения проекта"""
        exists = False
        with open(fr"\\172.18.202.140\projects\projects.txt", 'r') as f:
            for i in f:
                if i.lower().strip("\n") == project_name_open_ui.enter_name_lineEdit.text():
                    exists = True
        if exists:
            global ManagerWindow
            ManagerWindow = QtWidgets.QMainWindow()
            manager_ui = Manager()
            manager_ui.set_name(project_name_open_ui.enter_name_lineEdit.text())
            manager_ui.setupUi(ManagerWindow)
            ProjectNameOpenDialog.close()
            ManagerWindow.show()
            logger.info("Запущен основной модуль")

            def return_back():
                ManagerWindow.close()
                StartWindowDialog.show()

            manager_ui.btn_back.clicked.connect(return_back)

            def open_inter_files_const():
                """Запуск окна для работы c конструкторским САПР"""
                global GeneralFilesConstDialog
                GeneralFilesConstDialog = QtWidgets.QDialog()
                general_files_const_ui = GeneralFilesConst()
                general_files_const_ui.set_name(project_name_open_ui.enter_name_lineEdit.text())
                general_files_const_ui.setupUi(GeneralFilesConstDialog)
                GeneralFilesConstDialog.show()
                logger.info("Запущено окно промежуточных данных для конструкторского сапра")

            manager_ui.btn_const_step.clicked.connect(open_inter_files_const)

            def open_inter_files_plati():
                """Запуск окна для работы c топологическим САПР"""
                global GeneralFilesPlatiDialog
                GeneralFilesPlatiDialog = QtWidgets.QDialog()
                general_files_plati_ui = GeneralFilesPlati()
                general_files_plati_ui.set_name(project_name_open_ui.enter_name_lineEdit.text())
                general_files_plati_ui.setupUi(GeneralFilesPlatiDialog)
                GeneralFilesPlatiDialog.show()
                logger.info("Запущено окно промежуточных данных для топологического сапра")

            manager_ui.btn_plati_step.clicked.connect(open_inter_files_plati)

            def open_inter_files_program():
                """Запуск окна для работы c программным САПР"""
                global GeneralFilesProgramDialog
                GeneralFilesProgramDialog = QtWidgets.QDialog()
                general_files_program_ui = GeneralFilesProgram()
                general_files_program_ui.set_name(project_name_open_ui.enter_name_lineEdit.text())
                general_files_program_ui.setupUi(GeneralFilesProgramDialog)
                GeneralFilesProgramDialog.show()
                logger.info("Запущено окно промежуточных данных для программного сапра")

            manager_ui.btn_program_step.clicked.connect(open_inter_files_program)

            def open_inter_files_model():
                """Запуск окна для работы c САПР для моделирования"""
                global GeneralFilesModelDialog
                GeneralFilesModelDialog = QtWidgets.QDialog()
                general_files_model_ui = GeneralFilesModel()
                general_files_model_ui.set_name(project_name_open_ui.enter_name_lineEdit.text())
                general_files_model_ui.setupUi(GeneralFilesModelDialog)
                GeneralFilesModelDialog.show()
                logger.info("Запущено окно промежуточных данных для сапра моделирования")

            manager_ui.btn_model_step.clicked.connect(open_inter_files_model)

    project_name_open_ui.btn_back.clicked.connect(return_back)
    project_name_open_ui.btn_open.clicked.connect(open_main)

try:
    ## Запуск функционала по созданию/открытию проекта САПР
    start_window_ui.btn_create.clicked.connect(open_project_name_create)
    start_window_ui.btn_open.clicked.connect(open_project_name_open)
except SystemError:
    print("system error")
    logger.error("Системная ошибка при работе c данными")
except KeyboardInterrupt:
    logger.info("Программа остановлена через клавиатуру")

sys.exit(app.exec_())

