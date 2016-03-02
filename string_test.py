#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hubery.huang'

try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

#文档注释也可以用特殊变量__doc__访问

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

