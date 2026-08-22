forensic_record = ("CF101", "Samsung", "Mobile Phone", "Seized", "Delhi")
case_id, brand, *details = forensic_record

print(f"Case ID: {case_id}")
print(f"Brand: {brand}")
print(f"Details: {details}")