import sys
import json
import time
import socket
import vgamepad as vg
from flask import Flask


# Define the UDP IP address and port to listen on
try:
    ip=sys.args[1]
    port=sys.args[2]
except:
    print("Usage: python client.py <server_ip> <server_port>, or, default ip = 0.0.0.0, port is 50621")
    ip="0.0.0.0"
    port= 50621

UDP_IP = "0.0.0.0"
UDP_PORT = 50621

app = Flask(__name__)

# Initialize the virtual gamepad
gamepads = {
    key: vg.VX360Gamepad()
    for key in range(1, 6)
}

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
        index = json_data.get('controller')
        if "timestamp" in json_data:
            print(time.time())
            time_difference = time.time() - json_data["timestamp"]
            print(f"Time between packets: {time_difference} ms")
        
        ##D-PAD
        if json_data.get('hat_0') == [0, 1]: # D-PAD Up
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        elif json_data.get('hat_0') == [0, -1]: # D-PAD Down
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        elif json_data.get('hat_0') == [-1, 0]: # D-PAD Left
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif json_data.get('hat_0') == [1, 0]: # D-PAD Right
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        elif json_data.get('hat_0') == [-1, 1]: # D-PAD Up-Left
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif json_data.get('hat_0') == [1, 1]: # D-PAD Up-Right
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        elif json_data.get('hat_0') == [-1, -1]: # D-PAD Down-Left
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif json_data.get('hat_0') == [1, -1]: # D-PAD Down-Right
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        elif json_data.get('hat_0') == [0, 0]:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        ## End D-PAD

        ## BUTTONS
        if json_data.get('button_0') == 1: # Button 0: A button
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        elif json_data.get('button_0') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        if json_data.get('button_1') == 1: # Button 1: B button
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        elif json_data.get('button_1') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        if json_data.get('button_2') == 1: # Button 2: X button
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        elif json_data.get('button_2') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        if json_data.get('button_3') == 1: # Button 3: Y button
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        elif json_data.get('button_3') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        ## End BUTTONS
        ## Start and Back buttons
        if json_data.get('button_6') == 1: # Button 6: Back button
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        elif json_data.get('button_6') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        if json_data.get('button_7') == 1: # Button 7: Start button
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        elif json_data.get('button_7') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        ## End Start and Back buttons

        ## Shoulders
        if json_data.get('button_4') == 1: # Button 4: Left Shoulder
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        elif json_data.get('button_4') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        if json_data.get('button_5') == 1: # Button 5: Right Shoulder
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        elif json_data.get('button_5') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        ## End Shoulders
        ## JoySticks Press
        if json_data.get('button_8') == 1: # Button 8: Left Stick Press
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        elif json_data.get('button_8') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        if json_data.get('button_9') == 1: # Button 9: Right Stick Press
            gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        elif json_data.get('button_9') == 0:
            gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        ## End JoySticks Press

        ##Triggers
        if json_data.get('axis_4') is not None and json_data.get('axis_4') > 0:
            gamepads[index].left_trigger(value=255)
        elif json_data.get('axis_4') == -1.0:
            gamepads[index].left_trigger(value=0)
        if json_data.get('axis_5') is not None and json_data.get('axis_5') > 0:
            gamepads[index].right_trigger(value=255)
        elif json_data.get('axis_5') == -1.0:
            gamepads[index].right_trigger(value=0)

        # Left stick: X-axis and Y-axis
        left_joysticks = [
            (0, 0)
            for _ in range(len(gamepads))
        ]

        # Get the new joystick data
        new_left_x = json_data.get('axis_0', left_joysticks[index][0])
        new_left_y = json_data.get('axis_1', left_joysticks[index][1])

        # Update only if new values are significant
        if abs(new_left_x) > 0.02 or abs(new_left_y) > 0.02:
            left_joysticks[index] = (new_left_x, new_left_y)

        # Apply the joystick state
        gamepads[index].left_joystick(
            x_value=int(left_joysticks[index][0] * 32767),
            y_value=int(left_joysticks[index][1] * -32767)
        )

        # Debugging output
        print('Left Joystick:', left_joysticks[index])

        # Right stick: X-axis and Y-axis
        right_joysticks = [
            (0, 0)
            for _ in range(len(gamepads))
        ]

        # Get the new joystick data
        new_right_x = json_data.get('axis_2', right_joysticks[index][0])
        new_right_y = json_data.get('axis_3', right_joysticks[index][1])

        # Update only if new values are significant
        if abs(new_right_x) > 0.02 or abs(new_right_y) > 0.02:
            right_joysticks[index] = (new_right_x, new_right_y)

        # Apply the joystick state
        gamepads[index].right_joystick(
            x_value=int(right_joysticks[index][0] * 32767),
            y_value=int(right_joysticks[index][1] * -32767)
        )

        # Debugging output
        print('Right Joystick:', right_joysticks[index])

        # Update the gamepad state
        gamepads[index].update()  
    except json.JSONDecodeError:
        print("Received data is not valid JSON")