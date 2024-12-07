from flask import Flask, request, jsonify
import vgamepad as vg
import time

app = Flask(__name__)

# Initialize the virtual gamepad
gamepad = vg.VX360Gamepad()

@app.route('/controller-input', methods=['POST'])
def controller_input():
    data = request.json
    print(f"Received Data: {data}, {type(data)}")  # Debugging

    # Check the state of each button and perform actions accordingly
    if data:
        # Button 0: A button
        if data.get('button_0') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        elif data.get('button_0') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

        # Button 1: X button
        if data.get('button_2') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        elif data.get('button_2') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        # Button 2: Y button
        if data.get('button_3') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        elif data.get('button_3') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

        # Button 3: B button
        if data.get('button_1') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        elif data.get('button_1') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        # D-pad: Up
        if data.get('hat_0') == [0, 1]:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        elif data.get('hat_0') == [0, 0]:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

        # D-pad: Down
        if data.get('hat_0') == [0, -1]:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        elif data.get('hat_0') == [0, 0]:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        
        # D-pad: Left
        if data.get('hat_0') == [-1, 0]:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif data.get('hat_0') == [0, 0]:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        
        # D-pad: Right
        if data.get('hat_0') == [1, 0]:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        elif data.get('hat_0') == [0, 0]:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

        # Shoulder buttons: Left
        if data.get('button_4') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        elif data.get('button_4') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        
        # Shoulder buttons: Right
        if data.get('button_5') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        elif data.get('button_5') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

        # Start button
        if data.get('button_7') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        elif data.get('button_7') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        
        # Back button
        if data.get('button_6') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        elif data.get('button_6') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

        # Left stick: Press
        if data.get('button_8') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        elif data.get('button_8') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        
        # Right stick: Press
        if data.get('button_9') == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        elif data.get('button_9') == 0:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        
        # Left trigger
        axis_4_value = data.get('axis_4')
        if axis_4_value is not None and axis_4_value > 0:
            gamepad.left_trigger(value=int(axis_4_value * 255))
        else:
            gamepad.left_trigger(value=0)
        
        # Right trigger
        axis_5_value = data.get('axis_5')
        if axis_5_value is not None and axis_5_value > 0:
            gamepad.right_trigger(value=int(axis_5_value * 255))
        else:
            gamepad.right_trigger(value=0)

        # Update the gamepad state
        gamepad.update()

    # Small delay to simulate human-like interaction
    time.sleep(0.01)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
