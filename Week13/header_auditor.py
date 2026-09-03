# header_auditor.py - Automated Web Server Security Header Scanner
import urllib.request
import urllib.error

def audit_security_headers(target_url):
    print("--- Web Server Security Header Audit ---")
    print(f"[*] Target: {target_url}\n")
    
    expected_headers = {
        "Strict-Transport-Security": "Forces HTTPS connections.",
        "X-Frame-Options": "Prevents Clickjacking attacks.",
        "X-Content-Type-Options": "Prevents MIME-sniffing.",
        "Content-Security-Policy": "Mitigates XSS and data injection."
    }
    
    try:
        req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=5)
        headers = response.info()
        
        print("[*] Status: HTTP 200 OK - Analyzing Headers...\n")
        
        for header, description in expected_headers.items():
            if header in headers:
                print(f"[+] PASS | {header}")
            else:
                print(f"[-] FAIL | Missing '{header}'")
                print(f"    -> Impact: {description}")
                
        if "Server" in headers or "X-Powered-By" in headers:
            print("\n[!] WARNING: Server signature or tech stack exposed.")
            if "Server" in headers: print(f"    -> Server: {headers['Server']}")
            if "X-Powered-By" in headers: print(f"    -> Powered By: {headers['X-Powered-By']}")
            
    except urllib.error.URLError as e:
        print(f"[!] Connection failed: {e.reason}")

target = "https://example.com"
audit_security_headers(target)