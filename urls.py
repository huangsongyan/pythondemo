#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

import hashlib
import logging
import re
import time


from transwarp.web import get, post, ctx, view, interceptor, seeother, notfound




@get('/')
def index():

    return 'hello'

