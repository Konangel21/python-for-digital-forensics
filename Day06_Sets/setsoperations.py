device_A = {
    "10.10.10.5",
    "192.168.1.20",
    "172.16.0.8",
    "8.8.8.8"
}

device_B = {
    "192.168.1.20",
    "8.8.8.8",
    "1.1.1.1",
    "172.16.0.50"
}

common_ips = device_A & device_B
print(common_ips)
device_A_unique = device_A - device_B
print(device_A_unique)  
device_B_unique = device_B - device_A
print(device_B_unique)
all_unique_ips = device_A | device_B
print(all_unique_ips)   
unique_to_one_source = device_A ^ device_B
print(unique_to_one_source)