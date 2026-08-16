evidence = {
    "case_id": "CASE001",
    "device": "Laptop",
    "size": "10GB",
    "status": "Pending",
    "location": "Mumbai",
    "hash_status": "Pending"
}

removed_value = evidence.pop("location")
print(removed_value)