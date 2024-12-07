import pygame
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Initialize pygame and joystick
pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# Store previous states
prev_axis = {}
prev_buttons = {}
prev_hats = {}

history = []

# Loop to capture input
try:
	while True:
		for i in range(20):
			pygame.event.pump()  # Update event queue
			# Prepare input data
			input_data = {}
			# Check axes
			for i in range(joystick.get_numaxes()):
				axis = joystick.get_axis(i)
				if i not in prev_axis or abs(axis - prev_axis[i]) >= 0.01:
					input_data[f"axis_{i}"] = axis
					prev_axis[i] = axis
			if input_data:    
				print(input_data)
			history.append({
				'axis_0': input_data.get('axis_0', prev_axis.get(0, 0)),
				'axis_1': input_data.get('axis_1', prev_axis.get(1, 0)),
			})
		# Regenerate graph
		history = history[-1000:]
		df = pd.DataFrame(history)
		# Plot graph & save as image
		plt.plot(df['axis_0'], df['axis_1'])
		plt.savefig('graph.png')
		plt.close()

except KeyboardInterrupt:
    print("Exiting...")