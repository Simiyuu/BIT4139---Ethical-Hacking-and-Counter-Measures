$LogFile = "lab_environment_report.log"
"--- SECURITY LAB PRE-FLIGHT DIAGNOSTICS ---" | Out-File $LogFile

$IsAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if ($IsAdmin) { 
    "[-] Privilege Level: Administrator Access Confirmed" | Out-File $LogFile -Append 
} else { 
    "[!] WARNING: Non-Admin Privileges. Some Nmap features (e.g., raw packet scanning) will fail." | Out-File $LogFile -Append 
}

$NmapCheck = Get-Command nmap -ErrorAction SilentlyContinue
if ($NmapCheck) {
    $NmapVersion = (nmap -V | Select-String -Pattern "Nmap version")
    "[-] Diagnostic Success: $NmapVersion" | Out-File $LogFile -Append
} else {
    "[!] critical error: Nmap bin pathway not found in System Environment variables." | Out-File $LogFile -Append
}s

Get-Content $LogFile