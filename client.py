#pip install websockets
#pip install requests

import pygame
import requests

# Initialize pygame and joystick
pygame.init()
pygame.joystick.init()

controller_id=int(input("N° de controller: [1-4] ? "))
if controller_id < 1 or controller_id > 4:
    print("Invalid controller ID!")
    exit()

if pygame.joystick.get_count() == 0:
    print("No joysticks connected!")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick Name: {joystick.get_name()}")

# Store previous states
prev_axis = {}
prev_buttons = {}
prev_hats = {}

# Server details
SERVER_URL = "http://100.127.238.23:5000/controller-input"
#SERVER_URL = "http://195.15.213.250:5000/controller-input-1"

# Function to send data to the server
def send_to_server(data):
    try:
        response = requests.post(SERVER_URL, json=data)
        print(f"Server response: {response.json()}")
    except Exception as e:
        print(f"Error sending data: {e}")

# Loop to capture input
try:
    while True:
        pygame.event.pump()  # Update event queue

        # Prepare input data
        input_data = {}

        # Check axes
        for i in range(joystick.get_numaxes()):
            axis = joystick.get_axis(i)
            if i not in prev_axis or abs(axis - prev_axis[i]) >= 0.01:
                input_data[f"axis_{i}"] = axis
                prev_axis[i] = axis

        # Check buttons
        for i in range(joystick.get_numbuttons()):
            button = joystick.get_button(i)
            if i not in prev_buttons or button != prev_buttons[i]:
                input_data[f"button_{i}"] = button
                prev_buttons[i] = button

        # Check hats (D-pad)
        for i in range(joystick.get_numhats()):
            hat = joystick.get_hat(i)
            if i not in prev_hats or hat != prev_hats[i]:
                input_data[f"hat_{i}"] = hat
                prev_hats[i] = hat

        # Send data if there are changes
        if input_data:
            input_data[f"controller"] = controller_id
            send_to_server(input_data)

except KeyboardInterrupt:
    print("Exiting...")

import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")

start_server = websockets.serve(handler, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
