#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

# 通过获取hostname，然后再通过hostname反查处机器的IP。
# 但是很多的机器没有规范这个hostname的设置。
# 在linux服务器中容易一直获得127.0.0.1

print(socket.gethostbyname(socket.gethostname()))