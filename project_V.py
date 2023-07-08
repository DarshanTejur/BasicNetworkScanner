import socket
import sys

def scan_ports(target_host, start_port, end_port):
    for port in range(start_port, end_port+1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the socket connection

        # Try to connect to the target host and port
        result = sock.connect_ex((target_host, port))

        # Check if the port is open or closed
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

        # Close the socket connection
        sock.close()

# Example usage
target_host = "192.30.253.112"  # Google Public DNS IP address
start_port = 1
end_port = 100

print(f"Scanning ports {start_port}-{end_port} on {target_host}...\n")
scan_ports(target_host, start_port, end_port)
