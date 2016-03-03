#encoding:utf-8

class WSGIApplication(object):
    def __init__(self, document_root=None, **kw):
        pass

    # 添加一个URL定义:
    def add_url(self, func):
        pass

    # 添加一个Interceptor定义:
    def add_interceptor(self, func):
        pass

    # 设置TemplateEngine:
    @property
    def template_engine(self):
        pass

    @template_engine.setter
    def template_engine(self, engine):
        pass

    # 返回WSGI处理函数:
    def get_wsgi_application(self):
        def wsgi(env, start_response):
            # start_response('200 OK', [('Content-Type', 'text/html')])
            # return 'hello'
            pass
        return wsgi

    # 开发模式下直接启动服务器:
    def run(self, port=8003, host='127.0.0.1'):
        from wsgiref.simple_server import make_server
        server = make_server('', port, self.get_wsgi_application())
        server.serve_forever()

wsgi = WSGIApplication()
if __name__ == '__main__':
    wsgi.run()
else:
    application = wsgi.get_wsgi_application()