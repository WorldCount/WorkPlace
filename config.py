#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ctypes
from engine.wcutils.files import create_dirs


__author__ = 'WorldCount'


# Версия приложения
APP_VERSION = '0.1'

# Приложение
my_app_id = 'redesing.mmp3.workplace.1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)


# ПУТИ
# Путь к папке с программой
DIR_PROGRAM = os.path.dirname(__file__)
# Путь к папке с данными
DIR_DATA = os.path.join(DIR_PROGRAM, 'DATA')
# Путь к папке с настроками окон
DIR_WIN_SETTINGS = os.path.join(DIR_DATA, 'WIN_CFG')
# Путь к папке с отчетами
DIR_REPORT = os.path.join(DIR_DATA, 'REPORT')
# Путь к папке с логами
DIR_LOGS = os.path.join(DIR_DATA, 'LOGS')
# Путь к папке с со всеми логами
DIR_DEFAULT_LOGS = os.path.join(DIR_LOGS, 'ALL')


# Файлы
FILE_TYPE = {'W': 'WinPost', 'P': 'PartPost', 'D': 'DW', 'R': 'Sort', 'N': 'Post', 'B': 'Base', 'E': 'EAC',
             'U': 'Unkown' }
# Маска для поиска файлов
FILE_MASK = '*.*F'


# Какие папки создать
_mk_dirs = [DIR_REPORT, DIR_WIN_SETTINGS, DIR_DEFAULT_LOGS]

# Создаем папки для работы
create_dirs(_mk_dirs)
