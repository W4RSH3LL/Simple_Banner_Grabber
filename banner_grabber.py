#!/usr/bin/python3

import socket

try:
    # Get the IP addresses to scan
    ips_to_scan_input = input("Enter the IP addresses to scan\n(separate them using a comma) > ")
    ips = [ip.strip() for ip in ips_to_scan_input.split(",")]
    
    # Get the ports to scan
    ports_to_scan_input = input("Enter the ports to scan\n(separate them using a comma) > ")
    ports = [int(port.strip()) for port in ports_to_scan_input.split(",")]
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

for ip in ips:  # Iterating through each IP address
    for port in ports:  # Iterating through each port for the current IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create our socket object
        s.settimeout(2)  # Set a timeout for socket operations

        try:
            s.connect((ip, port))
            print(f'This is the banner for IP {ip} on port {port}\n[+] Banner: [+]')
            answer = s.recv(1024)
            print(answer.decode('utf-8'))
        except socket.error as err:
            print(f"Cannot connect to IP {ip} on port {port}: {err}")
        finally:
            s.close()
