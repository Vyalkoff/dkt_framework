from views import PageNotFound
from request import PostRequest, GetRequest


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

        if method == 'POST':
            post_params = PostRequest(environ).request_params()
            request['post_params'] = post_params
            print(f'POST-запрос:{post_params}')
        if method == 'GET':
            # ?name1 = value1 & name2 = value2
            get_params = GetRequest().get_params(environ)
            request['get_params'] = get_params
            print(f'GET-параметры: {get_params}')
        print(request)

        for carws in self.carws_lst:
            carws(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
