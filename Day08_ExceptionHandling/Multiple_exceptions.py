
try:
    evidence_items = int(input("enter number of evidence items = "))
    result = 100 // evidence_items
    print(f"result: {result}")
except ValueError:
    print("Invalid number of evidence items")
except ZeroDivisionError:
    print("number of evidence items cannot be zero")
else:
    print("Evidence calculation completed successfully")
finally:
    print("Evidence analysis session ended")