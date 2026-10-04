files = [
    "evidence.dd",
    "notes.txt",
    "memory.raw",
    "malware.exe",
    "disk.img",
    "photo.jpg"
]

for item in files:
    if not item.endswith(".dd") and not item.endswith(".raw") and not item.endswith(".img"):
        continue
    print("processing", item)