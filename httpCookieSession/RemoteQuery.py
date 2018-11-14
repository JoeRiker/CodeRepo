import os
import requests.packages.urllib3
from requests import Session
import http.cookiejar
import sys

requests.packages.urllib3.disable_warnings()
"""
    Fetch da AskMe senza Login presupponendo che vi sia una sessione
    già loggata e salvata in un cookie su file.
    
"""
cookiefile = 'D:\\biscotto.txt'
loginscriptfile = 'RemoteLogin.py'
numeroQuery = 5
urls = ["https://supporto.aruba.it/Askme/rest/authentication/token",
        "https://supporto.aruba.it/Askme/rest/richieste/lista-richieste-fornitore-paginated?listaStatoAvanz=P&listaStatoAvanz=D&listaIdAsset=37",
        "https://supporto.aruba.it/Askme/rest/richieste/lista-richieste-fornitore-paginated?listaStatoAvanz=P&listaStatoAvanz=D&listaIdAsset=37&flagDestEvento=F",
        "https://supporto.aruba.it/Askme/rest/richieste/lista-richieste-fornitore-paginated?listaStatoAvanz=D&listaIdAsset=37",
        "https://supporto.aruba.it/Askme/rest/ticket/lista-avanzamento-ticket-paginated?listaIdStatoAvanzamento=142&listaIdStatoAvanzamento=63&listaIdStatoAvanzamento=148&listaIdStatoAvanzamento=139",
        "https://supporto.aruba.it/Askme/rest/ticket/lista-avanzamento-ticket-paginated"]
recs = ["DUMMY VALUE",
        "Richieste_D_P  : ",
        "Richieste_NECL : ",
        "Richieste_P    : ",
        "Ticket_Nuovi   : ",
        "Ticket_Tutti   : "]

cj = http.cookiejar.LWPCookieJar(cookiefile)
try:
    cj.load(ignore_discard=True, ignore_expires=True)
except:
    pass
s = Session()
s.cookies = cj
# print(cj)
req = s.get(urls[0], verify=False, cookies=cj)

# print(req.status_code)
if req.status_code == 401:
    # print('Sessione Scaduta o non valida')
    os.system(loginscriptfile)
else:
    if len(sys.argv) != 2:
        for x in range(1, numeroQuery+1):
            req = s.get(urls[x], verify=False, cookies=cj).json()
            print(recs[x] + 'askme sum=' + str(req['recordsTotal']))
    else:
        cosastampare = sys.argv[1]
        req = s.get(urls[int(cosastampare)], verify=False, cookies=cj).json()
        print('askme sum=' + str(req['recordsTotal']))
