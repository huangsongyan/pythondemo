#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'


from transwarp.web import get,post


@get('/')
def index():

    return 'hello'



