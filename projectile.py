import matplotlib.pyplot as plt
import os
import math
import numpy as np
import random
import matplotlib.colors as mcolors

INITIAL_VELOCITY = 20
GRAVITY = 9.8
TIME_STEPS = 0.01

MIN_LAUNCH_ANGLE = 5
MAX_LAUNCH_ANGLE = 85
MIN_LAUNCH_HEIGHT = 2
MAX_LAUNCH_HEIGHT = 15

if not os.path.exists('./projectile_data'):
    os.makedirs('./projectile_data')

def calculate_trajectory(angle, height):

    angle_rad = np.radians(angle)

    speed_x = INITIAL_VELOCITY * np.cos(angle_rad)
    speed_y = INITIAL_VELOCITY * np.sin(angle_rad)

    time = 0
    x = 0
    y = height

    x_values = [x]
    y_values = [y]

    while y >= 0:
        
        time += TIME_STEPS
        x = speed_x * time
        y = height + speed_y * 0.5 * GRAVITY * (time ** 2)

        x_values.append(x)
        y_values.append(y)

num_samples = 10

for i in range(num_samples):

    angle_deg = np.random.uniform(MIN_LAUNCH_ANGLE, MAX_LAUNCH_ANGLE)
    height = np.random.uniform(MIN_LAUNCH_HEIGHT, MAX_LAUNCH_HEIGHT)

    x_values, y_values = calculate_trajectory(angle_deg, height)
    distance_traveled = max(x_values)

    plt.figure()
    plt.plot(x_values, y_values)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(False)
    plt.axis('off')



