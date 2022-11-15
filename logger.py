# Импортируем стандартный модуль logging
import logging

# Создаем новое форматирование
_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def get_file_handler():
    """" Функция форматирования к обработчику"""
    file_handler = logging.FileHandler("logs/api.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_logger(name):
    """" Функция с добавлением обработчика к журналу"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    return logger
