Username = input("Enter your username: ")
Attempts = int(input("Enter number of login attempts: "))


def login_report(username, attempts):
    return("Suspicious" if attempts > 3 else "Normal")

status = login_report(Username, Attempts)


print("Username:", Username)
print("Attempts:", Attempts)
print("Status:", status)