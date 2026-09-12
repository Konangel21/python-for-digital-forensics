evidence_ids = ["DF001", "DF002", "DF003", "DF004"]

evidence_types = ["HDD", "USB", "Mobile", "Laptop"]

for evidence_id, evidence_type in zip(evidence_ids, evidence_types):
    print("evidence", evidence_id, evidence_type)