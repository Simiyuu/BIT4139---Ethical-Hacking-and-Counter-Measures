# phishing_scanner.py - Automated Social Engineering & Phishing Indicator Tool
import re

def analyze_email_content(email_text):
    print("--- Automated Phishing Indicator Scan ---")
    
    urgent_keywords = [
        "immediate action", "account suspended", "verify your identity",
        "click here", "urgent", "password expires", "unauthorized login"
    ]
    
    print("[*] Checking for manipulation and urgency indicators...")
    found_keywords = [word for word in urgent_keywords if word.lower() in email_text.lower()]
    
    if found_keywords:
        print(f"[!] WARNING: High-pressure language detected: {', '.join(found_keywords)}")
    else:
        print("[+] No high-pressure language detected.")

    print("\n[*] Extracting embedded URLs for domain verification...")
    url_pattern = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')
    extracted_urls = url_pattern.findall(email_text)
    
    if extracted_urls:
        for url in extracted_urls:
            print(f"  -> Found Link: {url}")
            if "login" in url.lower() or "secure" in url.lower():
                print("      [!] Alert: Suspicious login keyword in URL path.")
    else:
        print("  -> No embedded URLs found.")
        
    print("-" * 40)

sample_email = """
Dear Customer,
Immediate action is required! Your account suspended due to an unauthorized login attempt.
Please verify your identity and restore access by visiting our secure portal:
http://paypal-security-update-2026.com/login/secure_auth.php

Failure to click here within 24 hours will result in permanent deletion.
"""

analyze_email_content(sample_email)