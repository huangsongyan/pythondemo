#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
A WSGI application entry.
'''

import urls

from transwarp.web import WSGIApplication


# init wsgi app:
wsgi = WSGIApplication()

wsgi.add_module(urls)

if __name__ == '__main__':
    wsgi.run(8080)
else:
    application = wsgi.get_wsgi_application()
