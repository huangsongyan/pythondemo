#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'


from transwarp.web import get,post,ctx


@get('/')
def index():

    print ctx.request.headers
    return 'hello'

@post('/')
def post():
    print ctx.request.headers
    print ctx.request.header('CONTENT-TYPE','test2')
    return 'post'



