from flask import Flask, request, jsonify
import vgamepad as vg
import time

app = Flask(__name__)

# Initialize the virtual gamepad
gamepads = {
    key: vg.VX360Gamepad()
    for key in range(1, 5)
}

@app.route('/controller-input', methods=['POST'])
def controller_input():
    data = request.json
    print(f"Received Data: {data}, {type(data)}")  # Debugging

    index = data.get('controller')

    if data.get('button_0') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    else: #if data.get('button_0') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    # Button 1: X button
    if data.get('button_2') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    else: #if data.get('button_2') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    # Button 2: Y button
    if data.get('button_3') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    else: #if data.get('button_3') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

    # Button 3: B button
    if data.get('button_1') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    else: #if data.get('button_1') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    # D-pad: Up
    if data.get('hat_0') == [0, 1]:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    elif data.get('hat_0') == [0, 0]:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

    # D-pad: Down
    if data.get('hat_0') == [0, -1]:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    elif data.get('hat_0') == [0, 0]:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    
    # D-pad: Left
    if data.get('hat_0') == [-1, 0]:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    elif data.get('hat_0') == [0, 0]:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    
    # D-pad: Right
    if data.get('hat_0') == [1, 0]:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    elif data.get('hat_0') == [0, 0]:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

    # Shoulder buttons: Left
    if data.get('button_4') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    else: #if data.get('button_4') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    
    # Shoulder buttons: Right
    if data.get('button_5') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    else: #if data.get('button_5') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

    # Start button
    if data.get('button_7') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    else: #if data.get('button_7') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    
    # Back button
    if data.get('button_6') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    else: #if data.get('button_6') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

    # Left stick: Press
    if data.get('button_8') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    else: #if data.get('button_8') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    
    # Right stick: Press
    if data.get('button_9') == 1:
        gamepads[index].press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    else: #if data.get('button_9') == 0:
        gamepads[index].release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    
    # Left trigger
    axis_4_value = data.get('axis_4')
    if axis_4_value is not None and axis_4_value > 0:
        gamepads[index].left_trigger(value=int(axis_4_value * 255))
    else:
        gamepads[index].left_trigger(value=0)
    
    # Right trigger
    axis_5_value = data.get('axis_5')
    if axis_5_value is not None and axis_5_value > 0:
        gamepads[index].right_trigger(value=int(axis_5_value * 255))
    else:
        gamepads[index].right_trigger(value=0)

    # Left stick: X-axis and Y-axis
    left_joysticks = [
        (0, 0)
        for _ in range(len(gamepads))
    ]
    left_joysticks[index] = (
        data.get('axis_0', left_joysticks[index][0]),
        data.get('axis_1', left_joysticks[index][1]),
    )
    gamepads[index].left_joystick(x_value=int(left_joysticks[index][0] * 32767), y_value=int(left_joysticks[index][1] * -32767))

    # Right stick: X-axis and Y-axis
    right_joysticks = [
        (0, 0)
        for _ in range(len(gamepads))
    ]
    right_joysticks[index] = (
        data.get('axis_2', right_joysticks[index][0]),
        data.get('axis_3', right_joysticks[index][1]),
    )
    gamepads[index].right_joystick(x_value=int(right_joysticks[index][0] * 32767), y_value=int(right_joysticks[index][1] * -32767))

    # Update the gamepad state
    gamepads[index].update()

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
