events = ["Login","Failed Login","USB Inserted","Failed Login","Logout","Failed Login"]

failed_count = 0

print("Total events:", len(events))

for event in events:
    print("Event:", event)

    if event == "Failed Login":
        failed_count = failed_count + 1

print("Failed login attempts:", failed_count)