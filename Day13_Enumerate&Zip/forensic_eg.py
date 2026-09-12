logs = [
    "Successful login - user1 - 192.168.1.5",
    "Failed login - admin - 192.168.1.10",
    "Successful login - user2 - 192.168.1.8",
    "Failed login - guest - 10.0.0.5"
]

for index, log in enumerate(logs, 1):
    if log.lower().startswith("failed login"):
        print(index,log)