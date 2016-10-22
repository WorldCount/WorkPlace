#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import (DIR_WIN_SETTINGS, APP_VERSION)
from engine.wc32app.wcwindows import WCWindow


__author__ = 'WorldCount'


"""
Окна приложения
"""


#
class AppWindow(WCWindow):

    def __init__(self, config_name, parent=None):
        super(AppWindow, self).__init__(parent, config_name, DIR_WIN_SETTINGS)
        self._app_name = 'WorkPlace'
        self.setWindowTitle('%s v.%s' % (self._app_name, APP_VERSION))
