files = [
    "evidence.dd",
    "photo.jpg",
    "memory.raw",
    "notes.txt",
    "disk.dd"
]
dd_files =[len(item) for item in files if item.endswith(".dd")]
print(dd_files)