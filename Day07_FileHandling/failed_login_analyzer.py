# Detects failed login attempts and extracts unique suspicious IPs

with open("Day07_FileHandling/security.log") as f:
    count = 0
    suspicious_ips = set()

    for line in f:
        line = line.strip()
        if "Failed login" in line:
            count +=1 
            parts = line.split(" - ")
            suspicious_ips.add(parts[2])
        
print(f"Failed login attempts: {count}")
print(f"Suspicious IPs: {suspicious_ips}")
