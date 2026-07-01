import re

def extract_corporate_intelligence(file_path):
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    discovered_patterns = set()

    try:
        with open(file_path, 'r', encoding='utf-8') as data_source:
            for line in data_source:
                matches = re.findall(email_regex, line)
                for match in matches:
                    if "kenya-airways.com" in match:
                        discovered_patterns.add(match)

        print(f"--- Mapped Targets Summary ({len(discovered_patterns)} Records Found) ---")
        for email in sorted(discovered_patterns):
            print(f"[TARGET] Identified Endpoint User: {email}")
            
    except FileNotFoundError:
        print(f"[!] Error: Could not find the file '{file_path}'.")

extract_corporate_intelligence('raw_maltego_export.txt')