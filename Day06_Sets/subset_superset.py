all_evidence = {"HDD", "SSD", "USB", "Mobile"}
digital_evidence = {"HDD", "SSD"}

digital_evidence.issubset(all_evidence)
print(digital_evidence.issubset(all_evidence))
all_evidence.issuperset(digital_evidence)
print(all_evidence.issuperset(digital_evidence))

