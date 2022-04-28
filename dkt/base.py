from views import PageNotFound
from request import PostRequest


class Framework:
    def __init__(self, cswp_obj, carws_obj):
        self.cswp_lst = cswp_obj  # Controller special web-page
        self.carws_lst = carws_obj  # Controller all requests to the  website

    def __call__(self, environ, start_response):

        request = {}
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']
        if path in self.cswp_lst:
            view = self.cswp_lst[path]
        else:
            view = PageNotFound()

        request['method'] = method

        request['logname'] = environ['LOGNAME']
        if method == 'POST':
            result = PostRequest(environ).request_params()
            print(result)

        for carws in self.carws_lst:
            carws(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
