from dkt.templator import render
from patterns.creational_patterns import Storage
from load import get_storage


class Login:
    def __call__(self, request):
        return '200 OK', render('login.html')


class PageNotFound:
    def __call__(self, request):
        return '404 BAD', '404 PAGE Not Found'


class Index:
    def __call__(self, request):
        if request['method'] == 'POST':
            store = Storage(request)
            store.add_storage()
        return '200 OK', render('index.html', logo=request)


class WareHouse:
    def __call__(self, request):
        storage = get_storage()
        return '200 OK', render('warehouse.html', logo=request, storage=storage)


class RepairHistory:
    def __call__(self, request):
        return '200 OK', render('repair_history.html', logo=request)


class StartRepair:
    def __call__(self, request):
        return '200 OK', render('start_repair.html', logo=request)


class RepairParts:
    def __call__(self, request):
        return '200 OK', render('repair_parts.html', logo=request)


class CreateCategory:
    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            print(request)
            data = request['data']

        return '200 OK', render('create_repair.html', logo=request)
