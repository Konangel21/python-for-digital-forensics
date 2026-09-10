logs = [
    "Failed login - ADMIN - 192.168.1.10",
    "Successful login - user1 - 192.168.1.5",
    "FAILED LOGIN - ROOT - 10.0.0.5",
    "Failed login - guest - 172.16.0.8"
]
usernames = [item.split(" - ")[1].lower() for item in logs if item.lower().startswith("failed")]
print(usernames)
