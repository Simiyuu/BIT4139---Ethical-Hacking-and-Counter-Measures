import json

def audit_cloud_storage_policy(policy_data):
    print("--- Cloud Storage Security Posture Audit ---")
    print("[*] Analyzing bucket policy for public exposure and encryption...\n")
    
    try:
        policy = json.loads(policy_data)
        statements = policy.get("Statement", [])
        
        public_exposure = False
        encryption_enforced = False
        
        for stmt in statements:
            if stmt.get("Effect") == "Allow" and stmt.get("Principal") == "*":
                actions = stmt.get("Action", [])
                if any("GetObject" in a or "PutObject" in a for a in actions):
                    public_exposure = True
                    print("[-] CRITICAL VULNERABILITY: Bucket allows public anonymous access.")
                    print(f"    -> Action Allowed: {actions}")
                    

            if stmt.get("Effect") == "Deny" and "PutObject" in stmt.get("Action", ""):
                condition = stmt.get("Condition", {})
                if "s3:x-amz-server-side-encryption" in condition.get("Null", {}):
                    encryption_enforced = True
                    
        if not public_exposure:
            print("[+] PASS: No public anonymous access detected.")
            
        if encryption_enforced:
            print("[+] PASS: Server-side encryption is enforced on uploads.")
        else:
            print("[!] WARNING: Server-side encryption is NOT explicitly enforced.")
            
    except json.JSONDecodeError:
        print("[!] Error: Invalid JSON policy format.")
        
    print("-" * 50)

insecure_bucket_policy = """
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::university-student-data/*"
    }
  ]
}
"""

audit_cloud_storage_policy(insecure_bucket_policy)