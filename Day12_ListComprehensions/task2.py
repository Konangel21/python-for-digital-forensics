logs = [
    "Failed login - admin - 192.168.1.10",
    "Successful login - user1 - 192.168.1.5",
    "Failed login - guest - 10.0.0.5",
    "Successful login - admin - 192.168.1.20"
]

suspicious_logs = [item for item in logs if item.lower().startswith("failed")]
print(suspicious_logs)