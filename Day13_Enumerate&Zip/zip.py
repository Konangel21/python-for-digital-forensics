evidence_ids = ["DF001", "DF002", "DF003"]
evidence_types = ["HDD", "USB", "Mobile"]

for evidence_id, evidence_type in zip(evidence_ids, evidence_types):
    print(evidence_id, evidence_type)