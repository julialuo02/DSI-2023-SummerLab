import matplotlib.pyplot as plt
import os

import matplotlib.image as mpimg
import random
import math
import numpy as np
import pandas as pd

X_LIMIT = 1; Y_LIMIT = 1
FULCRUM_X = 0.5; FULCRUM_Y = 0.4; FULCRUM_HEIGHT = 0.2; FULCRUM_WIDTH = 0.14
FULCRUM_COLOR = 'blue'

SCALE_THICKNESS = 5; SCALE_LEN = 0.8; SCALE_COLOR = 'black'
SCALE_TIP_FACTOR = 10

BALL_RADIUS = 0.03; BALL_SPACING = 0.01
BALL_COLOR_L = 'red'; BALL_COLOR_R = 'green'

if not os.path.exists('./causal_data/scale/'):
    os.makedirs('./causal_data/scale/train/')
    os.makedirs('./causal_data/scale/test/')

def calculate_tipping_angle(num_balls_left, num_balls_right):
    ball_diff = num_balls_left - num_balls_right

    scale_tip_factor = SCALE_TIP_FACTOR
    
    tip_angle = scale_tip_factor * ball_diff

    return tip_angle

def balanced_scale(num_balls_left, num_balls_right):
    fig, ax = plt.subplots(figsize=(96/100, 96/100), dpi=100)

    ax.set_xlim(0,X_LIMIT)
    ax.set_ylim(0,Y_LIMIT)

    fulcrum_x = [FULCRUM_X - FULCRUM_WIDTH / 2, FULCRUM_X + FULCRUM_WIDTH / 2, FULCRUM_X]
    fulcrum_y = [FULCRUM_Y - FULCRUM_HEIGHT, FULCRUM_Y - FULCRUM_HEIGHT, FULCRUM_Y]
    plt.fill(fulcrum_x, fulcrum_y,FULCRUM_COLOR)

    tipping_angle = math.radians(calculate_tipping_angle(num_balls_left, num_balls_right))
    scale_x1 = FULCRUM_X - SCALE_LEN / 2 * math.cos(tipping_angle)
    scale_x2 = FULCRUM_X + SCALE_LEN / 2 * math.cos(tipping_angle)
    scale_y1 = FULCRUM_Y - SCALE_LEN / 2 * math.sin(tipping_angle)
    scale_y2 = FULCRUM_Y + SCALE_LEN / 2 * math.sin(tipping_angle)
    scale_x = [scale_x1, scale_x2]
    scale_y = [scale_y1, scale_y2]
    ax.plot(scale_x, scale_y, linewidth=SCALE_THICKNESS, color=SCALE_COLOR)

    for i in range(num_balls_left):
        x = scale_x1
        y = scale_y1 + BALL_RADIUS + BALL_SPACING + (BALL_RADIUS * 2 + BALL_SPACING) * i
        ball = plt.Circle((x, y), BALL_RADIUS, color=BALL_COLOR_L)
        ax.add_artist(ball)

    for i in range(num_balls_right):
        x = scale_x2
        y = scale_y2 + BALL_RADIUS + BALL_SPACING + (BALL_RADIUS * 2 + BALL_SPACING) * i
        ball = plt.Circle((x, y), BALL_RADIUS, color=BALL_COLOR_R)
        ax.add_artist(ball)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(False)
    plt.axis('off')

    return fig

num_samples_train = 10
num_samples_test = 10

for _ in range(num_samples_train + num_samples_test):
    num_balls_left = random.randint(0, 6)
    num_balls_right = random.randint(0, 6)
    fig = balanced_scale(num_balls_left, num_balls_right)
    # if _ < num_samples_test:
    #     fig.savefig(f'./causal_data/scale/test/scale_{num_balls_left}_{num_balls_right}.png', dpi=96)
    # else:
    #     fig.savefig(f'./causal_data/scale/train/scale_{num_balls_left}_{num_balls_right}.png', dpi=96)
    # plt.clf()

fig = balanced_scale(6,0)
plt.show()
