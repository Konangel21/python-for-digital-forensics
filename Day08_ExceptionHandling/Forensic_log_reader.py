try:
    with open("Day07_FileHandling/security.log", "r") as file:
        for line in file:
            print(f"reading line from file: {line.strip()}")
except FileNotFoundError as e:
    print(f"Error: {e}")
else:
    print("successful log processing")
finally:
    print("investigation step completed")
