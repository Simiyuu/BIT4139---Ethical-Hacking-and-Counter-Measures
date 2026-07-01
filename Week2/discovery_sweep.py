import os
import threading
from socket import gethostbyaddr

def ping_host(subnet, host):
    ip = f"{subnet}.{host}"
    response = os.system(f"ping -n 1 -w 1000 {ip} > nul 2>&1")
    if response == 0:
        try:
            hostname = gethostbyaddr(ip)[0]
            print(f"[+] Active Host Discovered: {ip} ({hostname})")
        except:
            print(f"[+] Active Host Discovered: {ip} (No Reverse DNS)")

subnet_target = "192.168.56"
print(f"[*] Starting concurrent sweep on subnet: {subnet_target}.0/24")

threads = []
for i in range(1, 255):
    t = threading.Thread(target=ping_host, args=(subnet_target, i))
    threads.append(t)
    t.start()