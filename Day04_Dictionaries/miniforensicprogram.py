evidence = [
    {"device": "Laptop", "status": "Seized"},
    {"device": "Phone", "status": "Analyzed"},
    {"device": "USB", "status": "Seized"},
    {"device": "Hard Disk", "status": "Analyzed"},
    {"device": "Tablet", "status": "Seized"}
]
analysis_results = 0

for item in evidence:
    if item["status"] == "Analyzed":
        print(item["device"])
        analysis_results = analysis_results + 1


print(f"Total analyzed items: {analysis_results}")