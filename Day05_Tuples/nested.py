evidence_records = (
    ("CF101", "Laptop"),
    ("CF102", "Mobile"),
    ("CF103", "USB")
)

for case_number, device_type in evidence_records:
    print(f"{case_number} -> {device_type}")