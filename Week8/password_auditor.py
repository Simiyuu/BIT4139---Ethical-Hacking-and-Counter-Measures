import math
import re

def calculate_entropy(password):
    pool_size = 0
    if re.search(r'[a-z]', password): pool_size += 26
    if re.search(r'[A-Z]', password): pool_size += 26
    if re.search(r'\d', password): pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): pool_size += 32
    
    if pool_size == 0: return 0
    
    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def audit_passwords(password_list, common_dictionary):
    print("--- Enterprise Password Security Audit ---")
    for pwd in password_list:
        entropy = calculate_entropy(pwd)
        
        if pwd.lower() in common_dictionary:
            status = "VULNERABLE (Dictionary Match)"
        elif entropy < 60:
            status = "WEAK (Low Entropy)"
        else:
            status = "SECURE (High Entropy)"
            
        print(f"[*] Password: {pwd:<15} | Entropy: {entropy:<6} bits | Status: {status}")

test_passwords = ["admin123", "P@ssw0rd123!", "vQ7!xZ9$kL2#mP", "Chandler2026!"]
compromised_dict = ["admin123", "password", "chandler2026!", "p@ssw0rd123!"]

audit_passwords(test_passwords, compromised_dict)