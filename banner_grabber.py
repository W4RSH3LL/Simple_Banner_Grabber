#!/usr/bin/python3

import socket

try:
    ports = []
    ports_to_scan_input = input("Enter the ports to scan\n(separate them using a comma) > ")
    ports = [int(port.strip()) for port in ports_to_scan_input.split(",")]
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

for port in ports:  # Iterating through every port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create our socket object
    s.settimeout(2)  # Set a timeout for socket operations

    try:
        s.connect(("192.168.141.130", port))
        print(f'This is the banner for the port: {port}\n[+] Banner: [+]')
        answer = s.recv(1024)
        print(answer.decode('utf-8'))
    except socket.error as err:
        print(f"Cannot connect to port {port}: {err}")
    finally:
        s.close()
