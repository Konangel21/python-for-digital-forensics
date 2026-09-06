logs = [
    "  FAILED LOGIN - ADMIN - 192.168.1.10  ",
    "Successful login - user1 - 192.168.1.5",
    "FAILED LOGIN - ADMIN - 192.168.1.10",
    "Failed login - guest - 10.0.0.5",
    "Successful login - admin - 192.168.1.20"
]
count = 0
for log in logs:
    normalized_log = log.strip().lower().split(" - ")
    if "failed" in normalized_log[0]:
        count+=1
        normalized_log[0].startswith("failed")
        print("FAILED LOGIN DETECTED", "user:",normalized_log[1], "IP:", normalized_log[2])
print("total failed login attempts:", count)