import matplotlib.pyplot as plt
import os
import math
import numpy as np
import random
import matplotlib.colors as mcolors

random.seed(42)

SWITCH_RADIUS = 0.3
SWITCH_COLOR = 'white'  # White switch
DIAL_ARROW_LENGTH = 0.2
DIAL_COLOR = 'blue'  # Blue dial
LIGHT_BULB_RADIUS = 0.15
LIGHT_BULB_STEM_HEIGHT = 0.08
LIGHT_BULB_STEM_WIDTH = 0.04
LIGHT_BULB_BOTTOM_HEIGHT = 0.03

# Custom colormap with 100 shades of yellow
num_colors = 100
yellow_colors = mcolors.LinearSegmentedColormap.from_list('yellow_colors', ['#FFFF00', '#FFCC00'], N=num_colors)

def light_switch_and_bulb(position):
    fig, ax = plt.subplots(figsize=(96/100, 96/100), dpi=100, facecolor='#333333')  # Facecolor - dark grey

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Light switch (white semicircle)
    theta = np.linspace(0, np.pi, 100)
    switch_x = 0.3 + SWITCH_RADIUS * np.cos(theta)
    switch_y = 0.7 + SWITCH_RADIUS * np.sin(theta)
    ax.fill_between(switch_x, switch_y, 0.7, color=SWITCH_COLOR)

    # Dial arrow (blue)
    dial_angle = position * np.pi
    dial_angle_wrapped = dial_angle % (2 * np.pi)
    if dial_angle_wrapped > np.pi:
        dial_angle_wrapped -= 2 * np.pi
    arrow_x = 0.3 + (SWITCH_RADIUS - 0.05) * np.cos(dial_angle_wrapped)  # Move arrow closer to center
    arrow_y = 0.7 + (SWITCH_RADIUS - 0.05) * np.sin(dial_angle_wrapped)
    ax.arrow(0.3, 0.7, arrow_x - 0.3, arrow_y - 0.7, head_width=0.02, head_length=0.02, fc=DIAL_COLOR, ec=DIAL_COLOR)

    # Light bulb (gradually turning yellow and transparent)
    normalized_position = (180 - abs(dial_angle_wrapped) * 180 / np.pi) / 180.0  # Normalize position to range [0, 1]
    transparency = 1.0 - normalized_position  # Linear interpolation between 0 and 1
    color_interpolation = yellow_colors(position)[:3]  # Extract RGB values (0-1 range)
    bulb_color = (*color_interpolation, transparency)  # Combine with alpha (transparency)
    bulb_x = 0.8
    bulb_y = 0.2
    bulb = plt.Circle((bulb_x, bulb_y), LIGHT_BULB_RADIUS, color=bulb_color, edgecolor='white', linewidth=1.5)
    ax.add_artist(bulb)

    # Light bulb highlights and shading
    num_highlights = 5
    highlight_radius = 0.02
    highlight_positions = np.linspace(bulb_y + 0.03, bulb_y + 0.06, num_highlights)
    for pos in highlight_positions:
        highlight = plt.Circle((bulb_x, pos), highlight_radius, color='white', alpha=0.7)
        ax.add_artist(highlight)

    shading = plt.Circle((bulb_x, bulb_y - 0.04), LIGHT_BULB_RADIUS, color='black', alpha=0.15)
    ax.add_artist(shading)

    # Light bulb stem
    stem_x = bulb_x
    stem_y = bulb_y - LIGHT_BULB_RADIUS
    stem = plt.Rectangle((stem_x - LIGHT_BULB_STEM_WIDTH / 2, stem_y), LIGHT_BULB_STEM_WIDTH, LIGHT_BULB_STEM_HEIGHT,
                         color='black', edgecolor='black')
    ax.add_artist(stem)

    # Light bulb bottom (grey rectangle with patterned stripes)
    bottom_x = bulb_x - LIGHT_BULB_RADIUS
    bottom_y = bulb_y - LIGHT_BULB_RADIUS - LIGHT_BULB_BOTTOM_HEIGHT
    bottom = plt.Rectangle((bottom_x, bottom_y), 2 * LIGHT_BULB_RADIUS, LIGHT_BULB_BOTTOM_HEIGHT,
                           color='grey', hatch='///', edgecolor='black')
    ax.add_artist(bottom)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(False)
    plt.axis('off')

    return fig

num_samples_to_save = 181

if not os.path.exists('./causal_data/light_switch/'):
    os.makedirs('./causal_data/light_switch/')

for i in range(num_samples_to_save):
    switch_position = i / (num_samples_to_save-1)
    switch_angle = switch_position * 180
    fig = light_switch_and_bulb(switch_position)
    fig.savefig(f'./causal_data/light_switch/light_switch_{switch_angle:.0f}_{switch_position:.5f}.png', dpi=96)
    plt.clf()