files = ["disk.dd", "memory.raw", "photo.jpg", "usb.img"]
for index, filename in enumerate(files, 1):
    if filename.endswith(".dd") or filename.endswith(".img"):
        print(index , filename)



evidence_ids = ["DF101", "DF102", "DF103"]
hashes = ["abc123", "def456", "ghi789"]

for evidence_id, file_hash in zip(evidence_ids, hashes):
    print(evidence_id, file_hash)




usernames = ["ADMIN", "Root", "GUEST", "analyst"]

ips = [
    "192.168.1.10",
    "10.0.0.5",
    "172.16.0.8",
    "192.168.1.20"
]

for index, (username, ip) in enumerate (zip(usernames, ips), 1):
    print(index, username.lower(), ip)