import pygame
import requests
from flask import Flask, request, jsonify

# Initialize pygame and joystick
pygame.init()
pygame.joystick.init()

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

app = Flask(__name__)

@app.route('/receive-input', methods=['POST'])
def receive_input():
    data = request.json
    input_number = data.get('inputNumber')
    if input_number:
        # Process the input number (1 to 4)
        print(f"Received input number: {input_number}")
        # Here you can add code to handle the input and control the joystick
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Invalid input'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)