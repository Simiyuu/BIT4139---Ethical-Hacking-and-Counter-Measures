# BBIT 4139: Application-Layer SQLi Mitigation

This repository contains a secure PHP authentication implementation developed as the final creative mitigation phase of my BBIT 3103 Penetration Testing Practical Portfolio. 

It serves as a direct, application-layer defense against the authentication bypass vulnerabilities (such as the `' OR '1'='1` payload) successfully demonstrated in the Damn Vulnerable Web Application (DVWA) environment during Phase 3 testing.

## 🛡️ Core Security Features

* **PHP Data Objects (PDO):** Utilizes the PDO extension for secure database interactions.
* **Parameterized Queries:** Implements prepared statements to strictly separate SQL logic from user-supplied input data.
* **Input Binding:** Neutralizes malicious syntax by binding variables (`:username`, `:password`) before query execution, entirely preventing the database engine from parsing input strings as executable commands.

## 📂 Repository Contents

* `secure_login.php`: The primary authentication script demonstrating the secure connection and query execution logic.

## 🔍 The Vulnerability Addressed

During the practical assessment, basic string concatenation in SQL queries allowed for severe logic subversion. For example, a standard query like:
`SELECT * FROM users WHERE username = '$user' AND password = '$password'`

Could be easily bypassed by injecting tautologies into the `$user` field, forcing the backend database to evaluate the query as "True" and granting unauthorized access. 

This repository demonstrates how to patch that exact flaw at the source code level rather than relying solely on external Web Application Firewalls (WAFs).

---
**Author:** Chandler Matere | [GitHub: Simiyuu] https://github.com/Simiyuu/cybersecurity-practical-portfolio