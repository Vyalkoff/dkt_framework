from dkt.templator import render


class Login:
    def __call__(self, request):
        return '200 OK', render('login.html')


class PageNotFound:
    def __call__(self, request):
        return '404 BAD', '404 PAGE Not Found'


class Index:
    def __call__(self, request):
        
        return '200 OK', render('index.html', name=request.get('name'))
