evidence_types = {
    "HDD",
    "SSD",
    "USB",
    "Mobile"
}

removed = evidence_types.pop()

print("Removed:", removed)
print("Remaining:", evidence_types)

#.pop() removes and returns an arbitrary element from the set. Since sets are unordered, you cannot predict which element will be removed.