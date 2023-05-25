import math
import tifffile

from matplotlib import animation, pyplot as plt
from tifffile import imread, imshow


def compute_min_max(data):
    min_value = math.inf
    max_value = -math.inf

    for image in data:
        for row in image:
            min_value = min(min_value, min(row))
            max_value = max(max_value, max(row))

    return min_value, max_value

dataset = imread("Braided River/detrended.tiff")

min_value = 3928808
max_value = 21311037

for t in [0, 100, 200, 300, 400, 500, 600]:
    image = imread("Braided River/detrended.tiff", key=t)
    
    fig = plt.figure(figsize=(13, 3))
    plt.imshow(image, vmin=min_value, vmax=max_value)
    plt.title(f"River bed elevation at t = {t}")
    plt.show()



fig = plt.figure("Animation of river bed elevation over time", figsize=(13, 3))

img = plt.imshow(dataset[0], vmin=min_value, vmax=max_value)

def animate(t):
    img.set_data(dataset[t])
    plt.title(f"River bed elevation at t = {t}")
    return img

anim = animation.FuncAnimation(fig, animate, frames=len(dataset), interval=10)
plt.show()