evidence = {
    "case_id": "CF501",
    "device": "Hard Disk",
    "status": "Analyzed"
}

print (evidence.get("serial", "Not Recorded"))
print (evidence.get("examiner", "Unknown"))