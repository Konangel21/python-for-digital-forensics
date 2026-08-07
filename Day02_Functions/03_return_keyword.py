# Return Keyword

def multiply(a, b):
    return a * b


result = multiply(3, 4)

print(result + 5)

def login_status(attempts):
    if attempts > 3:
        return "Suspicious"
    else:
        return "Normal"


status = login_status(5)

print(status)