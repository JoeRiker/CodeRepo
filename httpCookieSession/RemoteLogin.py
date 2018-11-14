import requests.packages.urllib3
from requests import Session
from requests.auth import HTTPBasicAuth
import http.cookiejar

username = 'marco.margutti'
password = 'P4xw0rdmail00'
cookiefile = 'D:\\biscotto.txt'

requests.packages.urllib3.disable_warnings()
cj = http.cookiejar.LWPCookieJar()
s = Session()
s.cookies = cj
url = 'https://supporto.aruba.it/Askme/rest/authentication/token'
req = s.get(url, verify=False, auth=HTTPBasicAuth(username, password))

# print(req.status_code)
if req.status_code == 401:
    print('Sessione Scaduta o non valida')
else:
    print('Sessione Valida')
    cj.save(filename=cookiefile, ignore_discard=True, ignore_expires=True)
    # s.cookies.save()
    # print(s.cookies)
