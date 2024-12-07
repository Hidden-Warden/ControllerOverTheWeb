from flask import Flask, request, jsonify
import vgamepad as vg
import time

app = Flask(__name__)

# Initialize the virtual gamepad
gamepad1 = vg.VX360Gamepad()
gamepad2 = vg.VX360Gamepad()
gamepad3 = vg.VX360Gamepad()
gamepad4 = vg.VX360Gamepad()

@app.route('/controller-input', methods=['POST'])
def controller_input():
    data = request.json
    print(f"Received Data: {data}, {type(data)}")  # Debugging

    if data.get('controller') == 1:
        if data.get('button_0') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        elif data.get('button_0') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

        # Button 1: X button
        if data.get('button_2') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        elif data.get('button_2') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        # Button 2: Y button
        if data.get('button_3') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        elif data.get('button_3') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

        # Button 3: B button
        if data.get('button_1') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        elif data.get('button_1') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        # D-pad: Up
        if data.get('hat_0') == [0, 1]:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        elif data.get('hat_0') == [0, 0]:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

        # D-pad: Down
        if data.get('hat_0') == [0, -1]:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        elif data.get('hat_0') == [0, 0]:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        
        # D-pad: Left
        if data.get('hat_0') == [-1, 0]:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif data.get('hat_0') == [0, 0]:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        
        # D-pad: Right
        if data.get('hat_0') == [1, 0]:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        elif data.get('hat_0') == [0, 0]:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

        # Shoulder buttons: Left
        if data.get('button_4') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        elif data.get('button_4') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        
        # Shoulder buttons: Right
        if data.get('button_5') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        elif data.get('button_5') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

        # Start button
        if data.get('button_7') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        elif data.get('button_7') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        
        # Back button
        if data.get('button_6') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        elif data.get('button_6') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

        # Left stick: Press
        if data.get('button_8') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        elif data.get('button_8') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        
        # Right stick: Press
        if data.get('button_9') == 1:
            gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        elif data.get('button_9') == 0:
            gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        
        # Left trigger
        axis_4_value = data.get('axis_4')
        if axis_4_value is not None and axis_4_value > 0:
            gamepad1.left_trigger(value=int(axis_4_value * 255))
        else:
            gamepad1.left_trigger(value=0)
        
        # Right trigger
        axis_5_value = data.get('axis_5')
        if axis_5_value is not None and axis_5_value > 0:
            gamepad1.right_trigger(value=int(axis_5_value * 255))
        else:
            gamepad1.right_trigger(value=0)

        # Left stick: X-axis and Y-axis
        axis_0_value = data.get('axis_0', 0)
        axis_1_value = data.get('axis_1', 0)
        gamepad1.left_joystick(x_value=int(axis_0_value * 32767), y_value=int(axis_1_value * -32767))

        # Right stick: X-axis and Y-axis
        axis_2_value = data.get('axis_2', 0)
        axis_3_value = data.get('axis_3', 0)
        gamepad1.right_joystick(x_value=int(axis_2_value * 32767), y_value=int(axis_3_value * -32767))

        # Update the gamepad state
        gamepad1.update()

    if data.get('controller') == 2:
        if data.get('button_0') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        elif data.get('button_0') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

        # Button 1: X button
        if data.get('button_2') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        elif data.get('button_2') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        # Button 2: Y button
        if data.get('button_3') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        elif data.get('button_3') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

        # Button 3: B button
        if data.get('button_1') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        elif data.get('button_1') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        # D-pad: Up
        if data.get('hat_0') == [0, 1]:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        elif data.get('hat_0') == [0, 0]:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

        # D-pad: Down
        if data.get('hat_0') == [0, -1]:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        elif data.get('hat_0') == [0, 0]:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        
        # D-pad: Left
        if data.get('hat_0') == [-1, 0]:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif data.get('hat_0') == [0, 0]:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        
        # D-pad: Right
        if data.get('hat_0') == [1, 0]:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        elif data.get('hat_0') == [0, 0]:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

        # Shoulder buttons: Left
        if data.get('button_4') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        elif data.get('button_4') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        
        # Shoulder buttons: Right
        if data.get('button_5') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        elif data.get('button_5') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

        # Start button
        if data.get('button_7') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        elif data.get('button_7') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        
        # Back button
        if data.get('button_6') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        elif data.get('button_6') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

        # Left stick: Press
        if data.get('button_8') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        elif data.get('button_8') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        
        # Right stick: Press
        if data.get('button_9') == 1:
            gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        elif data.get('button_9') == 0:
            gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        
        # Left trigger
        axis_4_value = data.get('axis_4')
        if axis_4_value is not None and axis_4_value > 0:
            gamepad2.left_trigger(value=int(axis_4_value * 255))
        else:
            gamepad2.left_trigger(value=0)
        
        # Right trigger
        axis_5_value = data.get('axis_5')
        if axis_5_value is not None and axis_5_value > 0:
            gamepad2.right_trigger(value=int(axis_5_value * 255))
        else:
            gamepad2.right_trigger(value=0)

        # Left stick: X-axis and Y-axis
        axis_0_value = data.get('axis_0', 0)
        axis_1_value = data.get('axis_1', 0)
        gamepad2.left_joystick(x_value=int(axis_0_value * 32767), y_value=int(axis_1_value * -32767))

        # Right stick: X-axis and Y-axis
        axis_2_value = data.get('axis_2', 0)
        axis_3_value = data.get('axis_3', 0)
        gamepad2.right_joystick(x_value=int(axis_2_value * 32767), y_value=int(axis_3_value * -32767))

        # Update the gamepad state
        gamepad2.update()

    if data.get('controller') == 3:
        if data.get('button_0') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        elif data.get('button_0') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

        # Button 1: X button
        if data.get('button_2') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        elif data.get('button_2') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        # Button 2: Y button
        if data.get('button_3') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        elif data.get('button_3') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

        # Button 3: B button
        if data.get('button_1') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        elif data.get('button_1') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        # D-pad: Up
        if data.get('hat_0') == [0, 1]:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        elif data.get('hat_0') == [0, 0]:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

        # D-pad: Down
        if data.get('hat_0') == [0, -1]:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        elif data.get('hat_0') == [0, 0]:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        
        # D-pad: Left
        if data.get('hat_0') == [-1, 0]:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif data.get('hat_0') == [0, 0]:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        
        # D-pad: Right
        if data.get('hat_0') == [1, 0]:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        elif data.get('hat_0') == [0, 0]:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

        # Shoulder buttons: Left
        if data.get('button_4') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        elif data.get('button_4') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        
        # Shoulder buttons: Right
        if data.get('button_5') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        elif data.get('button_5') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

        # Start button
        if data.get('button_7') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        elif data.get('button_7') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        
        # Back button
        if data.get('button_6') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        elif data.get('button_6') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

        # Left stick: Press
        if data.get('button_8') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        elif data.get('button_8') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        
        # Right stick: Press
        if data.get('button_9') == 1:
            gamepad3.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        elif data.get('button_9') == 0:
            gamepad3.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        
        # Left trigger
        axis_4_value = data.get('axis_4')
        if axis_4_value is not None and axis_4_value > 0:
            gamepad3.left_trigger(value=int(axis_4_value * 255))
        else:
            gamepad3.left_trigger(value=0)
        
        # Right trigger
        axis_5_value = data.get('axis_5')
        if axis_5_value is not None and axis_5_value > 0:
            gamepad3.right_trigger(value=int(axis_5_value * 255))
        else:
            gamepad3.right_trigger(value=0)

        # Left stick: X-axis and Y-axis
        axis_0_value = data.get('axis_0', 0)
        axis_1_value = data.get('axis_1', 0)
        gamepad3.left_joystick(x_value=int(axis_0_value * 32767), y_value=int(axis_1_value * -32767))

        # Right stick: X-axis and Y-axis
        axis_2_value = data.get('axis_2', 0)
        axis_3_value = data.get('axis_3', 0)
        gamepad3.right_joystick(x_value=int(axis_2_value * 32767), y_value=int(axis_3_value * -32767))

        # Update the gamepad state
        gamepad3.update()

    if data.get('controller') == 4:
        if data.get('button_0') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        elif data.get('button_0') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

        # Button 1: X button
        if data.get('button_2') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        elif data.get('button_2') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        # Button 2: Y button
        if data.get('button_3') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        elif data.get('button_3') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

        # Button 3: B button
        if data.get('button_1') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        elif data.get('button_1') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        # D-pad: Up
        if data.get('hat_0') == [0, 1]:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        elif data.get('hat_0') == [0, 0]:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

        # D-pad: Down
        if data.get('hat_0') == [0, -1]:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        elif data.get('hat_0') == [0, 0]:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        
        # D-pad: Left
        if data.get('hat_0') == [-1, 0]:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif data.get('hat_0') == [0, 0]:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        
        # D-pad: Right
        if data.get('hat_0') == [1, 0]:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        elif data.get('hat_0') == [0, 0]:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

        # Shoulder buttons: Left
        if data.get('button_4') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        elif data.get('button_4') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        
        # Shoulder buttons: Right
        if data.get('button_5') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        elif data.get('button_5') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

        # Start button
        if data.get('button_7') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        elif data.get('button_7') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        
        # Back button
        if data.get('button_6') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        elif data.get('button_6') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

        # Left stick: Press
        if data.get('button_8') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        elif data.get('button_8') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        
        # Right stick: Press
        if data.get('button_9') == 1:
            gamepad4.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        elif data.get('button_9') == 0:
            gamepad4.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        
        # Left trigger
        axis_4_value = data.get('axis_4')
        if axis_4_value is not None and axis_4_value > 0:
            gamepad4.left_trigger(value=int(axis_4_value * 255))
        else:
            gamepad4.left_trigger(value=0)
        
        # Right trigger
        axis_5_value = data.get('axis_5')
        if axis_5_value is not None and axis_5_value > 0:
            gamepad4.right_trigger(value=int(axis_5_value * 255))
        else:
            gamepad4.right_trigger(value=0)

        # Left stick: X-axis and Y-axis
        axis_0_value = data.get('axis_0', 0)
        axis_1_value = data.get('axis_1', 0)
        gamepad4.left_joystick(x_value=int(axis_0_value * 32767), y_value=int(axis_1_value * -32767))

        # Right stick: X-axis and Y-axis
        axis_2_value = data.get('axis_2', 0)
        axis_3_value = data.get('axis_3', 0)
        gamepad4.right_joystick(x_value=int(axis_2_value * 32767), y_value=int(axis_3_value * -32767))

        # Update the gamepad state
        gamepad4.update()
    # Small delay to simulate human-like interaction
    time.sleep(0.01)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
