evidence = {
    "device": "HDD",
    "case_id": "DF101"
}

try:
    print(evidence["hash"])

except KeyError:
    print("Hash value not found")