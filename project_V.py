"""
1. The code imports the necessary modules: `socket` for creating network sockets and `sys` for system-specific parameters and functions.

2. The `scan_ports()` function is defined to scan a range of ports on a target host:
   - It iterates over the range of ports from the start port to the end port.
   - For each port, it creates a socket object and sets a timeout of 1 second.
   - It tries to connect to the target host and port using `sock.connect_ex()`.
   - If the connection is successful (return value of 0), it prints that the port is open. Otherwise, it prints that the port is closed.
   - It closes the socket connection.

3. The example usage section sets the target host IP address, start port, and end port.

4. It prints a message indicating the range of ports being scanned and the target host.

5. The `scan_ports()` function is called with the provided parameters.

The code scans the specified range of ports on the target host by attempting to establish a connection to each port. It then prints whether each port is open or closed based on the connection result.

"""

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
