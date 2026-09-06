log = "Failed login - admin - 192.168.1.10"
parts = log.split(" - ")
print("usernme:", parts[1])
print("IP Address:", parts[2])