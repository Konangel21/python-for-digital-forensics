hash_types = ("MD5", "SHA1", "SHA256", "MD5", "SHA512", "MD5")

print(hash_types.count("MD5"))
print(hash_types.index("SHA256"))
print(hash_types.index("SHA512"))

if "SHA512" in hash_types:
    print("SHA512 is supported")
else:
    print("SHA512 is not supported")