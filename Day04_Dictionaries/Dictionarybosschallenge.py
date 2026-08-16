evidence = [
    {
        "case_id": "CF101",
        "device": "Laptop",
        "status": "Analyzed"
    },
    {
        "case_id": "CF102",
        "device": "Phone",
        "status": "Seized"
    },
    {
        "case_id": "CF103",
        "device": "USB",
        "status": "Analyzed"
    },
    {
        "case_id": "CF104",
        "device": "Hard Disk",
        "status": "Seized"
    }
]

Analysis_results = 0
for items in evidence:
    if items["status"] == "Analyzed":
        print(f"Case ID: {items['case_id']}, Device: {items['device']}")
        Analysis_results = Analysis_results + 1
print(f"Total analyzed items: {Analysis_results}")