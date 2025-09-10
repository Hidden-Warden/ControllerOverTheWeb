import os
import sys
import json
import socket
import asyncio
import websockets #pip install websockets
from dotenv import load_dotenv, dotenv_values

load_dotenv()
try:
    UDP_IP = os.getenv("SERVER_IP") or sys.argv[1]
    UDP_PORT = int(os.getenv("SERVER_PORT") or sys.argv[2])
    BRIDGE_PORT = int(os.getenv("BRIDGE_PORT") or sys.argv[3])
except:
    print("Usage: python webserv_bridge.py <server_ip> <server_port> <bridge_port>")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

async def handler(websocket, path):
    async for message in websocket:
        try:
            data = json.loads(message)
            sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
            print(f"Forwarded: {data}")
        except Exception as e:
            print(f"Error: {e}")

start_server = websockets.serve(handler, UDP_IP, BRIDGE_PORT)

print(f"WebSocket server running on ws://{UDP_IP}:{BRIDGE_PORT}, forwarding to UDP {UDP_IP}:{UDP_PORT}")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()