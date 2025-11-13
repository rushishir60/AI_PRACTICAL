import socket

# Ask user for input
user_input = input("Enter a domain name or IP address: ")

try:
    # If input is domain name
    ip_address = socket.gethostbyname(user_input)
    print(f"The IP address of {user_input} is: {ip_address}")

except socket.gaierror:
    try:
        # If input is an IP address
        domain_name = socket.gethostbyaddr(user_input)
        print(f"The domain name for IP {user_input} is: {domain_name[0]}")
    except socket.herror:
        print("Invalid input or address not found.")
