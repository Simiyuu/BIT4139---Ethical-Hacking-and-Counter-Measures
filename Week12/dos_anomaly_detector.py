# dos_anomaly_detector.py - Automated Request Rate & DoS Detection
from collections import Counter
import datetime

def analyze_traffic_logs(log_data, threshold=100):
    print("--- Network Traffic Anomaly & DoS Detector ---")
    print(f"[*] Analyzing logs for IPs exceeding {threshold} requests/minute...\n")
    
    ip_list = [entry.split()[0] for entry in log_data]
    traffic_counts = Counter(ip_list)
    
    anomaly_detected = False
    
    for ip, count in traffic_counts.items():
        if count >= threshold:
            anomaly_detected = True
            print(f"[!] ALERT: Possible DoS Attack Detected!")
            print(f"    -> Source IP: {ip}")
            print(f"    -> Request Count: {count} (Exceeds threshold)")
            print(f"    -> Recommended Action: Block IP at firewall and review WAF rules.")
            print("-" * 50)
            
    if not anomaly_detected:
        print("[+] Traffic levels normal. No anomalies detected.")

simulated_logs = [
    "192.168.1.5 - [02/Sep/2026:12:01:00] 'GET /index.html HTTP/1.1' 200",
    "192.168.1.5 - [02/Sep/2026:12:01:05] 'GET /style.css HTTP/1.1' 200",
] + ["10.0.0.42 - [02/Sep/2026:12:01:10] 'GET /api/data HTTP/1.1' 503"] * 150

analyze_traffic_logs(simulated_logs, threshold=100)