import socket
import time
import json

UDP_IP = "100.127.238.23" # Replace with the target IP address
UDP_PORT = 5000       # Replace with the target port

data = {}
data['timestamp'] = time.time()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    data_json = json.dumps(data)
    sock.sendto(data_json.encode(), (UDP_IP, UDP_PORT))
    print(f"Sent UDP packet to {UDP_IP}:{UDP_PORT}: {data_json}")
except Exception as e:
    print(f"Failed to send UDP packet: {e}")
finally:
    sock.close()