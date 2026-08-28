import socket
from concurrent.futures import ThreadPoolExecutor

TARGET_HOST = "127.0.0.1"  # Target IP (Localhost)
PORTS_TO_SCAN = [21, 22, 80, 443, 8080, 3306]

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        result = sock.connect_ex((TARGET_HOST, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: Closed")
        sock.close()
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

def main():
    print(f"Starting scan on target: {TARGET_HOST}\n" + "-"*35)
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(scan_port, PORTS_TO_SCAN)

if __name__ == "__main__":
    main()
  
