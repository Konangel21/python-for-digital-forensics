Username = input("Enter Username: ")
Ip_address = input("Enter IP address: ")
Failed_attempts = int(input("Enter number of Failed attempts: "))
if Failed_attempts >=3:
    Status = "Suspicious"
else:
    Status = "Normal"

print("===== Login Report =====")
print("Username:", Username)
print("Ip_address:", Ip_address)
print("Failed_attempts:", Failed_attempts)
print("Status:", Status)
