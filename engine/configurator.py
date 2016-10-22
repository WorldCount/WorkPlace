#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PyQt5.QtCore import QSettings


__author__ = 'WorldCount'

"""
Конфигуратор приложения
"""


#
class Configurator:

    # Конструктор
    def __init__(self, config_dir=None):

        self._name = 'config.ini'
        self._root = os.path.dirname(__file__)
        self._config_dir = config_dir

        if self._config_dir:
            self._config_path = os.path.join(self._config_dir, self._name)
        else:
            self._config_path = os.path.join(self._root, self._name)

        self.settings = QSettings(self._config_path, QSettings.IniFormat)
        self.settings.setFallbacksEnabled(False)

        if not os.path.exists(self._config_path):
            self._create_default_data()

    # Создает конфиг-файл с настройками по умолчанию
    def create_default_config(self):
        if os.path.exists(self._config_path):
            os.remove(self._config_path)
            self._create_default_data()

    # Создает настройки по умолчанию
    def _create_default_data(self):
        self._create_default_database_cfg()
        self._create_default_app_cfg()
        self._create_default_style_cfg()
        self._create_default_user_cfg()

    # Создает конфиг для БД
    def _create_default_database_cfg(self):
        self.settings.beginGroup('DataBase')
        self.settings.setValue('host', '127.0.0.1')
        self.settings.setValue('port', '5433')
        self.settings.setValue('db_name', 'base_name')
        self.settings.setValue('user', 'user_name')
        self.settings.setValue('pass', 'password')
        self.settings.endGroup()

    # Создает конфиг для стилей
    def _create_default_style_cfg(self):
        self.settings.beginGroup('Style')
        self.settings.setValue('font', 'Arial,12,-1,5,50,0,0,0,0,0')
        self.settings.endGroup()

    # Создает конфиг для приложения
    def _create_default_app_cfg(self):
        self.settings.beginGroup('App')
        self.settings.setValue('logging', True)
        self.settings.setValue('write_ip', True)
        self.settings.endGroup()

    # Создает конфиг для пользователей
    def _create_default_user_cfg(self):
        self.settings.beginGroup('User')
        self.settings.setValue('last_user', 0)
        self.settings.endGroup()

    # Получает значение из секции
    def _get_value(self, section, option, object_type=None):
        if section and option:
            param = '%s%s' % (section, option)
            if object_type:
                return self.settings.value(param, None, object_type)
            else:
                return self.settings.value(param)
        return None

    # Устанавливае значение в секцию
    def _set_value(self, section, option, value):
        if section and option and value:
            param = '%s%s' % (section, option)
            self.settings.setValue(param, value)
            return True
        return False

    # СЕТТЕРЫ
    # Устанавливает значение в секцию к БД
    def set_database_value(self, option, value):
        return self._set_value('DataBase', option, value)

    # Устанавливает значение в секцию к Стилям
    def set_style_value(self, option, value):
        return self._set_value('Style', option, value)

    # Устанавливает значение в секцию к Приложению
    def set_app_value(self, option, value):
        return self._set_value('App', option, value)

    # Устанавливает значение в секцию к Пользователям
    def set_user_value(self, option, value):
        return self._set_value('User', option, value)

    # ГЕТТЕРЫ
    # Получает значение секции БД
    def get_database_value(self, option, object_type=None):
        return self._get_value('Database', option, object_type)

    # Получает значение секции Стилей
    def get_style_value(self, option, object_type=None):
        return self._get_value('Style', option, object_type)

    # Получает значение секции Приложения
    def get_app_value(self, option, object_type=None):
        return self._get_value('App', option, object_type)

    # Получает значение секции Пользователей
    def get_user_value(self, option, object_type=None):
        return self._get_value('User', option, object_type)
