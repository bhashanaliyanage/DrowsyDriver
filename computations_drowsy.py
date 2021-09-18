import numpy as np
import winsound


def compute(pt_a, pt_b):  # Getting an average ratio
    dist = np.linalg.norm(pt_a - pt_b)
    return dist


def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    # Checking blinks
    if ratio > 0.25:
        return 2
    elif 0.21 < ratio <= 0.25:
        return 1
    else:
        return 0


def beep():
    winsound.Beep(1000, 100)
