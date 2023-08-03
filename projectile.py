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
SPACING = 0.5

PLATFORM_WIDTH = 5
MIN_LAUNCH_ANGLE = 0
MAX_LAUNCH_ANGLE = 85
MIN_LAUNCH_HEIGHT = BALL_RADIUS + SPACING
MAX_LAUNCH_HEIGHT = 15

VELOCITY = 15

X_LIMIT = 40
Y_LIMIT = 40

if not os.path.exists('./causal_data/projectile'):
    os.makedirs('./causal_data/projectile')

def calculate_trajectory(angle, height, initial_velocity):

    angle_rad = np.radians(angle)

    speed_x = initial_velocity * np.cos(angle_rad)
    speed_y = initial_velocity * np.sin(angle_rad)

    time = 0
    x = PLATFORM_WIDTH / 2 
    y = height

    x_values = [x]
    y_values = [y]

    while y >= BALL_RADIUS + SPACING:
        
        time += TIME_STEPS
        x = PLATFORM_WIDTH / 2 + speed_x * time
        y = height + speed_y * time - 0.5 * GRAVITY * (time ** 2)

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


def projectile(height, angle):
    fig, ax = plt.subplots(figsize=(96/100, 96/100), dpi=100)

    ax.set_xlim(0,X_LIMIT)
    ax.set_ylim(0,Y_LIMIT)

    # Launching platform
    rect = Rectangle((0, 0), PLATFORM_WIDTH, height, linewidth=1, edgecolor='black', facecolor='lightgray')
    ax.add_patch(rect)
 
    x_values, y_values = calculate_trajectory(angle, height, VELOCITY)
    ax.plot(x_values, y_values)

    # Ball final position
    ax.add_patch(plt.Circle((x_values[-1], y_values[-1]), radius=BALL_RADIUS, color='blue'))


    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(False)
    plt.axis('off')

    return fig

num_samples = 100
for i in range(num_samples):

    angle_deg = np.random.uniform(MIN_LAUNCH_ANGLE, MAX_LAUNCH_ANGLE)
    height = np.random.uniform(MIN_LAUNCH_HEIGHT, MAX_LAUNCH_HEIGHT)

    fig = projectile(height, angle_deg)
    
    plt.savefig(f'./causal_data/projectile/projectile_{height:.1f}_{angle_deg:.0f}.png', dpi=96)
    plt.close()

# fig = projectile(height=50, angle=45)
# plt.show()