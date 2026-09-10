files = [
    "Evidence.DD",
    "photo.jpg",
    "MEMORY.RAW",
    "disk.dd",
    "backup.DD",
    "notes.txt"
]
dd_files = [item.lower() for item in files if item.lower().endswith(".dd")]
print(dd_files)