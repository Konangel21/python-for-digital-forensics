evidence = {
    "case_id": "DF501",
    "device": "Mobile Phone",
    "brand": "Samsung",
    "status": "Seized"
}
print(evidence.get("brand"))

evidence.update({"status": "Analyzed",
 "examiner": "Konangel"})

for key in evidence.keys():
    print(key)

for value in evidence.values():
    print(value)

evidence.update({"location": "Delhi",
 "hash_status": "Verified"})

removed_brand = evidence.pop("brand")
print(removed_brand)

for key, value in evidence.items():
    print(f"{key} -> {value}")