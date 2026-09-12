usernames = ["ADMIN", "root", "guest"]

ips = ["192.168.1.10", "10.0.0.5", "172.16.0.8"]


for index, (username, ip) in enumerate(zip(usernames, ips), 1):
    print(index, username.lower(), ip)
