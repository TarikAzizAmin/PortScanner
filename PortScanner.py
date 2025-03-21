#!/usr/bin/python
#Creating a custom port scanner using python scapy module
import socket

"""
    here we are creating a port scanner with SOCKET library, we are trying to create a socket CLIENT and tried to connect to the specified 
    HOST and PORT 
"""
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open and running {sock.recv(1024)}")
        sock.close()
    except socket.error:
        print(f"Couldn't connect to target {target}")

def scan_target(target):
    print(f"Scanning target {target}")
    for port in range(1, 1025):
        scan_port(target, port)

if __name__ == "__main__":
    target_ip = input("Enter the target ip...")
    scan_target(target_ip)

