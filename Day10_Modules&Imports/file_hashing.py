import hashlib
with open("Day10_Modules/evidence.dd", "rb") as f:
     x = hashlib.sha256()
     while True:
            chunk = f.read(4096)
            if chunk == b"":
                 break
            x.update(chunk)

print(x.hexdigest())