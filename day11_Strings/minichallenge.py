log = "  FAILED LOGIN - ADMIN - 192.168.1.10   "

normalized_log = log.strip().lower().split(" - ")

if normalized_log[0].startswith("failed"):
    print("true")
else:
    print("false")


print("event:" , normalized_log[0],
    "username:" , normalized_log[1],
    "ip:" , normalized_log[2])

