#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError


__author__ = 'WorldCount'

"""
Подключение к БД
"""

