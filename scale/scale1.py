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

SCALE_THICKNESS = 3; SCALE_LEN = 0.8; SCALE_COLOR = 'black'
SCALE_TIP_FACTOR = 8

BALL_RADIUS = 0.03; BALL_SPACING = 0.01
BALL_COLOR_L = 'red'; BALL_COLOR_R = 'green'

TRAY_SUPPORT_HEIGHT = 0.15
TRAY_LENGTH = 0.2

if not os.path.exists('./causal_data/scale/'):
    os.makedirs('./causal_data/scale/train/')
    os.makedirs('./causal_data/scale/test/')

def calculate_tipping_angle(num_balls_left, num_balls_right):
    ball_diff = num_balls_left - num_balls_right

    scale_tip_factor = SCALE_TIP_FACTOR
    
    tip_angle = scale_tip_factor * ball_diff

    return tip_angle

def draw_balls(ax, num, location, color):
    location_x, location_y = location

    if num >= 1:
        x = location_x
        y = location_y + BALL_RADIUS + BALL_SPACING + (BALL_RADIUS * 2 + BALL_SPACING) * 0 + \
            TRAY_SUPPORT_HEIGHT + BALL_SPACING
        ball = plt.Circle((x, y), BALL_RADIUS, color=color)
        ax.add_artist(ball)

    if num >= 2:
        x = location_x - BALL_RADIUS * 2 - BALL_SPACING
        y = location_y + BALL_RADIUS + BALL_SPACING + (BALL_RADIUS * 2 + BALL_SPACING) * 0 + \
            TRAY_SUPPORT_HEIGHT + BALL_SPACING
        ball = plt.Circle((x, y), BALL_RADIUS, color=color)
        ax.add_artist(ball)

    if num >= 3:
        x = location_x + BALL_RADIUS * 2 + BALL_SPACING
        y = location_y + BALL_RADIUS + BALL_SPACING + (BALL_RADIUS * 2 + BALL_SPACING) * 0 + \
            TRAY_SUPPORT_HEIGHT + BALL_SPACING
        ball = plt.Circle((x, y), BALL_RADIUS, color=color)
        ax.add_artist(ball)

    if num >= 4:
        x = location_x 
        y = location_y + BALL_RADIUS + BALL_SPACING + (BALL_RADIUS * 2 + BALL_SPACING) * 1 + \
            TRAY_SUPPORT_HEIGHT + BALL_SPACING
        ball = plt.Circle((x, y), BALL_RADIUS, color=color)
        ax.add_artist(ball)
    
    if num >= 5:
        x = location_x - BALL_RADIUS * 2 - BALL_SPACING
        y = location_y + BALL_RADIUS + BALL_SPACING + (BALL_RADIUS * 2 + BALL_SPACING) * 1 + \
            TRAY_SUPPORT_HEIGHT + BALL_SPACING
        ball = plt.Circle((x, y), BALL_RADIUS, color=color)
        ax.add_artist(ball)

    if num >= 6:
        x = location_x + BALL_RADIUS * 2 + BALL_SPACING
        y = location_y + BALL_RADIUS + BALL_SPACING + (BALL_RADIUS * 2 + BALL_SPACING) * 1 + \
            TRAY_SUPPORT_HEIGHT + BALL_SPACING
        ball = plt.Circle((x, y), BALL_RADIUS, color=color)
        ax.add_artist(ball)


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
    tray_support1_x = [scale_x1, scale_x1]
    tray_support1_y = [scale_y1, scale_y1 + TRAY_SUPPORT_HEIGHT]
    ax.plot(tray_support1_x, tray_support1_y, linewidth=SCALE_THICKNESS, color=SCALE_COLOR)
    tray1_x = [scale_x1-TRAY_LENGTH/2, scale_x1+TRAY_LENGTH/2 ]
    tray1_y = [scale_y1+TRAY_SUPPORT_HEIGHT, scale_y1+TRAY_SUPPORT_HEIGHT]
    ax.plot(tray1_x, tray1_y, linewidth=SCALE_THICKNESS, color=SCALE_COLOR)

    tray_support2_x = [scale_x2, scale_x2]
    tray_support2_y = [scale_y2, scale_y2 + TRAY_SUPPORT_HEIGHT]
    ax.plot(tray_support2_x, tray_support2_y, linewidth=SCALE_THICKNESS, color=SCALE_COLOR)
    tray2_x = [scale_x2-TRAY_LENGTH/2, scale_x2+TRAY_LENGTH/2 ]
    tray2_y = [scale_y2+TRAY_SUPPORT_HEIGHT, scale_y2+TRAY_SUPPORT_HEIGHT]
    ax.plot(tray2_x, tray2_y, linewidth=SCALE_THICKNESS, color=SCALE_COLOR)
    
    draw_balls(ax, num_balls_left, (scale_x1, scale_y1), BALL_COLOR_L)
    draw_balls(ax, num_balls_right, (scale_x2, scale_y2), BALL_COLOR_R)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(False)
    plt.axis('off')

    return fig

num_samples_train = 100
num_samples_test = 100

for _ in range(num_samples_train + num_samples_test):
    num_balls_left = random.randint(0, 6)
    num_balls_right = random.randint(0, 6)
    fig = balanced_scale(num_balls_left, num_balls_right)
    if _ < num_samples_test:
        fig.savefig(f'./causal_data/scale/test/scale_{num_balls_left}_{num_balls_right}.png', dpi=96)
    else:
        fig.savefig(f'./causal_data/scale/train/scale_{num_balls_left}_{num_balls_right}.png', dpi=96)
    plt.clf()

# fig = balanced_scale(6,2)
# plt.show()