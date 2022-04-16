from wsgiref.simple_server import make_server
from dkt.base import Framework
from urls import carws_obj,cswp_obj

application = Framework(cswp_obj,carws_obj)

with make_server('', 8000, application) as dkt_server:
    print("Приложение запущено на порту 8000...")
    dkt_server.serve_forever()
