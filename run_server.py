from wsgiref.simple_server import make_server
from dkt.base import Framework
from urls import carws_obj, cswp_obj

application = Framework(cswp_obj, carws_obj)

with make_server('localhost', 8000, application) as dkt_server:
    httpd = dkt_server.socket.getsockname()
    print(f'Приложение запущено : {httpd[0]}/{httpd[1]} ...')
    import webbrowser
    webbrowser.open(f'http://{httpd[0]}:{httpd[1]}', new=2)
    dkt_server.serve_forever()

