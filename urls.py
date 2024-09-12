from views import Login, Index, WareHouse, RepairHistory
from datetime import date


def secret_front(request):
    request['date'] = date.today()
    request['name'] = 'Владимир Александрович'


carws_obj = [secret_front]
cswp_obj = {
    '/login': Login(),
    '/': Index(),
    '/warehouse': WareHouse(),
    '/repair_history': RepairHistory(),
}
