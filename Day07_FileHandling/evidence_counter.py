with open("Day07_FileHandling/evidence.txt", "r") as file:
    count = 0
    for line in file:
        line = line.strip()
        if line:
            count += 1


with open("evidence_report.txt", "w") as file:
    file.write("Digital Forensic Evidence Report\n")
    file.write(f"Total Evidence Items: {count}\n")
    file.write("Analysis Status: Complete\n")
print(f"Number of evidence items: {count}")