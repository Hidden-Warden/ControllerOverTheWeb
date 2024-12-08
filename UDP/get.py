import time
import socket
import json

# Define the UDP IP address and port to listen on
UDP_IP = "100.127.238.23"
UDP_PORT = 5000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}")

while True:
    # Receive data from the socket
    data, addr = sock.recvfrom(1024)
    decoded_data = data.decode('utf-8')
    print(f"Received packet from {addr}: {decoded_data}")
    
    try:
        json_data = json.loads(decoded_data)
        if "timestamp" in json_data:
            time_difference = time.time() - json_data["timestamp"]
            print(f"Time between packets: {time_difference * 1000:.2f} ms")
    except json.JSONDecodeError:
        print("Received data is not valid JSON")