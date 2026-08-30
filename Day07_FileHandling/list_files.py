import os
files = os.listdir("Day07_FileHandling")

for filename in files:
    path = os.path.join("Day07_FileHandling", filename)

    if os.path.isfile(path) and filename.endswith(".log"):
           with open(path) as f:
               print(f"Reading: {filename}" )
               for line in f:
                   print(line.strip())
               

               