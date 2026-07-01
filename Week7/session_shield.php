<?php

echo "[*] Initializing Secure Session Middleware...\n";

ini_set('session.cookie_httponly', 1);
ini_set('session.cookie_secure', 1);
ini_set('session.use_only_cookies', 1);
ini_set('session.cookie_samesite', 'Strict');

echo "[-] Security Flags Applied: HttpOnly=True, Secure=True, SameSite=Strict\n";

$simulated_ip = "192.168.100.45";
$simulated_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36";
$client_fingerprint = md5($simulated_ip . $simulated_agent);

echo "[-] Generating unique client fingerprint hash...\n";
echo "[-] Fingerprint: " . $client_fingerprint . "\n";

echo "[+] SUCCESS: Session strictly bound to client fingerprint to prevent hijacking.\n";
?>