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
        
        
