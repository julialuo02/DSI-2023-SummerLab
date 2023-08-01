import matplotlib.pyplot as plt
import os
import math
import numpy as np
import random
from matplotlib.patches import Rectangle

INITIAL_VELOCITY = 20
GRAVITY = 9.8
TIME_STEPS = 0.01
BALL_RADIUS = 1.5  # Set the ball size

MIN_LAUNCH_ANGLE = 5
MAX_LAUNCH_ANGLE = 85
MIN_LAUNCH_HEIGHT = 2
MAX_LAUNCH_HEIGHT = 15

if not os.path.exists('./causal_data/projectile'):
    os.makedirs('./causal_data/projectile')

def calculate_trajectory(angle, height):

    angle_rad = np.radians(angle)

    speed_x = INITIAL_VELOCITY * np.cos(angle_rad)
    speed_y = INITIAL_VELOCITY * np.sin(angle_rad)

    time = 0
    x = 3  # Launch from the top right corner of the rectangle
    y = height

    x_values = [x]
    y_values = [y]

    while y >= 0:
        
        time += TIME_STEPS
        x = 3 + speed_x * time
        y = height + speed_y * time - 0.5 * GRAVITY * (time ** 2)

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

num_samples = 10

for i in range(num_samples):

    angle_deg = np.random.uniform(MIN_LAUNCH_ANGLE, MAX_LAUNCH_ANGLE)
    height = np.random.uniform(MIN_LAUNCH_HEIGHT, MAX_LAUNCH_HEIGHT)

    x_values, y_values = calculate_trajectory(angle_deg, height)

    fig, ax = plt.subplots(figsize=(96/100, 96/100), dpi=100)

    # Plot the trajectory
    ax.plot(x_values, y_values)
    
    # Draw a rectangle as the launching platform
    rect = Rectangle((0, 0), 3, height, linewidth=1, edgecolor='black', facecolor='lightgray')
    ax.add_patch(rect)
    
    # Add a ball as a circle at the initial position (top right corner of the rectangle)
    ax.add_patch(plt.Circle((3, height), radius=BALL_RADIUS, color='red'))
    
    # Add a ball as a circle at the final position
    ax.add_patch(plt.Circle((x_values[-1], y_values[-1]), radius=BALL_RADIUS, color='blue'))

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, max(x_values) + 1)
    ax.set_ylim(0, max(y_values) + 1)

    # Remove the black square border
    plt.axis('off')

    plt.tight_layout()

    plt.savefig(f'./causal_data/projectile/projectile_{i+1}.png', dpi=96)
    plt.close()
