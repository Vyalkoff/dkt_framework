from views import Login, Index
from datetime import date


def secret_front(request):
    request['date'] = date.today()


carws_obj = [secret_front]
cswp_obj = {
    '/login': Login(),
    '/': Index(),
}
