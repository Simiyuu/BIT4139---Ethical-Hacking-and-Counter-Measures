# static_triage.py - Automated Static File Triage & IOC Extractor
import hashlib
import os
import re

def compute_hashes(file_path):
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
            sha256_hash.update(chunk)
            
    return md5_hash.hexdigest(), sha256_hash.hexdigest()

def extract_ioc_strings(file_path):
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    url_pattern = re.compile(r'https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?')
    registry_pattern = re.compile(r'HKCU\\[a-zA-Z0-9\\_]+|HKLM\\[a-zA-Z0-9\\_]+', re.IGNORECASE)

    extracted_iocs = {"IPs": set(), "URLs": set(), "RegistryKeys": set()}

    with open(file_path, "rb") as f:
        content = f.read().decode('latin-1', errors='ignore')
        
        extracted_iocs["IPs"].update(ip_pattern.findall(content))
        extracted_iocs["URLs"].update(url_pattern.findall(content))
        extracted_iocs["RegistryKeys"].update(registry_pattern.findall(content))

    return extracted_iocs

def run_triage(target_file):
    print("=" * 60)
    print(f"[*] STATIC TRIAGE REPORT: {target_file}")
    print("=" * 60)
    
    if not os.path.exists(target_file):
        print(f"[!] Error: File '{target_file}' not found.")
        return

    md5, sha256 = compute_hashes(target_file)
    print(f"[+] File Size : {os.path.getsize(target_file)} bytes")
    print(f"[+] MD5 Hash  : {md5}")
    print(f"[+] SHA256    : {sha256}")
    print("-" * 60)

    iocs = extract_ioc_strings(target_file)
    print("[*] EXTRACTED INDICATORS OF COMPROMISE (IOCs):")
    for category, findings in iocs.items():
        print(f"  -> {category}:")
        if findings:
            for item in findings:
                print(f"      - {item}")
        else:
            print("      (None detected)")
    print("=" * 60)

sample_path = "suspicious_payload.bin"
dummy_payload = (
    b"MZ\x90\x00\x03\x00\x00\x00"
    b"Host: http://c2-beacon-traffic.org/api/v1 "
    b"IP: 198.51.100.24 "
    b"Persistence: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run "
    b"Dropped: keylogger.dll"
)

with open(sample_path, "wb") as sample:
    sample.write(dummy_payload)

run_triage(sample_path)