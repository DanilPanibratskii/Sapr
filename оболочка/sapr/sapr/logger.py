"""! @brief Определяет класс Logger."""
##
# @file logger.py
#
# @brief Определяет класс Logger.
#
# @section description_logger Описание
# Определяет создание логгера - дополнительного функционала приложения для отслеживания работы программы.
# - Logger (основной класс)
#
# @section libraries_logger Библиотеки/Модули
# - logging
# - logging.config
#
# @section todo_logger TODO
# - None.
#
# @section author_logger Авторы
# - Создано Шараповым Александром 10/08/2022.
# - Доработано Белоусовым Дмитрием и Шараповым Александром 20/12/2022.
#
# Copyright (c).

import logging
import logging.config


class Logger:
    """! Класс Logger.

    Определяет создание функционала для отслеживания бесперебойности работы приложения.    
    """
    def __init__(self, name, debug):
        """! Конструктор класса Logger.
        Работает в двух режимах - INFO (запись логов в файл) и DEBUG (запись в консоль).

        @param name Название логгируемого объекта.
        @param debug Определение вариации запуска приложения в режиме INFO/DEBUG.

        @return Возвращает объект Logger и вариацию записи логов приложения.
        
        """
        if not debug:
            ## Задание параметров для запуска логгирования в режиме INFO.
            logging.basicConfig(
                filename="D:\\sapr\\log.log",
                filemode='w',
                encoding='utf-8',
                format='%(asctime)s %(name)s - %(levelname)s:%(message)s',
                datefmt='%d-%b-%y %H:%M:%S',
                level=logging.INFO
                )
            
        else:
            ## Задание параметров для запуска логгирования в режиме DEBUG.
            logging.basicConfig(
                format='%(asctime)s %(name)s - %(levelname)s:%(message)s',
                datefmt='%d-%b-%y %H:%M:%S',
                level=logging.DEBUG
                )
        ## Логгер с именем обрабатываемого объекта
        self.logger = logging.getLogger(name)

    def info(self, msg):
        """! Функция логгирования информативных событий. 
        
        @return Возвращает строку c логом.
        """
        ## Строка с логом.
        self.logger.info(msg)

    def debug(self, msg):
        """! Функция логгирования отладочных событий. 
        
        @return Возвращает строку c логом.
        """
        ## Строка с логом.
        self.logger.debug(msg)

    def warning(self, msg):
        """! Функция логгирования событий c предупреждением. 
        
        @return Возвращает строку c логом.
        """
        ## Строка с логом.
        self.logger.warning(msg)

    def error(self, msg):
        """! Функция логгирования событий o ошибках. 
        
        @return Возвращает строку c логом.
        """
        ## Строка с логом.
        self.logger.error(msg)
