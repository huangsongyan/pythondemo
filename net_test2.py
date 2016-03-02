#encoding:utf-8

import json
import functools
from transwarp import web


@web.api
@web.get('/api/users')
def api_get_users():

    return "asd"




