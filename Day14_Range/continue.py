files = ["evidence.dd", "notes.txt", "memory.raw", "photo.jpg"]

for item in files:
    if not item.endswith(".dd") and not item.endswith(".raw"):
       continue
    print("Processing", item)
    
