#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import socket
import hashlib

__author__ = 'WorldCount'


"""
Рабочие функции
"""


# Создает директории из списка
def create_dirs(list_dirs):
    if type(list_dirs) == list:
        for new_dir in list_dirs:
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
        return True
    return False


# Возвращает хеш-сумму пароля
def password_to_hash(password):
    md5 = hashlib.md5(password.encode())
    return md5.hexdigest()


# Возвращает IP-адрес
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())
