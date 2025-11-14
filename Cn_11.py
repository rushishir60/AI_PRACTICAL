import socket

user_input = input("Enter a domain name or IP address: ")

def is_ip(address):
    try:
        socket.inet_aton(address)   # Check if IPv4
        return True
    except socket.error:
        return False

if is_ip(user_input):      # If input is an IP
    try:
        domain_name = socket.gethostbyaddr(user_input)
        print(f"Domain name for IP {user_input} is: {domain_name[0]}")
    except socket.herror:
        print("No domain (PTR record) found for this IP.")
else:                       # Otherwise treat as domain
    try:
        ip_address = socket.gethostbyname(user_input)
        print(f"IP address for domain {user_input} is: {ip_address}")
    except socket.gaierror:
        print("Invalid domain name.")
