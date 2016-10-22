#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from engine.windows import AppWindow
from engine.wc32app.wcapps import WCStyleApp


__author__ = 'WorldCount'


app = WCStyleApp(sys.argv)
win = AppWindow('app_win.ini')
win.show()
sys.exit(app.exec_())
