import matplotlib.pyplot as plt
import os
import math
import numpy as np
import random
from matplotlib.patches import Rectangle

# CONSTANTS
GRAVITY = 9.8
TIME_STEPS = 0.01
BALL_RADIUS = 1.5 

MIN_LAUNCH_ANGLE = 5
MAX_LAUNCH_ANGLE = 85
MIN_LAUNCH_HEIGHT = 2
MAX_LAUNCH_HEIGHT = 15

if not os.path.exists('./causal_data/projectile'):
    os.makedirs('./causal_data/projectile')

def calculate_initial_velocity(angle, height, range_):
    # initial velocity
    v_squared = (range_ * GRAVITY) / np.sin(2 * np.radians(angle))
    v_y = np.sqrt(2 * GRAVITY * height)
    initial_velocity = np.sqrt(v_squared + v_y**2)
    return initial_velocity

def calculate_trajectory(angle, height, initial_velocity):

    angle_rad = np.radians(angle)

    speed_x = initial_velocity * np.cos(angle_rad)
    speed_y = initial_velocity * np.sin(angle_rad)

    time = 0
    x = 3 
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
    
    # Horizontal range based on height
    max_range = 3 * np.sqrt((2 * height) / GRAVITY)
    range_ = np.random.uniform(0.5, 1) * max_range 

    initial_velocity = calculate_initial_velocity(angle_deg, height, range_)
    x_values, y_values = calculate_trajectory(angle_deg, height, initial_velocity)

    fig, ax = plt.subplots(figsize=(96/100, 96/100), dpi=100)

    # Plot trajectory
    ax.plot(x_values, y_values)
    
    # Launching platform
    rect = Rectangle((0, 0), 3, height, linewidth=1, edgecolor='black', facecolor='lightgray')
    ax.add_patch(rect)
    
    # Ball initial position
    ax.add_patch(plt.Circle((3, height), radius=BALL_RADIUS, color='red'))
    
    # Ball final position
    ax.add_patch(plt.Circle((x_values[-1], y_values[-1]), radius=BALL_RADIUS, color='blue'))

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, max(x_values) + 1)
    ax.set_ylim(0, max(y_values) + 1)

    plt.axis('off')

    plt.tight_layout()

    plt.savefig(f'./causal_data/projectile/projectile_{i+1}.png', dpi=96)
    plt.close()
